/**
 * Harmonia Apex Match - Module 1: Setup (Biometric Ingestion & Onboarding)
 *
 * Spec Reference: README.md Section 3 - "The Concierge Signup Flow"
 * HTML Template: modules/1-setup.html
 *
 * This module handles:
 * - Form input validation (name, email, password)
 * - Gender and seeking preference selection
 * - "Mandatory Five" baseline questions
 * - Biometric/DNA file upload or kit request
 * - Waitlist logic for gender equilibrium
 * - Progress tracking and navigation to Calibration
 *
 * Research Applied:
 * - Progressive disclosure pattern
 * - Accessible form validation (WCAG 2.2)
 * - Event delegation for performance
 * - File upload with drag-drop
 * - Component lifecycle management
 */

(function(window, document) {
    'use strict';

    // ============================================================================
    // MODULE STATE
    // ============================================================================

    let state = null; // Global app state (injected on init)
    let components = {
        nameInput: null,
        emailInput: null,
        passwordInput: null,
        genderControl: null,
        seekingControl: null,
        biometricSeal: null
    };

    // Mandatory Five Questions Data
    const MANDATORY_QUESTIONS = [
        {
            id: 1,
            text: 'When facing a social gathering, do you typically feel:',
            choices: {
                A: 'Energized by the prospect of meeting new people',
                B: 'Drained and prefer quiet reflection'
            },
            category: 'Social Battery'
        },
        {
            id: 2,
            text: 'In conflict situations, do you tend to:',
            choices: {
                A: 'Address issues directly and immediately',
                B: 'Reflect privately before engaging'
            },
            category: 'Conflict Style'
        },
        {
            id: 3,
            text: 'Your ideal weekend involves:',
            choices: {
                A: 'Pursuing ambitious goals and productivity',
                B: 'Restorative activities and leisure'
            },
            category: 'Ambition'
        },
        {
            id: 4,
            text: 'When making important decisions, you prioritize:',
            choices: {
                A: 'Logic and objective analysis',
                B: 'Intuition and emotional intelligence'
            },
            category: 'Decision Making'
        },
        {
            id: 5,
            text: 'In relationships, you value most:',
            choices: {
                A: 'Deep emotional intimacy and vulnerability',
                B: 'Intellectual connection and shared interests'
            },
            category: 'Connection Type'
        }
    ];

    // Track answered questions
    const answeredQuestions = new Set();

    // ============================================================================
    // COMPONENT INITIALIZATION
    // ============================================================================

    /**
     * Initialize floating input components
     */
    function initializeInputs() {
        // Check if FloatingInput component exists (from Session 1)
        if (typeof FloatingInput === 'undefined') {
            console.warn('[Setup] FloatingInput component not loaded, using native inputs');
            return;
        }

        // Initialize Name Input
        const nameContainer = document.getElementById('input-name-container');
        if (nameContainer) {
            components.nameInput = new FloatingInput(nameContainer, {
                label: 'Full Name',
                value: state.userData.name || '',
                required: true,
                autocomplete: 'name',
                onChange: (value) => {
                    state.userData.name = value;
                    validateForm();
                }
            });
        }

        // Initialize Email Input
        const emailContainer = document.getElementById('input-email-container');
        if (emailContainer) {
            components.emailInput = new FloatingInput(emailContainer, {
                type: 'email',
                label: 'Email Address',
                value: state.userData.email || '',
                required: true,
                pattern: '^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$',
                autocomplete: 'email',
                onChange: (value) => {
                    state.userData.email = value;
                    validateForm();
                }
            });
        }

        // Initialize Password Input
        const passwordContainer = document.getElementById('input-password-container');
        if (passwordContainer) {
            components.passwordInput = new FloatingInput(passwordContainer, {
                type: 'password',
                label: 'Password',
                value: '', // Never pre-fill password
                required: true,
                autocomplete: 'new-password',
                onValidate: (value) => {
                    if (value.length < 8) {
                        return 'Password must be at least 8 characters';
                    }
                    if (!/[A-Z]/.test(value)) {
                        return 'Password must contain at least one uppercase letter';
                    }
                    if (!/[0-9]/.test(value)) {
                        return 'Password must contain at least one number';
                    }
                    return true;
                },
                onChange: (value) => {
                    state.userData.password = value;
                    validateForm();
                }
            });
        }
    }

    /**
     * Initialize segmented controls (gender, seeking)
     */
    function initializeSegmentedControls() {
        // Check if SegmentedControl component exists
        if (typeof SegmentedControl === 'undefined') {
            console.warn('[Setup] SegmentedControl component not loaded');
            return;
        }

        // Initialize Gender Control
        const genderContainer = document.getElementById('gender-control-container');
        if (genderContainer) {
            components.genderControl = new SegmentedControl(genderContainer, {
                segments: ['Male', 'Female', 'Non-Binary'],
                selected: state.userData.gender ? ['Male', 'Female', 'Non-Binary'].indexOf(state.userData.gender) : 0,
                name: 'gender',
                onChange: (index, value) => {
                    state.userData.gender = value;
                    validateForm();
                }
            });
        }

        // Initialize Seeking Control
        const seekingContainer = document.getElementById('seeking-control-container');
        if (seekingContainer) {
            components.seekingControl = new SegmentedControl(seekingContainer, {
                segments: ['Men', 'Women', 'Everyone'],
                selected: state.userData.seeking ? ['Men', 'Women', 'Everyone'].indexOf(state.userData.seeking) : 0,
                name: 'seeking',
                onChange: (index, value) => {
                    state.userData.seeking = value;
                    validateForm();
                }
            });
        }
    }

    /**
     * Initialize Biometric Seal component
     */
    function initializeBiometricSeal() {
        // Check if BiometricSeal component exists
        if (typeof BiometricSeal === 'undefined') {
            console.warn('[Setup] BiometricSeal component not loaded');
            return;
        }

        const sealElement = document.getElementById('biometric-seal-element');
        if (sealElement) {
            components.biometricSeal = new BiometricSeal(sealElement, {
                size: 200,
                label: 'Upload Biometric Data',
                accept: '.txt,.csv,.zip',
                showProgress: true,
                onUpload: handleBiometricUpload,
                onProgress: (progress) => {
                    console.log(`[Setup] Upload progress: ${progress}%`);
                },
                onError: (error) => {
                    console.error('[Setup] Upload error:', error);
                    showNotification('Failed to upload file. Please try again.', 'error');
                }
            });
        }
    }

    // ============================================================================
    // MANDATORY FIVE QUESTIONS
    // ============================================================================

    /**
     * Load and render Mandatory Five questions
     */
    function loadMandatoryQuestions() {
        const container = document.getElementById('mandatory-questions-container');
        if (!container) return;

        const template = document.getElementById('question-card-template');
        if (!template) {
            console.warn('[Setup] Question card template not found');
            return;
        }

        // Clear existing questions
        container.innerHTML = '';

        // Render each question
        MANDATORY_QUESTIONS.forEach(question => {
            const clone = template.content.cloneNode(true);

            // Set question card attributes
            const card = clone.querySelector('.setup-question-card');
            card.dataset.question = question.id;

            // Set question text
            const questionText = clone.querySelector('.setup-question-text');
            questionText.textContent = question.text;

            // Set choice buttons
            const buttons = clone.querySelectorAll('.assessment-choice-btn');
            buttons[0].textContent = question.choices.A;
            buttons[0].dataset.choice = 'A';
            buttons[0].setAttribute('aria-label', `Choice A: ${question.choices.A}`);

            buttons[1].textContent = question.choices.B;
            buttons[1].dataset.choice = 'B';
            buttons[1].setAttribute('aria-label', `Choice B: ${question.choices.B}`);

            // Add click handlers
            buttons.forEach(btn => {
                btn.addEventListener('click', () => handleQuestionAnswer(question.id, btn.dataset.choice, card));
            });

            // Restore previous answer if exists
            if (state.mandatoryFive[question.id]) {
                const previousChoice = state.mandatoryFive[question.id];
                buttons.forEach(btn => {
                    if (btn.dataset.choice === previousChoice) {
                        btn.classList.add('selected');
                        btn.setAttribute('aria-pressed', 'true');
                    }
                });
                answeredQuestions.add(question.id);
            }

            container.appendChild(clone);
        });

        updateProgress();
    }

    /**
     * Handle answer selection for Mandatory Five
     */
    function handleQuestionAnswer(questionId, choice, cardElement) {
        // Store answer
        state.mandatoryFive[questionId] = choice;
        answeredQuestions.add(questionId);

        // Update UI - mark selected button
        const buttons = cardElement.querySelectorAll('.assessment-choice-btn');
        buttons.forEach(btn => {
            if (btn.dataset.choice === choice) {
                btn.classList.add('selected');
                btn.setAttribute('aria-pressed', 'true');
            } else {
                btn.classList.remove('selected');
                btn.setAttribute('aria-pressed', 'false');
            }
        });

        // Animate card (subtle confirmation)
        cardElement.style.transform = 'scale(0.98)';
        setTimeout(() => {
            cardElement.style.transform = 'scale(1)';
        }, 150);

        // Update progress
        updateProgress();

        // Validate form
        validateForm();

        console.log(`[Setup] Question ${questionId} answered: ${choice}`);
    }

    // ============================================================================
    // BIOMETRIC/DNA HANDLING
    // ============================================================================

    /**
     * Handle biometric file upload
     */
    function handleBiometricUpload(file, progress) {
        console.log(`[Setup] Biometric file upload:`, file.name, `${progress}%`);

        if (progress === 100) {
            // File uploaded successfully
            state.biometric.uploaded = true;
            state.biometric.fileName = file.name;

            // Show success notification
            showNotification('Biometric data uploaded successfully', 'success');

            // Validate form
            validateForm();

            // Mock processing delay (Labor Illusion)
            setTimeout(() => {
                showBiometricProcessing();
            }, 500);
        }
    }

    /**
     * Show biometric processing status (Labor Illusion)
     */
    function showBiometricProcessing() {
        const statusEl = document.getElementById('kit-request-status');
        if (!statusEl) return;

        const steps = [
            'Detecting File Format (23andMe/Ancestry)...',
            'Parsing Chromosome 6 Region...',
            'Validating 1,000+ SNP Markers...',
            'Imputing HLA-A, B, DRB1 Alleles...',
            'Processing Complete ✓'
        ];

        let currentStep = 0;
        statusEl.style.display = 'block';
        statusEl.style.fontFamily = 'var(--font-body)';
        statusEl.style.fontSize = '0.875rem';
        statusEl.style.color = 'var(--color-mediterranean-500)';

        const interval = setInterval(() => {
            statusEl.textContent = steps[currentStep];

            if (currentStep === steps.length - 1) {
                clearInterval(interval);
                statusEl.style.color = 'var(--color-champagne-500)';
            }

            currentStep++;
        }, 800); // ~3.2 seconds total (4 steps × 800ms)
    }

    /**
     * Handle DNA kit request
     */
    function handleRequestKit() {
        const gender = state.userData.gender;

        // Check gender equilibrium (mock logic)
        // In production, this would check backend API
        const maleQuotaFull = false; // Mock - would come from API

        if (gender === 'Male' && maleQuotaFull) {
            // Show waitlist modal
            showWaitlistModal();
            state.biometric.waitlisted = true;
        } else {
            // Process kit request
            state.biometric.kitRequested = true;
            showNotification('DNA testing kit requested. You will receive it within 5-7 business days.', 'success');

            // Update status
            const statusEl = document.getElementById('kit-request-status');
            if (statusEl) {
                statusEl.style.display = 'block';
                statusEl.textContent = '✓ Kit requested. Please proceed with Visual and Psychometric calibration.';
                statusEl.style.fontFamily = 'var(--font-body)';
                statusEl.style.color = 'var(--color-champagne-500)';
            }
        }

        validateForm();
    }

    /**
     * Show waitlist modal
     */
    function showWaitlistModal() {
        const message = `Due to strict scientific equilibrium protocols, the Pilot Pool for male testing kits is currently at capacity. You have been placed on the Priority Access List. Please proceed with Visual and Psychometric calibration.`;

        // In production, this would be a styled modal
        // For now, using browser alert (would replace with custom modal)
        alert(message);

        // Update status display
        const statusEl = document.getElementById('kit-request-status');
        if (statusEl) {
            statusEl.style.display = 'block';
            statusEl.textContent = '⏳ Waitlisted. Please proceed with other calibration steps.';
            statusEl.style.fontFamily = 'var(--font-body)';
            statusEl.style.color = 'var(--color-mediterranean-500)';
        }
    }

    // ============================================================================
    // FORM VALIDATION
    // ============================================================================

    /**
     * Validate entire form
     * Enable "Continue" button when all required fields are complete
     */
    function validateForm() {
        const continueBtn = document.getElementById('continue-to-calibration');
        if (!continueBtn) return;

        // Check all validation criteria
        const nameValid = state.userData.name && state.userData.name.length >= 2;
        const emailValid = state.userData.email && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(state.userData.email);
        const passwordValid = state.userData.password && state.userData.password.length >= 8;
        const genderValid = state.userData.gender !== null;
        const seekingValid = state.userData.seeking !== null;
        const mandatoryFiveComplete = answeredQuestions.size === MANDATORY_QUESTIONS.length;
        const biometricComplete = state.biometric.uploaded || state.biometric.kitRequested || state.biometric.waitlisted;

        const allValid = nameValid && emailValid && passwordValid && genderValid &&
                         seekingValid && mandatoryFiveComplete && biometricComplete;

        // Enable/disable continue button
        continueBtn.disabled = !allValid;

        // Update button appearance
        if (allValid) {
            continueBtn.classList.remove('disabled');
            continueBtn.setAttribute('aria-disabled', 'false');
        } else {
            continueBtn.classList.add('disabled');
            continueBtn.setAttribute('aria-disabled', 'true');
        }

        return allValid;
    }

    /**
     * Update progress bar
     */
    function updateProgress() {
        const progressFill = document.querySelector('.setup-progress-fill');
        if (!progressFill) return;

        // Calculate progress based on completed sections
        const totalSections = 5; // Basic info, gender, seeking, mandatory five, biometric
        let completed = 0;

        if (state.userData.name && state.userData.email && state.userData.password) completed++;
        if (state.userData.gender) completed++;
        if (state.userData.seeking) completed++;
        if (answeredQuestions.size === MANDATORY_QUESTIONS.length) completed++;
        if (state.biometric.uploaded || state.biometric.kitRequested || state.biometric.waitlisted) completed++;

        const percentage = (completed / totalSections) * 100;

        // Animate progress bar
        progressFill.style.width = `${percentage}%`;

        // Update ARIA
        const progressBar = document.querySelector('.setup-progress');
        if (progressBar) {
            progressBar.setAttribute('aria-valuenow', percentage);
        }
    }

    // ============================================================================
    // NAVIGATION
    // ============================================================================

    /**
     * Handle continue to calibration
     */
    function handleContinue(e) {
        if (e) e.preventDefault();

        // Validate form one final time
        if (!validateForm()) {
            showNotification('Please complete all required fields', 'error');
            return;
        }

        // Save state (handled by app.js automatically via Proxy)
        console.log('[Setup] Setup complete, navigating to calibration');

        // Navigate to next module
        state.currentModule = 'calibration';
    }

    // ============================================================================
    // UTILITY FUNCTIONS
    // ============================================================================

    /**
     * Show notification message
     */
    function showNotification(message, type = 'info') {
        // In production, this would use a toast/notification component
        // For now, using console + potential future notification system
        console.log(`[Setup] ${type.toUpperCase()}: ${message}`);

        // Could create a simple toast here
        const toast = document.createElement('div');
        toast.className = `notification notification-${type}`;
        toast.textContent = message;
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'error' ? '#8b0000' : 'var(--color-mediterranean-500)'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: var(--radius-md);
            font-family: var(--font-body);
            font-size: 0.875rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            z-index: 9999;
            animation: slideInRight 0.3s ease-out;
        `;

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    // ============================================================================
    // EVENT HANDLERS
    // ============================================================================

    /**
     * Set up event listeners
     */
    function setupEventListeners() {
        // Continue button
        const continueBtn = document.getElementById('continue-to-calibration');
        if (continueBtn) {
            continueBtn.addEventListener('click', handleContinue);
        }

        // Request kit button
        const requestKitBtn = document.getElementById('request-kit-btn');
        if (requestKitBtn) {
            requestKitBtn.addEventListener('click', handleRequestKit);
        }

        // Form submission (prevent default)
        const form = document.getElementById('setup-form');
        if (form) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                handleContinue(e);
            });
        }
    }

    // ============================================================================
    // MODULE INITIALIZATION
    // ============================================================================

    /**
     * Initialize Module 1: Setup
     */
    function init(appState) {
        console.log('[Setup] Initializing Module 1...');

        // Store reference to global state
        state = appState;

        // Initialize components
        initializeInputs();
        initializeSegmentedControls();
        initializeBiometricSeal();

        // Load mandatory questions
        loadMandatoryQuestions();

        // Set up event listeners
        setupEventListeners();

        // Initial validation
        validateForm();
        updateProgress();

        console.log('[Setup] Module 1 initialized');
    }

    // ============================================================================
    // PUBLIC API
    // ============================================================================

    // Register module in global namespace
    window.HarmoniaModules = window.HarmoniaModules || {};
    window.HarmoniaModules.Setup = {
        init: init,
        validateForm: validateForm,
        updateProgress: updateProgress
    };

})(window, document);
