/**
 * Harmonia Segmented Control Component
 * iOS-style segmented control with spring physics sliding background
 * Integrates: spring-physics.js
 */

class SegmentedControl {
    constructor(container, options = {}) {
        this.container = typeof container === 'string'
            ? document.querySelector(container)
            : container;

        this.options = {
            segments: options.segments || ['Option 1', 'Option 2'],
            selected: options.selected || 0,
            onChange: options.onChange || (() => {}),
            name: options.name || 'segmented-control',
            ...options
        };

        this.currentIndex = this.options.selected;
        this.slider = null;
        this.springPhysics = null;
        this.sliderPosition = 0;
        this.targetPosition = 0;
        this.velocity = 0;
        this.animationId = null;

        this.init();
    }

    init() {
        // Create control container
        const control = document.createElement('div');
        control.className = 'segmented-control';
        control.style.cssText = `
            position: relative;
            display: inline-flex;
            background: #f5f0e6;
            border-radius: 999px;
            padding: 4px;
            gap: 0;
            box-shadow: inset 0 2px 4px rgba(42, 78, 108, 0.1);
        `;

        // Create slider background
        this.slider = document.createElement('div');
        this.slider.className = 'segmented-slider';
        this.slider.style.cssText = `
            position: absolute;
            top: 4px;
            left: 4px;
            height: calc(100% - 8px);
            background: linear-gradient(135deg, #d4af37 0%, #c5a028 100%);
            border-radius: 999px;
            box-shadow: 0 2px 8px rgba(212, 175, 55, 0.3);
            transition: width 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            z-index: 1;
        `;
        control.appendChild(this.slider);

        // Create segments
        this.segments = this.options.segments.map((label, index) => {
            const segment = document.createElement('label');
            segment.className = 'segment';
            segment.style.cssText = `
                position: relative;
                padding: 0.75rem 2rem;
                cursor: pointer;
                font-family: 'DM Sans', sans-serif;
                font-weight: 500;
                font-size: 0.875rem;
                color: ${index === this.currentIndex ? '#2c241b' : '#2a4e6c'};
                transition: color 0.3s ease;
                z-index: 2;
                user-select: none;
                white-space: nowrap;
            `;

            // Hidden radio input
            const input = document.createElement('input');
            input.type = 'radio';
            input.name = this.options.name;
            input.value = index;
            input.checked = index === this.currentIndex;
            input.style.display = 'none';

            input.addEventListener('change', () => {
                this.select(index);
            });

            segment.appendChild(input);

            const labelText = document.createElement('span');
            labelText.textContent = label;
            segment.appendChild(labelText);

            control.appendChild(segment);
            return segment;
        });

        this.container.appendChild(control);
        this.control = control;

        // Initialize spring physics
        if (typeof SpringPhysics !== 'undefined') {
            this.springPhysics = new SpringPhysics({
                mass: 1,
                stiffness: 200,
                damping: 25,
                precision: 0.5
            });
        }

        // Calculate initial slider position
        this.updateSliderDimensions();
        requestAnimationFrame(() => {
            this.moveSlider(this.currentIndex, false);
        });
    }

    updateSliderDimensions() {
        // Set slider width to match segment width
        const segmentWidth = this.segments[0].offsetWidth;
        this.slider.style.width = `${segmentWidth}px`;
    }

    select(index, animate = true) {
        if (index === this.currentIndex) return;

        const previousIndex = this.currentIndex;
        this.currentIndex = index;

        // Update checked state
        this.segments.forEach((segment, i) => {
            const input = segment.querySelector('input');
            const label = segment.querySelector('span');
            input.checked = i === index;

            // Update text color
            segment.style.color = i === index ? '#2c241b' : '#2a4e6c';
        });

        // Move slider
        this.moveSlider(index, animate);

        // Call onChange callback
        this.options.onChange(index, this.options.segments[index]);
    }

    moveSlider(index, animate = true) {
        const segmentWidth = this.segments[index].offsetWidth;
        const gap = 0; // No gap in this design
        const padding = 4;
        const targetPosition = padding + (segmentWidth + gap) * index;

        if (!animate || !this.springPhysics) {
            // Instant move
            this.slider.style.transform = `translateX(${targetPosition}px)`;
            this.sliderPosition = targetPosition;
            this.targetPosition = targetPosition;
            return;
        }

        // Animate with spring physics
        this.targetPosition = targetPosition;

        if (!this.animationId) {
            this.animateSlider();
        }
    }

    animateSlider() {
        if (!this.springPhysics) return;

        const result = this.springPhysics.step(
            this.sliderPosition,
            this.targetPosition,
            this.velocity
        );

        this.sliderPosition = result.position;
        this.velocity = result.velocity;

        this.slider.style.transform = `translateX(${this.sliderPosition}px)`;

        if (!result.done) {
            this.animationId = requestAnimationFrame(() => this.animateSlider());
        } else {
            this.animationId = null;
        }
    }

    getValue() {
        return this.currentIndex;
    }

    getLabel() {
        return this.options.segments[this.currentIndex];
    }

    destroy() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
        if (this.control && this.control.parentNode) {
            this.control.parentNode.removeChild(this.control);
        }
    }
}

// Export for both Node.js and browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SegmentedControl;
} else {
    // Browser global export
    window.SegmentedControl = SegmentedControl;
}
