/**
 * Harmonia Particle System
 * Gold dust particle effects for card dissolve animations
 * Based on research: tsParticles principles but lightweight vanilla JS implementation
 */

class HarmoniaParticles {
    constructor(container, options = {}) {
        this.container = typeof container === 'string'
            ? document.querySelector(container)
            : container;

        this.options = {
            particleCount: options.particleCount || 50,
            color: options.color || '#d4af37', // Gold Champagne
            size: options.size || 3,
            speed: options.speed || 2,
            direction: options.direction || 'up', // 'up', 'down', 'random'
            opacity: options.opacity || 0.8,
            ...options
        };

        this.particles = [];
        this.canvas = null;
        this.ctx = null;
        this.animationId = null;

        this.init();
    }

    init() {
        // Create canvas
        this.canvas = document.createElement('canvas');
        this.canvas.style.position = 'absolute';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.zIndex = '1000';

        this.container.style.position = 'relative';
        this.container.appendChild(this.canvas);

        this.ctx = this.canvas.getContext('2d');
        this.resize();

        window.addEventListener('resize', () => this.resize());
    }

    resize() {
        const rect = this.container.getBoundingClientRect();
        this.canvas.width = rect.width;
        this.canvas.height = rect.height;
    }

    createParticle(x, y) {
        return {
            x: x || Math.random() * this.canvas.width,
            y: y || Math.random() * this.canvas.height,
            vx: (Math.random() - 0.5) * this.options.speed,
            vy: this.options.direction === 'up'
                ? -(Math.random() * this.options.speed + 1)
                : this.options.direction === 'down'
                ? (Math.random() * this.options.speed + 1)
                : (Math.random() - 0.5) * this.options.speed,
            size: this.options.size + Math.random() * 2,
            opacity: this.options.opacity,
            life: 1.0,
            decay: 0.01 + Math.random() * 0.02
        };
    }

    burst(x, y, count) {
        for (let i = 0; i < (count || this.options.particleCount); i++) {
            this.particles.push(this.createParticle(x, y));
        }

        if (!this.animationId) {
            this.animate();
        }
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        this.particles = this.particles.filter(particle => {
            // Update position
            particle.x += particle.vx;
            particle.y += particle.vy;
            particle.life -= particle.decay;
            particle.opacity = this.options.opacity * particle.life;

            // Draw particle
            if (particle.life > 0) {
                this.ctx.fillStyle = this.hexToRGBA(this.options.color, particle.opacity);
                this.ctx.beginPath();
                this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                this.ctx.fill();
                return true;
            }
            return false;
        });

        if (this.particles.length > 0) {
            this.animationId = requestAnimationFrame(() => this.animate());
        } else {
            this.animationId = null;
        }
    }

    hexToRGBA(hex, alpha) {
        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);
        return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    }

    dissolveElement(element) {
        const rect = element.getBoundingClientRect();
        const containerRect = this.container.getBoundingClientRect();

        // Create particles from element position
        const particlesPerSide = Math.ceil(this.options.particleCount / 4);

        for (let i = 0; i < particlesPerSide; i++) {
            const progress = i / particlesPerSide;

            // Top edge
            this.particles.push(this.createParticle(
                rect.left - containerRect.left + rect.width * progress,
                rect.top - containerRect.top
            ));

            // Right edge
            this.particles.push(this.createParticle(
                rect.right - containerRect.left,
                rect.top - containerRect.top + rect.height * progress
            ));

            // Bottom edge
            this.particles.push(this.createParticle(
                rect.left - containerRect.left + rect.width * (1 - progress),
                rect.bottom - containerRect.top
            ));

            // Left edge
            this.particles.push(this.createParticle(
                rect.left - containerRect.left,
                rect.top - containerRect.top + rect.height * (1 - progress)
            ));
        }

        // Fade out element
        element.style.transition = 'opacity 0.6s ease-out';
        element.style.opacity = '0';

        if (!this.animationId) {
            this.animate();
        }
    }

    destroy() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
        if (this.canvas && this.canvas.parentNode) {
            this.canvas.parentNode.removeChild(this.canvas);
        }
        window.removeEventListener('resize', () => this.resize());
    }
}

// Export for both Node.js and browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HarmoniaParticles;
} else {
    // Browser global export
    window.HarmoniaParticles = HarmoniaParticles;
}
