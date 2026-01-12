/**
 * Harmonia Apex Match - Module 5: Results (The Apex Match Reveal)
 *
 * Spec Reference: README.md Section 7 - "The Apex Match Reveal"
 * HTML Template: modules/5-results.html
 *
 * This module handles:
 * - Match score reveal with count-up animation
 * - Profile display with spark indicator
 * - Tri-factor breakdown visualization
 * - Cardinal Drivers radar chart
 * - HLA chromosome compatibility map
 * - Action buttons (Like, Skip, Review)
 * - Ethical transparency disclosure
 *
 * Research Applied:
 * - requestAnimationFrame for count-up animation
 * - SVG radar chart rendering
 * - Accessible data visualization
 * - Button event handling
 * - Details/summary disclosure pattern
 */

(function(window, document) {
    'use strict';

    // ============================================================================
    // MODULE STATE
    // ============================================================================

    let state = null; // Global app state (injected on init)

    // ============================================================================
    // SCORE ANIMATION
    // ============================================================================

    /**
     * Animate match score count-up
     */
    function animateScoreCountUp(targetScore) {
        const scoreElement = document.querySelector('.score-number');
        if (!scoreElement) return;

        let currentScore = 0;
        const duration = 2000; // 2 seconds
        const startTime = performance.now();

        function updateScore(timestamp) {
            const elapsed = timestamp - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Easing function (ease-out cubic)
            const eased = 1 - Math.pow(1 - progress, 3);

            currentScore = Math.round(targetScore * eased);
            scoreElement.textContent = currentScore;

            if (progress < 1) {
                requestAnimationFrame(updateScore);
            } else {
                // Ensure final score is exact
                scoreElement.textContent = targetScore;
            }
        }

        requestAnimationFrame(updateScore);

        console.log(`[Results] Score animation: 0 → ${targetScore}`);
    }

    // ============================================================================
    // PROFILE DISPLAY
    // ============================================================================

    /**
     * Load and display match profile
     */
    function loadProfile() {
        const profile = state.results.profile;
        if (!profile) {
            console.error('[Results] No profile data available');
            return;
        }

        // Update profile elements
        const portraitImage = document.getElementById('profile-portrait');
        const nameText = document.getElementById('profile-name-text');
        const ageText = document.getElementById('profile-age');
        const locationText = document.getElementById('profile-location');
        const bioText = document.querySelector('.profile-bio-preview');

        if (portraitImage) {
            portraitImage.src = profile.portraitUrl;
            portraitImage.alt = `${profile.name}'s profile portrait`;
        }

        if (nameText) nameText.textContent = profile.name;
        if (ageText) ageText.textContent = profile.age;
        if (locationText) locationText.textContent = profile.location;
        if (bioText) bioText.textContent = profile.bio;

        // Update spark indicator
        updateSparkIndicator(state.results.spark);

        console.log('[Results] Profile loaded:', profile.name);
    }

    /**
     * Update spark indicator based on chemistry level
     */
    function updateSparkIndicator(sparkLevel) {
        const sparkIndicator = document.getElementById('spark-indicator');
        const sparkLabel = sparkIndicator?.querySelector('.spark-label');

        if (!sparkIndicator || !sparkLabel) return;

        sparkIndicator.dataset.spark = sparkLevel;

        const sparkLabels = {
            'high': 'High Chemistry',
            'medium': 'Good Chemistry',
            'low': 'Potential Chemistry'
        };

        sparkLabel.textContent = sparkLabels[sparkLevel] || 'Chemistry Detected';

        console.log(`[Results] Spark level: ${sparkLevel}`);
    }

    // ============================================================================
    // TRI-FACTOR VISUALIZATION
    // ============================================================================

    /**
     * Update tri-factor breakdown scores
     */
    function updateTriFactorBreakdown() {
        const factors = state.results.factors;

        // Update each factor card
        updateFactorScore('visual', factors.visual);
        updateFactorScore('psychometric', factors.psychometric);
        updateFactorScore('genetic', factors.genetic);
        updateFactorScore('serendipity', factors.serendipity);

        console.log('[Results] Tri-factor breakdown updated:', factors);
    }

    /**
     * Update individual factor score
     */
    function updateFactorScore(factorName, score) {
        const factorCard = document.querySelector(`[data-factor="${factorName}"]`);
        if (!factorCard) return;

        const scoreElement = factorCard.querySelector('.factor-score');
        if (scoreElement) {
            // Animate score count-up (faster than main score)
            animateFactorScore(scoreElement, score);
        }
    }

    /**
     * Animate individual factor score
     */
    function animateFactorScore(element, targetScore) {
        let currentScore = 0;
        const duration = 1500; // 1.5 seconds
        const startTime = performance.now();

        function updateScore(timestamp) {
            const elapsed = timestamp - startTime;
            const progress = Math.min(elapsed / duration, 1);

            currentScore = Math.round(targetScore * progress);
            element.textContent = `${currentScore}%`;

            if (progress < 1) {
                requestAnimationFrame(updateScore);
            } else {
                element.textContent = `${targetScore}%`;
            }
        }

        requestAnimationFrame(updateScore);
    }

    // ============================================================================
    // RADAR CHART
    // ============================================================================

    /**
     * Update Cardinal Drivers radar chart
     */
    function updateRadarChart() {
        const drivers = state.results.cardinalDrivers;
        if (!drivers) return;

        // Update radar chart polygons
        const userPolygon = document.getElementById('radar-user-profile');
        const matchPolygon = document.getElementById('radar-match-profile');

        if (userPolygon && matchPolygon) {
            // Calculate polygon points (heptagonal, 7 axes)
            const userPoints = calculateRadarPoints(drivers, 'you');
            const matchPoints = calculateRadarPoints(drivers, 'match');

            userPolygon.setAttribute('points', userPoints);
            matchPolygon.setAttribute('points', matchPoints);

            console.log('[Results] Radar chart updated');
        }
    }

    /**
     * Calculate radar chart polygon points
     */
    function calculateRadarPoints(drivers, who) {
        const centerX = 200;
        const centerY = 200;
        const maxRadius = 150;

        // Order of drivers in heptagon (7 points)
        const driverOrder = ['passion', 'indulgence', 'ambition', 'serenity', 'conviction', 'yearning', 'dignity'];

        const points = driverOrder.map((driver, index) => {
            const value = drivers[driver] ? drivers[driver][who] : 50;
            const angle = (Math.PI * 2 * index) / 7 - Math.PI / 2; // Start at top
            const radius = (value / 100) * maxRadius;

            const x = centerX + radius * Math.cos(angle);
            const y = centerY + radius * Math.sin(angle);

            return `${x},${y}`;
        });

        return points.join(' ');
    }

    // ============================================================================
    // CHROMOSOME MAP
    // ============================================================================

    /**
     * Update HLA chromosome compatibility visualization
     */
    function updateChromosomeMap() {
        const hlaData = state.results.hlaCompatibility;
        if (!hlaData) return;

        // Update compatibility percentages on connection lines
        const loci = hlaData.loci || [];
        loci.forEach((locus, index) => {
            // In production, would update actual SVG text elements
            console.log(`[Results] ${locus.name}: ${locus.compatibility}%`);
        });

        console.log('[Results] Chromosome map updated:', hlaData);
    }

    // ============================================================================
    // ACTION BUTTONS
    // ============================================================================

    /**
     * Handle "Send Like" action
     */
    function handleSendLike() {
        console.log('[Results] Send Like clicked');

        // In production, would send API request
        showNotification('Like sent! Waiting for mutual match...', 'success');

        // Mock: Navigate to next match or dashboard
        setTimeout(() => {
            alert('This would navigate to your matches dashboard or next profile in production.');
        }, 2000);
    }

    /**
     * Handle "Skip" action
     */
    function handleSkip() {
        console.log('[Results] Skip clicked');

        // In production, would record skip and load next match
        showNotification('Profile skipped. Loading next match...', 'info');

        setTimeout(() => {
            alert('This would load the next match profile in production.');
        }, 1500);
    }

    /**
     * Handle "Review Full Profile" action
     */
    function handleReviewProfile() {
        console.log('[Results] Review Profile clicked');

        // In production, would navigate to detailed profile view
        alert('This would open the full profile view with additional details, photos, and conversation starters.');
    }

    /**
     * Show notification toast
     */
    function showNotification(message, type = 'info') {
        console.log(`[Results] ${type.toUpperCase()}: ${message}`);

        const toast = document.createElement('div');
        toast.className = `notification notification-${type}`;
        toast.textContent = message;
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? 'var(--color-champagne-500)' : 'var(--color-mediterranean-500)'};
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
        // Send Like button
        const sendLikeBtn = document.getElementById('send-like-btn');
        if (sendLikeBtn) {
            sendLikeBtn.addEventListener('click', handleSendLike);
        }

        // Skip button
        const skipBtn = document.getElementById('skip-match-btn');
        if (skipBtn) {
            skipBtn.addEventListener('click', handleSkip);
        }

        // Review Profile button
        const reviewBtn = document.getElementById('review-profile-btn');
        if (reviewBtn) {
            reviewBtn.addEventListener('click', handleReviewProfile);
        }

        // Transparency disclosure toggle (built-in <details> element)
        const transparencyDetails = document.querySelector('.results-transparency');
        if (transparencyDetails) {
            transparencyDetails.addEventListener('toggle', (e) => {
                console.log(`[Results] Transparency disclosure ${e.target.open ? 'opened' : 'closed'}`);
            });
        }
    }

    // ============================================================================
    // MODULE INITIALIZATION
    // ============================================================================

    /**
     * Initialize Module 5: Results
     */
    function init(appState) {
        console.log('[Results] Initializing Module 5...');

        // Store reference to global state
        state = appState;

        // Check if results data exists
        if (!state.results || !state.results.matchScore) {
            console.error('[Results] No results data available');
            return;
        }

        // Set up event listeners
        setupEventListeners();

        // Load profile data
        loadProfile();

        // Animate match score reveal
        animateScoreCountUp(state.results.matchScore);

        // Update tri-factor breakdown
        updateTriFactorBreakdown();

        // Update radar chart
        updateRadarChart();

        // Update chromosome map
        updateChromosomeMap();

        console.log('[Results] Module 5 initialized with score:', state.results.matchScore);
    }

    // ============================================================================
    // PUBLIC API
    // ============================================================================

    // Register module in global namespace
    window.HarmoniaModules = window.HarmoniaModules || {};
    window.HarmoniaModules.Results = {
        init: init,
        handleSendLike: handleSendLike,
        handleSkip: handleSkip,
        handleReviewProfile: handleReviewProfile
    };

})(window, document);
