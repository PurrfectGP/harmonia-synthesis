/**
 * Harmonia Spring Physics
 * Smooth spring-based animations for sliders and UI elements
 * Based on research: Motion.dev and react-spring principles
 */

class SpringPhysics {
    constructor(options = {}) {
        this.config = {
            mass: options.mass || 1,
            stiffness: options.stiffness || 170,
            damping: options.damping || 26,
            precision: options.precision || 0.01,
            ...options
        };
    }

    // Calculate spring motion for a single step
    step(current, target, velocity, deltaTime = 16) {
        const { mass, stiffness, damping } = this.config;

        // Spring force: F = -k * x
        const springForce = -stiffness * (current - target);

        // Damping force: F = -c * v
        const dampingForce = -damping * velocity;

        // Total acceleration: a = F / m
        const acceleration = (springForce + dampingForce) / mass;

        // Update velocity and position
        const newVelocity = velocity + acceleration * (deltaTime / 1000);
        const newPosition = current + newVelocity * (deltaTime / 1000);

        return {
            position: newPosition,
            velocity: newVelocity,
            done: Math.abs(newVelocity) < this.config.precision &&
                  Math.abs(newPosition - target) < this.config.precision
        };
    }

    // Animate element property with spring physics
    animate(element, property, from, to, onUpdate, onComplete) {
        let currentValue = from;
        let velocity = 0;
        let animationId = null;
        let lastTime = performance.now();

        const update = (currentTime) => {
            const deltaTime = currentTime - lastTime;
            lastTime = currentTime;

            const result = this.step(currentValue, to, velocity, deltaTime);
            currentValue = result.position;
            velocity = result.velocity;

            // Call update callback
            if (onUpdate) {
                onUpdate(currentValue);
            } else if (element) {
                // Default: update CSS property
                if (property === 'x') {
                    element.style.transform = `translateX(${currentValue}px)`;
                } else if (property === 'y') {
                    element.style.transform = `translateY(${currentValue}px)`;
                } else if (property === 'scale') {
                    element.style.transform = `scale(${currentValue})`;
                } else if (property === 'opacity') {
                    element.style.opacity = currentValue;
                } else {
                    element.style[property] = currentValue;
                }
            }

            if (!result.done) {
                animationId = requestAnimationFrame(update);
            } else {
                if (onComplete) {
                    onComplete();
                }
            }
        };

        animationId = requestAnimationFrame(update);

        // Return cancel function
        return () => {
            if (animationId) {
                cancelAnimationFrame(animationId);
            }
        };
    }

    // Create a spring-based slider
    createSlider(element, options = {}) {
        const config = {
            min: options.min || 0,
            max: options.max || 100,
            value: options.value || 50,
            onChange: options.onChange || (() => {}),
            ...options
        };

        let isDragging = false;
        let targetValue = config.value;
        let currentValue = config.value;
        let velocity = 0;
        let animationId = null;

        const updatePosition = () => {
            const percent = ((currentValue - config.min) / (config.max - config.min)) * 100;
            element.style.setProperty('--slider-percent', `${percent}%`);
            config.onChange(currentValue);
        };

        const animate = () => {
            const result = this.step(currentValue, targetValue, velocity);
            currentValue = result.position;
            velocity = result.velocity;

            updatePosition();

            if (!result.done || isDragging) {
                animationId = requestAnimationFrame(animate);
            }
        };

        const setValue = (value) => {
            targetValue = Math.max(config.min, Math.min(config.max, value));
            if (!animationId) {
                animationId = requestAnimationFrame(animate);
            }
        };

        // Setup event listeners
        const handleMove = (clientX) => {
            const rect = element.getBoundingClientRect();
            const percent = Math.max(0, Math.min(1, (clientX - rect.left) / rect.width));
            const value = config.min + percent * (config.max - config.min);
            setValue(value);
        };

        element.addEventListener('mousedown', (e) => {
            isDragging = true;
            handleMove(e.clientX);
        });

        document.addEventListener('mousemove', (e) => {
            if (isDragging) {
                handleMove(e.clientX);
            }
        });

        document.addEventListener('mouseup', () => {
            isDragging = false;
        });

        // Touch events
        element.addEventListener('touchstart', (e) => {
            isDragging = true;
            handleMove(e.touches[0].clientX);
        });

        document.addEventListener('touchmove', (e) => {
            if (isDragging) {
                handleMove(e.touches[0].clientX);
            }
        });

        document.addEventListener('touchend', () => {
            isDragging = false;
        });

        // Initial position
        updatePosition();

        return {
            setValue,
            getValue: () => currentValue,
            destroy: () => {
                if (animationId) {
                    cancelAnimationFrame(animationId);
                }
            }
        };
    }
}

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SpringPhysics;
}
