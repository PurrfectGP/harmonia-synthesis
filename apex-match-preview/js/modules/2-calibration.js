/**
 * Harmonia Apex Match - Module 2: Calibration (The Meta FP Engine)
 *
 * Spec Reference: README.md Section 4 - "The Portrait Gallery"
 * HTML Template: modules/2-calibration.html
 *
 * This module handles:
 * - Visual preference calibration (50% of match score)
 * - Portrait gallery with 5-point Likert scale
 * - Dwell time tracking (performance.now())
 * - Decision velocity calculation
 * - Golden hour glow effect for high ratings (4-5)
 * - Mix of Meta FP stock images and real profiles
 * - Progress tracking through 50 portraits
 *
 * Research Applied:
 * - Dwell time tracking with performance.now()
 * - Custom range slider with ARIA
 * - Spring physics for slider feel
 * - Implicit signal capture
 * - requestAnimationFrame for smooth animations
 */

(function(window, document) {
    'use strict';

    // ============================================================================
    // MODULE STATE
    // ============================================================================

    let state = null; // Global app state (injected on init)
    let currentPortraitStartTime = null;
    let sliderMoveCount = 0;
    let lastSliderValue = 3;

    // Portrait dataset (mix of Meta FP stock and real profiles)
    const PORTRAIT_DATASET = generatePortraitDataset();

    // ============================================================================
    // PORTRAIT DATA GENERATION
    // ============================================================================

    /**
     * Generate portrait dataset
     * Mix of 14-50 stock images (Meta FP) with real profiles
     */
    function generatePortraitDataset() {
        const portraits = [];

        // For demo purposes, using placeholder images
        // In production, this would fetch from API
        for (let i = 0; i < 50; i++) {
            portraits.push({
                id: `portrait_${i + 1}`,
                imageUrl: `https://via.placeholder.com/400x600/e6ddd0/2a4e6c?text=Portrait+${i + 1}`,
                type: i < 20 ? 'stock' : 'real', // First 20 are stock (Meta FP), rest are real
                metadata: {
                    // Additional metadata for analysis (not shown to user)
                    ethnicity: ['Caucasian', 'African', 'Asian', 'Hispanic', 'Mixed'][Math.floor(Math.random() * 5)],
                    ageRange: ['20-25', '26-30', '31-35', '36-40'][Math.floor(Math.random() * 4)]
                }
            });
        }

        return portraits;
    }

    // ============================================================================
    // PORTRAIT DISPLAY
    // ============================================================================

    /**
     * Load and display current portrait
     */
    function loadPortrait() {
        const index = state.calibration.currentIndex;

        if (index >= PORTRAIT_DATASET.length) {
            // Calibration complete
            completeCalibration();
            return;
        }

        const portrait = PORTRAIT_DATASET[index];

        // Update UI elements
        const portraitFrame = document.getElementById('portrait-frame');
        const portraitImage = document.getElementById('portrait-image');
        const portraitDescription = document.getElementById('portrait-description');
        const currentCounter = document.getElementById('current-portrait');
        const totalCounter = document.getElementById('total-portraits');

        if (!portraitFrame || !portraitImage) {
            console.error('[Calibration] Portrait elements not found');
            return;
        }

        // Update image
        portraitImage.src = portrait.imageUrl;
        portraitImage.alt = `Portrait ${index + 1}`;

        // Update data attributes
        portraitFrame.dataset.portraitIndex = index;
        portraitFrame.dataset.portraitType = portrait.type;
        portraitFrame.dataset.portraitId = portrait.id;

        // Update screen reader description
        if (portraitDescription) {
            portraitDescription.textContent = `Portrait ${index + 1} of ${PORTRAIT_DATASET.length}. ${
                portrait.type === 'stock' ? 'Calibration image' : 'Profile'
            }.`;
        }

        // Update progress counter
        if (currentCounter) currentCounter.textContent = index + 1;
        if (totalCounter) totalCounter.textContent = PORTRAIT_DATASET.length;

        // Reset slider to middle position
        const slider = document.getElementById('calibration-slider');
        if (slider) {
            slider.value = 3;
            lastSliderValue = 3;
            updateFeedback(3);
        }

        // Remove previous magnetic class
        portraitFrame.classList.remove('magnetic');

        // Start dwell time tracking
        startDwellTracking();

        // Reset slider movement counter
        sliderMoveCount = 0;

        // Fade in animation
        portraitImage.style.opacity = '0';
        portraitImage.style.transform = 'scale(0.95)';

        // Wait for image to load
        portraitImage.onload = () => {
            requestAnimationFrame(() => {
                portraitImage.style.transition = 'all 0.4s cubic-bezier(0.4, 0.0, 0.2, 1)';
                portraitImage.style.opacity = '1';
                portraitImage.style.transform = 'scale(1)';
            });
        };

        console.log(`[Calibration] Loaded portrait ${index + 1}/${PORTRAIT_DATASET.length} (${portrait.type})`);
    }

    // ============================================================================
    // DWELL TIME TRACKING
    // ============================================================================

    /**
     * Start tracking dwell time for current portrait
     */
    function startDwellTracking() {
        currentPortraitStartTime = performance.now();

        const portraitFrame = document.getElementById('portrait-frame');
        if (portraitFrame) {
            portraitFrame.dataset.dwellStart = currentPortraitStartTime.toString();
        }

        console.log(`[Calibration] Dwell tracking started at ${currentPortraitStartTime.toFixed(2)}ms`);
    }

    /**
     * Calculate dwell time and decision metrics
     */
    function calculateMetrics() {
        if (!currentPortraitStartTime) {
            console.warn('[Calibration] No dwell start time recorded');
            return null;
        }

        const dwellTime = performance.now() - currentPortraitStartTime;
        const slider = document.getElementById('calibration-slider');
        const currentRating = slider ? parseInt(slider.value) : 3;

        const portraitFrame = document.getElementById('portrait-frame');
        const portraitId = portraitFrame?.dataset.portraitId;
        const portraitType = portraitFrame?.dataset.portraitType;

        // Decision velocity categorization
        // Fast: < 2s (visceral/instinctive)
        // Medium: 2-5s (deliberative)
        // Slow: > 5s (analytical)
        let decisionVelocity;
        if (dwellTime < 2000) {
            decisionVelocity = 'fast';
        } else if (dwellTime < 5000) {
            decisionVelocity = 'medium';
        } else {
            decisionVelocity = 'slow';
        }

        return {
            portraitId: portraitId,
            portraitType: portraitType,
            rating: currentRating,
            dwellTimeMs: Math.round(dwellTime),
            decisionVelocity: decisionVelocity,
            sliderMovements: sliderMoveCount,
            timestamp: Date.now()
        };
    }

    // ============================================================================
    // SLIDER HANDLING
    // ============================================================================

    /**
     * Initialize slider with spring physics and ARIA
     */
    function initializeSlider() {
        const slider = document.getElementById('calibration-slider');
        if (!slider) return;

        // Apply spring physics if library is available
        if (window.SpringPhysics && typeof window.SpringPhysics.applyToSlider === 'function') {
            window.SpringPhysics.applyToSlider(slider, {
                stiffness: 0.3,
                damping: 0.7,
                mass: 1.0
            });
        }

        // Update feedback on slider input
        slider.addEventListener('input', (e) => {
            const value = parseInt(e.target.value);

            // Track slider movement
            if (value !== lastSliderValue) {
                sliderMoveCount++;
                lastSliderValue = value;
            }

            updateFeedback(value);
        });

        // Keyboard navigation (Home/End keys)
        slider.addEventListener('keydown', (e) => {
            if (e.key === 'Home') {
                e.preventDefault();
                slider.value = 1;
                updateFeedback(1);
                sliderMoveCount++;
            } else if (e.key === 'End') {
                e.preventDefault();
                slider.value = 5;
                updateFeedback(5);
                sliderMoveCount++;
            }
        });

        console.log('[Calibration] Slider initialized');
    }

    /**
     * Update feedback text and visual effects based on slider value
     */
    function updateFeedback(value) {
        const feedback = document.getElementById('calibration-feedback');
        const slider = document.getElementById('calibration-slider');
        const portraitFrame = document.getElementById('portrait-frame');

        if (!feedback || !slider) return;

        // Feedback mapping
        const feedbackMap = {
            1: { text: 'Indifferent', class: 'indifferent' },
            2: { text: 'Indifferent', class: 'indifferent' },
            3: { text: 'Potential', class: 'potential' },
            4: { text: 'Magnetic', class: 'magnetic' },
            5: { text: 'Magnetic', class: 'magnetic' }
        };

        const current = feedbackMap[value];

        // Update feedback text and class
        feedback.textContent = current.text;
        feedback.className = `calibration-feedback ${current.class}`;

        // Update ARIA attributes
        slider.setAttribute('aria-valuetext', current.text);
        slider.setAttribute('aria-valuenow', value);

        // Apply golden hour glow for magnetic ratings (4-5)
        if (portraitFrame) {
            if (current.class === 'magnetic') {
                portraitFrame.classList.add('magnetic');
            } else {
                portraitFrame.classList.remove('magnetic');
            }
        }

        console.log(`[Calibration] Slider value: ${value} (${current.text})`);
    }

    // ============================================================================
    // RATING SUBMISSION
    // ============================================================================

    /**
     * Submit rating and move to next portrait
     */
    function submitRating() {
        const metrics = calculateMetrics();

        if (!metrics) {
            console.error('[Calibration] Failed to calculate metrics');
            return;
        }

        // Store in global state
        state.calibration.scores.push(metrics);

        console.log(`[Calibration] Rating submitted:`, metrics);

        // Move to next portrait
        state.calibration.currentIndex++;

        // Add transition effect
        const portraitImage = document.getElementById('portrait-image');
        if (portraitImage) {
            portraitImage.style.transition = 'all 0.3s ease-out';
            portraitImage.style.opacity = '0';
            portraitImage.style.transform = 'scale(0.95)';
        }

        // Load next portrait after brief delay
        setTimeout(() => {
            loadPortrait();
        }, 300);
    }

    /**
     * Skip current portrait
     */
    function skipPortrait() {
        const portraitFrame = document.getElementById('portrait-frame');
        const portraitId = portraitFrame?.dataset.portraitId;
        const portraitType = portraitFrame?.dataset.portraitType;

        // Record skip (null rating) for analytics
        state.calibration.scores.push({
            portraitId: portraitId,
            portraitType: portraitType,
            rating: null,
            skipped: true,
            dwellTimeMs: currentPortraitStartTime ? Math.round(performance.now() - currentPortraitStartTime) : 0,
            timestamp: Date.now()
        });

        console.log(`[Calibration] Portrait skipped: ${portraitId}`);

        // Move to next
        state.calibration.currentIndex++;
        loadPortrait();
    }

    // ============================================================================
    // COMPLETION
    // ============================================================================

    /**
     * Complete calibration module
     */
    function completeCalibration() {
        state.calibration.completed = true;

        console.log(`[Calibration] Calibration complete! ${state.calibration.scores.length} portraits rated`);

        // Calculate summary statistics
        const stats = calculateStats();
        console.log('[Calibration] Statistics:', stats);

        // Show completion message
        showCompletionMessage(stats);

        // Navigate to Assessment after brief delay
        setTimeout(() => {
            state.currentModule = 'assessment';
        }, 2000);
    }

    /**
     * Calculate calibration statistics
     */
    function calculateStats() {
        const scores = state.calibration.scores.filter(s => !s.skipped);

        const avgRating = scores.reduce((sum, s) => sum + s.rating, 0) / scores.length;
        const avgDwellTime = scores.reduce((sum, s) => sum + s.dwellTimeMs, 0) / scores.length;

        const velocityCounts = {
            fast: scores.filter(s => s.decisionVelocity === 'fast').length,
            medium: scores.filter(s => s.decisionVelocity === 'medium').length,
            slow: scores.filter(s => s.decisionVelocity === 'slow').length
        };

        const highRatings = scores.filter(s => s.rating >= 4).length;
        const lowRatings = scores.filter(s => s.rating <= 2).length;

        return {
            totalRated: scores.length,
            totalSkipped: state.calibration.scores.length - scores.length,
            avgRating: avgRating.toFixed(2),
            avgDwellTimeMs: Math.round(avgDwellTime),
            velocityCounts: velocityCounts,
            highRatings: highRatings,
            lowRatings: lowRatings
        };
    }

    /**
     * Show completion message
     */
    function showCompletionMessage(stats) {
        const gallery = document.querySelector('.calibration-gallery');
        if (!gallery) return;

        // Create completion overlay
        const overlay = document.createElement('div');
        overlay.className = 'calibration-completion';
        overlay.style.cssText = `
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(251, 249, 245, 0.95);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 100;
            animation: fadeIn 0.5s ease-out;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; max-width: 500px; padding: 2rem;">
                <h2 style="font-family: var(--font-display); font-size: 2rem; color: var(--color-mediterranean-500); margin-bottom: 1rem;">
                    Visual Calibration Complete
                </h2>
                <p style="font-family: var(--font-body); color: var(--color-parchment-900); opacity: 0.8; margin-bottom: 2rem;">
                    Your aesthetic preferences have been captured. Moving to psychometric assessment...
                </p>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; font-family: var(--font-body); font-size: 0.875rem;">
                    <div style="background: rgba(212, 175, 55, 0.1); padding: 1rem; border-radius: var(--radius-md);">
                        <div style="font-weight: 600; color: var(--color-mediterranean-500);">Avg Rating</div>
                        <div style="font-size: 1.5rem; color: var(--color-champagne-500);">${stats.avgRating}</div>
                    </div>
                    <div style="background: rgba(212, 175, 55, 0.1); padding: 1rem; border-radius: var(--radius-md);">
                        <div style="font-weight: 600; color: var(--color-mediterranean-500);">Avg Time</div>
                        <div style="font-size: 1.5rem; color: var(--color-champagne-500);">${(stats.avgDwellTimeMs / 1000).toFixed(1)}s</div>
                    </div>
                </div>
            </div>
        `;

        gallery.style.position = 'relative';
        gallery.appendChild(overlay);
    }

    // ============================================================================
    // EVENT HANDLERS
    // ============================================================================

    /**
     * Set up event listeners
     */
    function setupEventListeners() {
        // Submit rating button
        const submitBtn = document.getElementById('submit-rating-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', submitRating);
        }

        // Skip button
        const skipBtn = document.getElementById('skip-portrait-btn');
        if (skipBtn) {
            skipBtn.addEventListener('click', skipPortrait);
        }

        // Enter key to submit
        const slider = document.getElementById('calibration-slider');
        if (slider) {
            slider.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    submitRating();
                }
            });
        }
    }

    // ============================================================================
    // MODULE INITIALIZATION
    // ============================================================================

    /**
     * Initialize Module 2: Calibration
     */
    function init(appState) {
        console.log('[Calibration] Initializing Module 2...');

        // Store reference to global state
        state = appState;

        // Initialize state if needed
        if (!state.calibration.scores) {
            state.calibration.scores = [];
        }
        if (typeof state.calibration.currentIndex !== 'number') {
            state.calibration.currentIndex = 0;
        }

        // Initialize slider
        initializeSlider();

        // Set up event listeners
        setupEventListeners();

        // Load first portrait
        loadPortrait();

        console.log('[Calibration] Module 2 initialized');
    }

    // ============================================================================
    // PUBLIC API
    // ============================================================================

    // Register module in global namespace
    window.HarmoniaModules = window.HarmoniaModules || {};
    window.HarmoniaModules.Calibration = {
        init: init,
        submitRating: submitRating,
        skipPortrait: skipPortrait,
        calculateStats: calculateStats
    };

})(window, document);
