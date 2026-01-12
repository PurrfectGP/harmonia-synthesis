/**
 * Harmonia Floating Label Input Component
 * Material Design-style floating label input with validation
 * Pure CSS animations with JavaScript enhancement
 */

class FloatingInput {
    constructor(container, options = {}) {
        this.container = typeof container === 'string'
            ? document.querySelector(container)
            : container;

        this.options = {
            type: options.type || 'text',
            label: options.label || 'Label',
            value: options.value || '',
            placeholder: options.placeholder || ' ',
            required: options.required || false,
            pattern: options.pattern || null,
            maxlength: options.maxlength || null,
            autocomplete: options.autocomplete || null,
            onChange: options.onChange || (() => {}),
            onValidate: options.onValidate || null,
            ...options
        };

        this.input = null;
        this.label = null;
        this.errorMessage = null;
        this.isValid = true;

        this.init();
    }

    init() {
        // Create wrapper
        const wrapper = document.createElement('div');
        wrapper.className = 'floating-input-wrapper';
        wrapper.style.cssText = `
            position: relative;
            margin: 1.5rem 0;
            width: 100%;
        `;

        // Create input
        this.input = document.createElement('input');
        this.input.type = this.options.type;
        this.input.value = this.options.value;
        this.input.placeholder = this.options.placeholder;
        this.input.required = this.options.required;
        if (this.options.pattern) this.input.pattern = this.options.pattern;
        if (this.options.maxlength) this.input.maxLength = this.options.maxlength;
        if (this.options.autocomplete) this.input.autocomplete = this.options.autocomplete;

        this.input.style.cssText = `
            width: 100%;
            padding: 0.75rem 0;
            border: none;
            border-bottom: 1px solid #e6ddd0;
            background: transparent;
            font-family: 'DM Sans', sans-serif;
            font-size: 1rem;
            color: #2c241b;
            transition: border-color 0.3s ease;
            outline: none;
        `;

        // Create floating label
        this.label = document.createElement('label');
        this.label.textContent = this.options.label;
        this.label.style.cssText = `
            position: absolute;
            left: 0;
            top: ${this.options.value ? '-1rem' : '0.75rem'};
            color: #2a4e6c;
            font-family: 'DM Sans', sans-serif;
            font-size: ${this.options.value ? '0.75rem' : '1rem'};
            font-weight: ${this.options.value ? '500' : '400'};
            pointer-events: none;
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            transform-origin: left top;
        `;

        // Create error message
        this.errorMessage = document.createElement('div');
        this.errorMessage.className = 'input-error';
        this.errorMessage.style.cssText = `
            position: absolute;
            bottom: -1.25rem;
            left: 0;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.75rem;
            color: #8b0000;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;

        // Event listeners
        this.input.addEventListener('focus', () => this.handleFocus());
        this.input.addEventListener('blur', () => this.handleBlur());
        this.input.addEventListener('input', (e) => this.handleInput(e));

        wrapper.appendChild(this.input);
        wrapper.appendChild(this.label);
        wrapper.appendChild(this.errorMessage);
        this.container.appendChild(wrapper);
        this.wrapper = wrapper;
    }

    handleFocus() {
        // Animate label up
        this.label.style.top = '-1rem';
        this.label.style.fontSize = '0.75rem';
        this.label.style.fontWeight = '500';

        // Change border color
        this.input.style.borderBottomColor = '#2a4e6c';
        this.input.style.borderBottomWidth = '2px';

        // Clear error state
        if (!this.isValid) {
            this.clearError();
        }
    }

    handleBlur() {
        // If empty, animate label down
        if (!this.input.value) {
            this.label.style.top = '0.75rem';
            this.label.style.fontSize = '1rem';
            this.label.style.fontWeight = '400';
        }

        // Reset border
        this.input.style.borderBottomColor = '#e6ddd0';
        this.input.style.borderBottomWidth = '1px';

        // Validate
        this.validate();
    }

    handleInput(event) {
        // Call onChange callback
        this.options.onChange(event.target.value);

        // Clear error on typing
        if (!this.isValid) {
            this.clearError();
        }
    }

    validate() {
        let valid = true;
        let errorMsg = '';

        // Required validation
        if (this.options.required && !this.input.value.trim()) {
            valid = false;
            errorMsg = `${this.options.label} is required`;
        }

        // Pattern validation
        if (valid && this.options.pattern && this.input.value) {
            const regex = new RegExp(this.options.pattern);
            if (!regex.test(this.input.value)) {
                valid = false;
                errorMsg = `Invalid ${this.options.label.toLowerCase()}`;
            }
        }

        // Custom validation
        if (valid && this.options.onValidate) {
            const customValidation = this.options.onValidate(this.input.value);
            if (customValidation !== true) {
                valid = false;
                errorMsg = customValidation || 'Invalid input';
            }
        }

        this.isValid = valid;

        if (!valid) {
            this.showError(errorMsg);
        }

        return valid;
    }

    showError(message) {
        this.isValid = false;
        this.input.style.borderBottomColor = '#8b0000';
        this.errorMessage.textContent = message;
        this.errorMessage.style.opacity = '1';
    }

    clearError() {
        this.isValid = true;
        this.input.style.borderBottomColor = '#e6ddd0';
        this.errorMessage.style.opacity = '0';
    }

    getValue() {
        return this.input.value;
    }

    setValue(value) {
        this.input.value = value;

        // Update label position
        if (value) {
            this.label.style.top = '-1rem';
            this.label.style.fontSize = '0.75rem';
            this.label.style.fontWeight = '500';
        } else {
            this.label.style.top = '0.75rem';
            this.label.style.fontSize = '1rem';
            this.label.style.fontWeight = '400';
        }
    }

    focus() {
        this.input.focus();
    }

    disable() {
        this.input.disabled = true;
        this.input.style.opacity = '0.5';
        this.input.style.cursor = 'not-allowed';
    }

    enable() {
        this.input.disabled = false;
        this.input.style.opacity = '1';
        this.input.style.cursor = 'text';
    }

    destroy() {
        if (this.wrapper && this.wrapper.parentNode) {
            this.wrapper.parentNode.removeChild(this.wrapper);
        }
    }
}

// Export for both Node.js and browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = FloatingInput;
} else {
    // Browser global export
    window.FloatingInput = FloatingInput;
}
