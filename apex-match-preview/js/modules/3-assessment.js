/**
 * Harmonia Apex Match - Module 3: Assessment (The Sins & Perceived Similarity)
 *
 * Spec Reference: README.md Section 5 - "The Inquiry Deck Interface"
 * HTML Template: modules/3-assessment.html
 *
 * This module handles:
 * - Cardinal Drivers assessment (7 personality dimensions)
 * - Binary forced choice questions (A vs B)
 * - Card dissolution with gold dust particles
 * - Vertical liquid fill progress indicator
 * - Driver icon watermarks
 * - Psychometric profile building (35% of match score)
 *
 * Research Applied:
 * - Card stack UI pattern
 * - Particle effects with canvas/DOM
 * - Event delegation for buttons
 * - ARIA live regions for dynamic content
 * - requestAnimationFrame for animations
 */

(function(window, document) {
    'use strict';

    // ============================================================================
    // MODULE STATE
    // ============================================================================

    let state = null; // Global app state (injected on init)

    // Cardinal Drivers Questions (mapped from "Seven Deadly Sins")
    const CARDINAL_QUESTIONS = [
        {
            id: 1,
            driver: 'passion',      // Theological: Lust
            text: 'When you envision your ideal intimate relationship:',
            choices: {
                A: 'You prioritize intense emotional connection and vulnerability',
                B: 'You value steady companionship and mutual respect'
            }
        },
        {
            id: 2,
            driver: 'indulgence',   // Theological: Gluttony
            text: 'Your approach to life\'s pleasures:',
            choices: {
                A: 'You embrace spontaneous experiences and sensory delight',
                B: 'You prefer measured enjoyment and mindful moderation'
            }
        },
        {
            id: 3,
            driver: 'ambition',     // Theological: Greed
            text: 'In your pursuit of personal goals:',
            choices: {
                A: 'You are driven by achievement and constant growth',
                B: 'You prioritize balance and sustainable progress'
            }
        },
        {
            id: 4,
            driver: 'serenity',     // Theological: Sloth
            text: 'When facing life\'s uncertainties:',
            choices: {
                A: 'You find peace in acceptance and present-moment awareness',
                B: 'You seek control through planning and preparation'
            }
        },
        {
            id: 5,
            driver: 'conviction',   // Theological: Wrath
            text: 'Your relationship with your core values:',
            choices: {
                A: 'You hold firm principles that guide all decisions',
                B: 'You adapt your approach based on context and nuance'
            }
        },
        {
            id: 6,
            driver: 'yearning',     // Theological: Envy
            text: 'Your emotional orientation toward the future:',
            choices: {
                A: 'You feel a constant pull toward something greater',
                B: 'You find fulfillment in your current circumstances'
            }
        },
        {
            id: 7,
            driver: 'dignity',      // Theological: Pride
            text: 'Your sense of self-worth derives from:',
            choices: {
                A: 'Inherent personal value independent of achievement',
                B: 'Accomplishments and external validation'
            }
        }
    ];

    // Cardinal Driver Icon SVG paths
    const CARDINAL_ICONS = {
        passion: '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="var(--color-champagne-500)"/>',
        indulgence: '<path d="M6 3v18h12V3H6zm10 16H8V5h8v14zM11 7h2v2h-2zm0 4h2v2h-2zm0 4h2v2h-2z" fill="var(--color-champagne-500)"/>',
        ambition: '<path d="M14 2L8 13h5l-1 9 6-11h-5l1-9z" fill="var(--color-champagne-500)"/>',
        serenity: '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z" fill="var(--color-champagne-500)"/>',
        conviction: '<path d="M17 4h3v16h-3zM5 14h3v6H5zM11 9h3v11h-3z" fill="var(--color-champagne-500)"/>',
        yearning: '<path d="M12 2L4 9l8 7 8-7-8-7z" fill="var(--color-champagne-500)"/>',
        dignity: '<path d="M12 2l-2 5H5l4 3.5L7 15l5-3.5 5 3.5-2-4.5L19 7h-5l-2-5z" fill="var(--color-champagne-500)"/>'
    };

    // ============================================================================
    // QUESTION DISPLAY
    // ============================================================================

    /**
     * Load and display current question
     */
    function loadQuestion() {
        const index = state.assessment.currentIndex;

        if (index >= CARDINAL_QUESTIONS.length) {
            // Assessment complete
            completeAssessment();
            return;
        }

        const question = CARDINAL_QUESTIONS[index];

        // Update UI elements
        const card = document.getElementById('assessment-card');
        const questionText = document.getElementById('current-question-text');
        const choiceA = document.getElementById('choice-a');
        const choiceB = document.getElementById('choice-b');
        const watermark = document.getElementById('card-watermark');
        const currentNum = document.getElementById('current-question-num');
        const totalNum = document.getElementById('total-questions');

        if (!card || !questionText || !choiceA || !choiceB) {
            console.error('[Assessment] Required elements not found');
            return;
        }

        // Update card data attributes
        card.dataset.questionIndex = index;
        card.dataset.cardinalDriver = question.driver;
        card.dataset.questionId = question.id;

        // Update question text
        questionText.textContent = question.text;

        // Update choice buttons
        choiceA.textContent = question.choices.A;
        choiceA.setAttribute('aria-label', `Choice A: ${question.choices.A}`);

        choiceB.textContent = question.choices.B;
        choiceB.setAttribute('aria-label', `Choice B: ${question.choices.B}`);

        // Update watermark icon
        if (watermark) {
            const iconSvg = CARDINAL_ICONS[question.driver];
            watermark.querySelector('.cardinal-icon').innerHTML = iconSvg;
            watermark.style.opacity = '0.05';
        }

        // Update progress counter
        if (currentNum) currentNum.textContent = index + 1;
        if (totalNum) totalNum.textContent = CARDINAL_QUESTIONS.length;

        // Update progress tube
        updateProgressTube();

        // Card entrance animation
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';

        requestAnimationFrame(() => {
            card.style.transition = 'all 0.5s cubic-bezier(0.4, 0.0, 0.2, 1)';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        });

        console.log(`[Assessment] Loaded question ${index + 1}/${CARDINAL_QUESTIONS.length} (${question.driver})`);
    }

    // ============================================================================
    // ANSWER HANDLING
    // ============================================================================

    /**
     * Handle answer selection
     */
    function handleAnswer(choice) {
        const card = document.getElementById('assessment-card');
        const questionIndex = parseInt(card.dataset.questionIndex);
        const question = CARDINAL_QUESTIONS[questionIndex];

        // Record answer in state
        state.assessment.answers[question.id] = {
            driver: question.driver,
            choice: choice,
            questionText: question.text,
            choiceText: question.choices[choice],
            timestamp: Date.now()
        };

        console.log(`[Assessment] Question ${question.id} answered: ${choice} (${question.driver})`);

        // Trigger card dissolution animation
        dissolveCard(card);

        // Update progress tube
        updateProgressTube();

        // Move to next question after animation
        setTimeout(() => {
            state.assessment.currentIndex++;
            loadQuestion();
        }, 1200); // Wait for dissolution animation
    }

    // ============================================================================
    // ANIMATIONS
    // ============================================================================

    /**
     * Dissolve card into gold dust particles
     */
    function dissolveCard(cardElement) {
        if (!cardElement) return;

        // Add dissolving class
        cardElement.classList.add('dissolving');

        // Trigger particle effect
        const particlesContainer = document.getElementById('card-particles');
        if (particlesContainer) {
            triggerParticleEffect(particlesContainer);
        }

        // Remove dissolving class after animation
        setTimeout(() => {
            cardElement.classList.remove('dissolving');
        }, 1000);
    }

    /**
     * Create gold dust particle effect
     */
    function triggerParticleEffect(container) {
        if (!container) return;

        // Create particles
        const particleCount = 30;

        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'gold-particle';

            // Random position
            particle.style.left = `${Math.random() * 100}%`;
            particle.style.top = `${Math.random() * 100}%`;

            // Random animation delay
            particle.style.animationDelay = `${Math.random() * 0.5}s`;

            // Random drift direction
            const randomX = (Math.random() - 0.5) * 100;
            particle.style.setProperty('--random-x', `${randomX}px`);

            container.appendChild(particle);

            // Remove particle after animation
            setTimeout(() => {
                if (particle.parentNode) {
                    particle.remove();
                }
            }, 2000);
        }

        console.log('[Assessment] Particle effect triggered');
    }

    /**
     * Update vertical progress tube
     */
    function updateProgressTube() {
        const progressLiquid = document.getElementById('progress-liquid');
        if (!progressLiquid) return;

        const progress = ((state.assessment.currentIndex + 1) / CARDINAL_QUESTIONS.length) * 100;

        // Animate liquid fill
        progressLiquid.style.height = `${progress}%`;

        // Update ARIA
        const progressBar = progressLiquid.parentElement;
        if (progressBar) {
            progressBar.setAttribute('aria-valuenow', progress);
        }

        console.log(`[Assessment] Progress: ${progress.toFixed(1)}%`);
    }

    // ============================================================================
    // COMPLETION
    // ============================================================================

    /**
     * Complete assessment module
     */
    function completeAssessment() {
        state.assessment.completed = true;

        console.log(`[Assessment] Assessment complete! ${Object.keys(state.assessment.answers).length} questions answered`);

        // Calculate Cardinal Driver profile
        const profile = calculateCardinalProfile();
        console.log('[Assessment] Cardinal Driver Profile:', profile);

        // Show completion message
        showCompletionMessage();

        // Navigate to Analysis after brief delay
        setTimeout(() => {
            state.currentModule = 'analysis';
        }, 2000);
    }

    /**
     * Calculate Cardinal Driver profile from answers
     */
    function calculateCardinalProfile() {
        const profile = {};

        // Map answers to driver scores
        Object.values(state.assessment.answers).forEach(answer => {
            const driver = answer.driver;
            const choice = answer.choice;

            // Score: A = high score, B = low score (on that driver axis)
            // In production, this would use proper scoring algorithm
            profile[driver] = choice === 'A' ? 0.8 : 0.3;
        });

        return profile;
    }

    /**
     * Show completion message
     */
    function showCompletionMessage() {
        const container = document.querySelector('.assessment-container');
        if (!container) return;

        // Create completion overlay
        const overlay = document.createElement('div');
        overlay.className = 'assessment-completion';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(251, 249, 245, 0.95);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 200;
            animation: fadeIn 0.5s ease-out;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; max-width: 500px; padding: 2rem;">
                <h2 style="font-family: var(--font-display); font-size: 2rem; color: var(--color-mediterranean-500); margin-bottom: 1rem;">
                    Psychometric Assessment Complete
                </h2>
                <p style="font-family: var(--font-body); color: var(--color-parchment-900); opacity: 0.8; margin-bottom: 2rem;">
                    Your personality profile has been mapped across 7 Cardinal Drivers. Beginning synthesis...
                </p>
                <div style="display: inline-block; width: 50px; height: 50px; border: 4px solid var(--color-champagne-400); border-top-color: var(--color-mediterranean-500); border-radius: 50%; animation: spin 1s linear infinite;"></div>
            </div>
        `;

        document.body.appendChild(overlay);

        // Add spin animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
        `;
        document.head.appendChild(style);
    }

    // ============================================================================
    // EVENT HANDLERS
    // ============================================================================

    /**
     * Set up event listeners
     */
    function setupEventListeners() {
        // Choice button clicks (using event delegation)
        document.addEventListener('click', (e) => {
            const target = e.target;

            // Handle choice buttons within assessment module
            if (target.matches('#choice-a, #choice-b')) {
                const choice = target.id === 'choice-a' ? 'A' : 'B';
                handleAnswer(choice);
            }
        });

        // Keyboard shortcuts (A/B keys)
        document.addEventListener('keydown', (e) => {
            // Only handle if assessment module is active
            if (state && state.currentModule === 'assessment') {
                if (e.key === 'a' || e.key === 'A') {
                    e.preventDefault();
                    handleAnswer('A');
                } else if (e.key === 'b' || e.key === 'B') {
                    e.preventDefault();
                    handleAnswer('B');
                }
            }
        });
    }

    // ============================================================================
    // MODULE INITIALIZATION
    // ============================================================================

    /**
     * Initialize Module 3: Assessment
     */
    function init(appState) {
        console.log('[Assessment] Initializing Module 3...');

        // Store reference to global state
        state = appState;

        // Initialize state if needed
        if (!state.assessment.answers) {
            state.assessment.answers = {};
        }
        if (typeof state.assessment.currentIndex !== 'number') {
            state.assessment.currentIndex = 0;
        }

        // Set up event listeners
        setupEventListeners();

        // Load first question
        loadQuestion();

        console.log('[Assessment] Module 3 initialized');
    }

    // ============================================================================
    // PUBLIC API
    // ============================================================================

    // Register module in global namespace
    window.HarmoniaModules = window.HarmoniaModules || {};
    window.HarmoniaModules.Assessment = {
        init: init,
        handleAnswer: handleAnswer,
        calculateCardinalProfile: calculateCardinalProfile
    };

})(window, document);
