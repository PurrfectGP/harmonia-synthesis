/**
 * Harmonia Biometric Seal Component
 * Circular file upload with DNA helix icon and liquid fill animation
 * Integrates: dna-helix.svg, liquid-fill.js
 */

class BiometricSeal {
    constructor(container, options = {}) {
        this.container = typeof container === 'string'
            ? document.querySelector(container)
            : container;

        this.options = {
            size: options.size || 200,
            label: options.label || 'Upload Biometric',
            accept: options.accept || 'image/*,.pdf',
            onUpload: options.onUpload || (() => {}),
            showProgress: options.showProgress !== false,
            ...options
        };

        this.liquidFill = null;
        this.fileInput = null;
        this.uploadProgress = 0;

        this.init();
    }

    init() {
        // Create seal structure
        const seal = document.createElement('div');
        seal.className = 'biometric-seal';
        seal.style.cssText = `
            position: relative;
            width: ${this.options.size}px;
            height: ${this.options.size}px;
            border-radius: 50%;
            border: 2px dashed #2a4e6c;
            background: rgba(245, 240, 230, 0.5);
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        `;

        // Create icon container
        const iconContainer = document.createElement('div');
        iconContainer.className = 'seal-icon-container';
        iconContainer.style.cssText = `
            position: relative;
            z-index: 2;
            width: 60%;
            height: 60%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            pointer-events: none;
        `;

        // Load DNA helix SVG
        fetch('assets/svg/dna-helix.svg')
            .then(response => response.text())
            .then(svgContent => {
                const icon = document.createElement('div');
                icon.innerHTML = svgContent;
                icon.style.cssText = `
                    width: 50px;
                    height: 100px;
                    opacity: 0.6;
                    transition: opacity 0.3s ease;
                `;
                iconContainer.appendChild(icon);
            });

        // Add label
        const label = document.createElement('div');
        label.textContent = this.options.label;
        label.style.cssText = `
            font-family: 'DM Sans', sans-serif;
            font-size: 0.75rem;
            font-weight: 500;
            color: #2a4e6c;
            text-align: center;
            opacity: 0.8;
        `;
        iconContainer.appendChild(label);

        // Create hidden file input
        this.fileInput = document.createElement('input');
        this.fileInput.type = 'file';
        this.fileInput.accept = this.options.accept;
        this.fileInput.style.display = 'none';
        this.fileInput.addEventListener('change', (e) => this.handleFileSelect(e));

        // Create liquid fill background
        if (this.options.showProgress) {
            const fillContainer = document.createElement('div');
            fillContainer.className = 'seal-fill-container';
            fillContainer.style.cssText = `
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 1;
            `;
            seal.appendChild(fillContainer);

            // Initialize liquid fill (starts at 0%)
            if (typeof LiquidFill !== 'undefined') {
                this.liquidFill = new LiquidFill(fillContainer, {
                    fillPercent: 0,
                    fillColor: '#d4af37',
                    waveColor: '#c5a028',
                    amplitude: 5,
                    frequency: 2
                });
            }
        }

        seal.appendChild(iconContainer);
        seal.appendChild(this.fileInput);

        // Click handler
        seal.addEventListener('click', () => {
            this.fileInput.click();
        });

        // Hover effects
        seal.addEventListener('mouseenter', () => {
            seal.style.borderColor = '#d4af37';
            seal.style.transform = 'scale(1.05)';
        });

        seal.addEventListener('mouseleave', () => {
            seal.style.borderColor = '#2a4e6c';
            seal.style.transform = 'scale(1)';
        });

        this.container.appendChild(seal);
        this.seal = seal;
    }

    handleFileSelect(event) {
        const file = event.target.files[0];
        if (!file) return;

        // Simulate upload with progress
        if (this.options.showProgress && this.liquidFill) {
            this.simulateUpload(file);
        } else {
            this.options.onUpload(file, 100);
        }
    }

    simulateUpload(file) {
        // Change border to solid during upload
        this.seal.style.borderStyle = 'solid';
        this.seal.style.borderColor = '#d4af37';

        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 15;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);

                // Animate to 100%
                if (this.liquidFill) {
                    this.liquidFill.fillTo(100, 800);
                }

                // Call completion callback
                setTimeout(() => {
                    this.options.onUpload(file, 100);
                    this.seal.style.borderColor = '#2a4e6c';
                }, 800);
            } else {
                // Update fill
                if (this.liquidFill) {
                    this.liquidFill.fillTo(progress, 200);
                }
            }
            this.uploadProgress = progress;
        }, 200);
    }

    reset() {
        if (this.liquidFill) {
            this.liquidFill.fillTo(0, 500);
        }
        this.fileInput.value = '';
        this.uploadProgress = 0;
        this.seal.style.borderStyle = 'dashed';
        this.seal.style.borderColor = '#2a4e6c';
    }

    setProgress(percent) {
        if (this.liquidFill) {
            this.liquidFill.fillTo(percent, 300);
        }
        this.uploadProgress = percent;
    }

    destroy() {
        if (this.liquidFill) {
            this.liquidFill.destroy();
        }
        if (this.seal && this.seal.parentNode) {
            this.seal.parentNode.removeChild(this.seal);
        }
    }
}

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BiometricSeal;
}
