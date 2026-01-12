/**
 * Harmonia Custom Easing Functions Library
 * Sophisticated cubic-bezier curves for luxury brand animations
 * Based on research: easings.net, Josh Collinsworth blog, MDN documentation
 *
 * Sources:
 * - https://easings.net/
 * - https://joshcollinsworth.com/blog/easing-curves
 * - https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function
 */

const HarmoniaEasing = {
    /**
     * SOPHISTICATED ENTRANCES
     * Smooth, elegant entry animations for luxury feel
     */

    // Gentle, refined entrance (like a curtain opening)
    softEntry: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',

    // Confident entrance (establishes presence without jarring)
    refinedEntry: 'cubic-bezier(0.33, 0.0, 0.2, 1)',

    // Luxurious slow start (premium feel, no rush)
    luxuryEntry: 'cubic-bezier(0.4, 0.0, 0.2, 1)',

    /**
     * SOPHISTICATED EXITS
     * Graceful departures that maintain elegance
     */

    // Gentle fade away (like ink drying)
    softExit: 'cubic-bezier(0.55, 0.055, 0.675, 0.19)',

    // Confident exit (decisive but smooth)
    refinedExit: 'cubic-bezier(0.8, 0.0, 0.67, 1)',

    // Luxurious slow end (lingers with intention)
    luxuryExit: 'cubic-bezier(0.6, 0.04, 0.98, 0.335)',

    /**
     * SOPHISTICATED IN-OUT
     * Balanced, professional transitions
     */

    // Classic ease (most versatile, professional)
    classic: 'cubic-bezier(0.4, 0.0, 0.2, 1)',

    // Smooth luxury (for high-end brand feel)
    luxury: 'cubic-bezier(0.645, 0.045, 0.355, 1)',

    // Refined balance (subtle but noticeable)
    refined: 'cubic-bezier(0.42, 0.0, 0.58, 1.0)',

    /**
     * ORGANIC & NATURAL
     * Physics-based, realistic motion
     */

    // Spring-like (natural bounce, not cartoonish)
    spring: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)',

    // Gentle overshoot (subtle anticipation)
    anticipation: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',

    // Gravity (falling motion)
    gravity: 'cubic-bezier(0.55, 0.085, 0.68, 0.53)',

    /**
     * GOLD THEME SPECIFIC
     * Special curves for gold/champagne accents
     */

    // Gold shimmer (for glow effects)
    goldShimmer: 'cubic-bezier(0.25, 0.8, 0.25, 1)',

    // Gold flow (liquid gold movement)
    goldFlow: 'cubic-bezier(0.23, 1, 0.32, 1)',

    // Champagne bubble (floating upward)
    champagneBubble: 'cubic-bezier(0.34, 1.56, 0.64, 1)',

    /**
     * INK & PAPER THEME
     * Animations that feel tactile and handwritten
     */

    // Ink spread (expanding from center)
    inkSpread: 'cubic-bezier(0.19, 1, 0.22, 1)',

    // Pen stroke (confident, deliberate)
    penStroke: 'cubic-bezier(0.65, 0, 0.35, 1)',

    // Paper fold (crisp, mechanical)
    paperFold: 'cubic-bezier(0.86, 0, 0.07, 1)',

    /**
     * DNA & SCIENCE THEME
     * Precision animations for genetic/scientific elements
     */

    // DNA rotation (continuous, organic spiral)
    dnaRotation: 'cubic-bezier(0.4, 0.0, 0.6, 1)',

    // Helix pulse (breathing, living)
    helixPulse: 'cubic-bezier(0.45, 0.05, 0.55, 0.95)',

    // Scientific precision (exact, clinical)
    scientificPrecision: 'cubic-bezier(0.5, 0.0, 0.5, 1)',

    /**
     * RADAR & SCANNING
     * Rotating, sweeping motions
     */

    // Radar sweep (continuous rotation)
    radarSweep: 'linear',

    // Scanner pulse (accelerate then decelerate)
    scannerPulse: 'cubic-bezier(0.42, 0.0, 0.58, 1.0)',

    /**
     * CARD & PAGE TRANSITIONS
     * Module navigation and card effects
     */

    // Card dissolve (particles flying away)
    cardDissolve: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',

    // Page turn (book-like transition)
    pageTurn: 'cubic-bezier(0.645, 0.045, 0.355, 1.0)',

    // Module fade (cross-fade between modules)
    moduleFade: 'cubic-bezier(0.4, 0.0, 0.2, 1)',

    /**
     * LABOR ILLUSION
     * Loading and processing animations
     */

    // Processing step (deliberate, shows work)
    processingStep: 'cubic-bezier(0.4, 0.0, 0.2, 1)',

    // Sequential load (one after another)
    sequentialLoad: 'cubic-bezier(0.5, 0, 0.5, 1)',

    // Progress fill (smooth, consistent)
    progressFill: 'cubic-bezier(0.65, 0, 0.35, 1)',

    /**
     * LIQUID & WAVE
     * Fluid animations for liquid fill effects
     */

    // Wave motion (undulating, organic)
    wave: 'cubic-bezier(0.36, 0, 0.66, -0.56)',

    // Liquid fill (rising smoothly)
    liquidFill: 'cubic-bezier(0.23, 1, 0.32, 1)',

    // Ink flow (vertical climb, elegant)
    inkFlow: 'cubic-bezier(0.4, 0.0, 0.2, 1)',
};

/**
 * Helper Functions
 */

// Apply easing to an element's style
function applyEasing(element, property, easing, duration = '0.3s') {
    if (typeof element === 'string') {
        element = document.querySelector(element);
    }

    if (element) {
        element.style.transition = `${property} ${duration} ${easing}`;
    }
}

// Get CSS string for transition
function getTransition(property, duration = '0.3s', easing = HarmoniaEasing.classic) {
    return `${property} ${duration} ${easing}`;
}

// Get CSS string for animation
function getAnimation(name, duration = '1s', easing = HarmoniaEasing.classic, iterations = 1) {
    return `${name} ${duration} ${easing} ${iterations === 'infinite' ? 'infinite' : iterations}`;
}

/**
 * Recommended Pairings
 * Combinations that work well together based on UX research
 */

const HarmoniaEasingPresets = {
    // For button clicks
    buttonClick: {
        property: 'all',
        duration: '0.2s',
        easing: HarmoniaEasing.refined
    },

    // For modal/dialog appearances
    modalOpen: {
        property: 'all',
        duration: '0.3s',
        easing: HarmoniaEasing.softEntry
    },

    // For floating label inputs
    floatingLabel: {
        property: 'all',
        duration: '0.3s',
        easing: HarmoniaEasing.anticipation
    },

    // For segmented control sliding
    segmentedSlide: {
        property: 'transform',
        duration: '0.4s',
        easing: HarmoniaEasing.anticipation
    },

    // For card stack dissolve
    cardDissolveAnim: {
        property: 'all',
        duration: '0.6s',
        easing: HarmoniaEasing.cardDissolve
    },

    // For page/module transitions
    pageTransition: {
        property: 'opacity, transform',
        duration: '0.5s',
        easing: HarmoniaEasing.moduleFade
    },

    // For gold glow effects
    goldGlow: {
        property: 'box-shadow, opacity',
        duration: '0.8s',
        easing: HarmoniaEasing.goldShimmer
    },

    // For DNA rotation
    dnaRotate: {
        property: 'transform',
        duration: '3s',
        easing: HarmoniaEasing.dnaRotation
    },

    // For liquid fill progress
    liquidProgress: {
        property: 'height, transform',
        duration: '1.5s',
        easing: HarmoniaEasing.liquidFill
    },

    // For radar scanning
    radarScan: {
        property: 'transform',
        duration: '4s',
        easing: HarmoniaEasing.radarSweep
    }
};

// Export for both Node.js and browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { HarmoniaEasing, HarmoniaEasingPresets, applyEasing, getTransition, getAnimation };
} else {
    // Browser global exports
    window.HarmoniaEasing = HarmoniaEasing;
    window.HarmoniaEasingPresets = HarmoniaEasingPresets;
    window.applyEasing = applyEasing;
    window.getTransition = getTransition;
    window.getAnimation = getAnimation;
}
