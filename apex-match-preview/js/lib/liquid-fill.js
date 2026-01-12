/**
 * Harmonia Liquid Fill Animation
 * Circular progress fill with wave effect
 * Based on research: Pure CSS/SVG liquid fill techniques
 */

class LiquidFill {
    constructor(container, options = {}) {
        this.container = typeof container === 'string'
            ? document.querySelector(container)
            : container;

        this.options = {
            fillPercent: options.fillPercent || 0,
            fillColor: options.fillColor || '#d4af37', // Gold Champagne
            waveColor: options.waveColor || '#c5a028',
            waveAmplitude: options.waveAmplitude || 5,
            waveFrequency: options.waveFrequency || 2,
            animationDuration: options.animationDuration || 2000,
            ...options
        };

        this.svgNS = 'http://www.w3.org/2000/svg';
        this.svg = null;
        this.wave1 = null;
        this.wave2 = null;
        this.animating = false;

        this.init();
    }

    init() {
        const size = this.container.clientWidth || 200;

        // Create SVG
        this.svg = document.createElementNS(this.svgNS, 'svg');
        this.svg.setAttribute('viewBox', `0 0 ${size} ${size}`);
        this.svg.setAttribute('width', size);
        this.svg.setAttribute('height', size);
        this.svg.style.overflow = 'visible';

        // Create clip path for circular mask
        const defs = document.createElementNS(this.svgNS, 'defs');
        const clipPath = document.createElementNS(this.svgNS, 'clipPath');
        clipPath.setAttribute('id', `liquidClip_${Date.now()}`);
        const circle = document.createElementNS(this.svgNS, 'circle');
        circle.setAttribute('cx', size / 2);
        circle.setAttribute('cy', size / 2);
        circle.setAttribute('r', size / 2);
        clipPath.appendChild(circle);
        defs.appendChild(clipPath);
        this.svg.appendChild(defs);

        // Create wave group
        const waveGroup = document.createElementNS(this.svgNS, 'g');
        waveGroup.setAttribute('clip-path', `url(#${clipPath.getAttribute('id')})`);

        // Background fill
        const background = document.createElementNS(this.svgNS, 'rect');
        background.setAttribute('x', 0);
        background.setAttribute('y', size);
        background.setAttribute('width', size);
        background.setAttribute('height', 0);
        background.setAttribute('fill', this.options.fillColor);
        background.classList.add('liquid-bg');

        // Create two wave paths for layered effect
        this.wave1 = this.createWavePath(size, 0);
        this.wave2 = this.createWavePath(size, Math.PI);

        waveGroup.appendChild(background);
        waveGroup.appendChild(this.wave1);
        waveGroup.appendChild(this.wave2);
        this.svg.appendChild(waveGroup);

        this.container.appendChild(this.svg);
    }

    createWavePath(size, phase) {
        const wave = document.createElementNS(this.svgNS, 'path');
        wave.setAttribute('fill', this.options.waveColor);
        wave.setAttribute('opacity', '0.7');

        const path = this.generateWavePath(size, size, phase);
        wave.setAttribute('d', path);

        return wave;
    }

    generateWavePath(size, yPos, phase) {
        const amplitude = this.options.waveAmplitude;
        const frequency = this.options.waveFrequency;
        const points = 50;

        let path = `M 0,${yPos}`;

        for (let i = 0; i <= points; i++) {
            const x = (i / points) * size;
            const y = yPos + Math.sin((i / points) * Math.PI * frequency + phase) * amplitude;
            path += ` L ${x},${y}`;
        }

        path += ` L ${size},${size} L 0,${size} Z`;
        return path;
    }

    fillTo(percent, duration) {
        const size = this.svg.getAttribute('width');
        const targetY = size - (size * percent / 100);

        this.animating = true;
        const startTime = performance.now();
        const animDuration = duration || this.options.animationDuration;

        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / animDuration, 1);

            // Easing function (ease-in-out)
            const eased = progress < 0.5
                ? 2 * progress * progress
                : 1 - Math.pow(-2 * progress + 2, 2) / 2;

            const currentY = size - (size * this.options.fillPercent / 100);
            const newY = currentY + (targetY - currentY) * eased;

            // Update background
            const bg = this.svg.querySelector('.liquid-bg');
            bg.setAttribute('y', newY);
            bg.setAttribute('height', size - newY);

            // Animate waves
            const time = elapsed / 1000;
            const wave1Path = this.generateWavePath(size, newY, time * Math.PI);
            const wave2Path = this.generateWavePath(size, newY, time * Math.PI + Math.PI);

            this.wave1.setAttribute('d', wave1Path);
            this.wave2.setAttribute('d', wave2Path);

            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                this.options.fillPercent = percent;
                this.animating = false;
            }
        };

        requestAnimationFrame(animate);
    }

    destroy() {
        if (this.svg && this.svg.parentNode) {
            this.svg.parentNode.removeChild(this.svg);
        }
    }
}

// Export for both Node.js and browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LiquidFill;
} else {
    // Browser global export
    window.LiquidFill = LiquidFill;
}
