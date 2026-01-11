/**
 * Harmonia Apex Match - Main Application Orchestrator
 *
 * This file handles:
 * - State management (Proxy-based reactivity)
 * - SPA navigation (hash-based routing)
 * - Module initialization and lifecycle
 * - Data persistence (localStorage)
 * - Global event coordination
 *
 * Research Applied:
 * - Proxy-based state management (Modern JS 2026 patterns)
 * - Hash-based SPA routing for simplicity
 * - Module pattern for encapsulation
 * - DOMContentLoaded with readyState check
 * - Accessibility-first event handling
 */

(function(window, document) {
    'use strict';

    // ============================================================================
    // STATE MANAGEMENT (Proxy-based Reactivity)
    // ============================================================================

    /**
     * Creates a reactive state object using Proxy
     * Automatically triggers UI updates when state changes
     */
    function createReactiveState(initialState, onChange) {
        return new Proxy(initialState, {
            set(target, property, value) {
                const oldValue = target[property];
                target[property] = value;

                // Trigger change callback if value actually changed
                if (oldValue !== value && typeof onChange === 'function') {
                    onChange(property, value, oldValue);
                }

                return true;
            }
        });
    }

    // ============================================================================
    // APPLICATION STATE
    // ============================================================================

    const HarmoniaState = createReactiveState({
        // Navigation
        currentModule: 'setup',
        currentStep: 1,

        // User Data - Module 1 (Setup)
        userData: {
            name: '',
            email: '',
            password: '',
            gender: null,
            seeking: null
        },

        // Mandatory Five Answers
        mandatoryFive: {},

        // DNA/Biometric Data
        biometric: {
            uploaded: false,
            fileName: null,
            kitRequested: false,
            waitlisted: false
        },

        // Meta FP Calibration Data - Module 2
        calibration: {
            scores: [],      // Array of {imageId, score (1-5), dwellTimeMs, decisionVelocity}
            currentIndex: 0,
            totalPortraits: 50,
            completed: false
        },

        // Assessment Data - Module 3 (Cardinal Drivers)
        assessment: {
            answers: {},     // Object mapping questionId to choice (A/B)
            currentIndex: 0,
            totalQuestions: 7,
            completed: false
        },

        // Analysis State - Module 4
        analysis: {
            stage: 0,        // 0-4 (stages of analysis theater)
            progress: 0,     // 0-100
            completed: false
        },

        // Results Data - Module 5
        results: {
            matchScore: 0,
            profile: null,
            factors: {
                visual: 0,
                psychometric: 0,
                genetic: 0,
                serendipity: 0
            },
            spark: 'medium', // low, medium, high
            cardinalDrivers: {},
            hlaCompatibility: null
        },

        // Session metadata
        session: {
            startTime: null,
            lastActive: null,
            resumed: false
        }
    }, handleStateChange);

    /**
     * State change handler
     * Triggers UI updates and localStorage persistence
     */
    function handleStateChange(property, newValue, oldValue) {
        console.log(`[State Change] ${property}:`, oldValue, '->', newValue);

        // Persist non-sensitive data to localStorage
        saveState();

        // Trigger module-specific handlers
        if (property === 'currentModule') {
            navigateToModule(newValue);
        }
    }

    // ============================================================================
    // LOCAL STORAGE PERSISTENCE
    // ============================================================================

    /**
     * Save state to localStorage (non-sensitive data only)
     * Security: Never store passwords, biometric data, or PII
     */
    function saveState() {
        try {
            const safeState = {
                currentModule: HarmoniaState.currentModule,
                currentStep: HarmoniaState.currentStep,
                mandatoryFive: HarmoniaState.mandatoryFive,
                calibration: {
                    currentIndex: HarmoniaState.calibration.currentIndex,
                    completed: HarmoniaState.calibration.completed
                },
                assessment: {
                    currentIndex: HarmoniaState.assessment.currentIndex,
                    completed: HarmoniaState.assessment.completed
                },
                session: {
                    lastActive: Date.now()
                }
            };

            localStorage.setItem('harmonia_session', JSON.stringify(safeState));
        } catch (error) {
            console.error('[Storage] Failed to save state:', error);
        }
    }

    /**
     * Load state from localStorage
     */
    function loadState() {
        try {
            const saved = localStorage.getItem('harmonia_session');
            if (saved) {
                const parsed = JSON.parse(saved);

                // Restore non-sensitive state
                Object.assign(HarmoniaState, {
                    currentModule: parsed.currentModule || 'setup',
                    currentStep: parsed.currentStep || 1,
                    mandatoryFive: parsed.mandatoryFive || {},
                    session: {
                        ...HarmoniaState.session,
                        resumed: true,
                        lastActive: parsed.session?.lastActive
                    }
                });

                console.log('[Storage] State restored from localStorage');
                return true;
            }
        } catch (error) {
            console.error('[Storage] Failed to load state:', error);
        }
        return false;
    }

    /**
     * Clear session data (on logout/reset)
     */
    function clearState() {
        localStorage.removeItem('harmonia_session');
        console.log('[Storage] Session cleared');
    }

    // ============================================================================
    // SPA NAVIGATION (Hash-based routing)
    // ============================================================================

    const MODULES = {
        'setup': { step: 1, selector: '#module-setup' },
        'calibration': { step: 2, selector: '#module-calibration' },
        'assessment': { step: 3, selector: '#module-assessment' },
        'analysis': { step: 4, selector: '#module-analysis' },
        'results': { step: 5, selector: '#module-results' }
    };

    /**
     * Navigate to a specific module
     */
    function navigateToModule(moduleName) {
        if (!MODULES[moduleName]) {
            console.error(`[Navigation] Invalid module: ${moduleName}`);
            return;
        }

        const module = MODULES[moduleName];

        // Hide all modules
        Object.values(MODULES).forEach(mod => {
            const el = document.querySelector(mod.selector);
            if (el) {
                el.style.display = 'none';
                el.setAttribute('aria-hidden', 'true');
            }
        });

        // Show target module
        const targetEl = document.querySelector(module.selector);
        if (targetEl) {
            targetEl.style.display = 'block';
            targetEl.setAttribute('aria-hidden', 'false');

            // Update state
            HarmoniaState.currentStep = module.step;

            // Update URL hash (for back button support)
            window.location.hash = moduleName;

            // Scroll to top
            window.scrollTo(0, 0);

            // Announce to screen readers
            announceNavigation(moduleName);

            // Initialize module if needed
            initializeModule(moduleName);

            console.log(`[Navigation] Navigated to: ${moduleName}`);
        }
    }

    /**
     * Handle hash change events (back/forward navigation)
     */
    function handleHashChange() {
        const hash = window.location.hash.slice(1); // Remove #
        if (hash && MODULES[hash]) {
            HarmoniaState.currentModule = hash;
        } else if (!hash) {
            // No hash, go to first module
            HarmoniaState.currentModule = 'setup';
        }
    }

    /**
     * Announce navigation to screen readers
     */
    function announceNavigation(moduleName) {
        const announcer = document.getElementById('route-announcer');
        if (announcer) {
            const moduleNames = {
                'setup': 'Setup and Biometric Ingestion',
                'calibration': 'Visual Calibration',
                'assessment': 'Psychometric Assessment',
                'analysis': 'Analysis in Progress',
                'results': 'Match Results'
            };
            announcer.textContent = `Navigated to ${moduleNames[moduleName]}`;
        }
    }

    // ============================================================================
    // MODULE INITIALIZATION
    // ============================================================================

    const initializedModules = new Set();

    /**
     * Initialize a module's JavaScript
     */
    function initializeModule(moduleName) {
        // Prevent double initialization
        if (initializedModules.has(moduleName)) {
            return;
        }

        console.log(`[Init] Initializing module: ${moduleName}`);

        switch(moduleName) {
            case 'setup':
                if (window.HarmoniaModules && window.HarmoniaModules.Setup) {
                    window.HarmoniaModules.Setup.init(HarmoniaState);
                }
                break;
            case 'calibration':
                if (window.HarmoniaModules && window.HarmoniaModules.Calibration) {
                    window.HarmoniaModules.Calibration.init(HarmoniaState);
                }
                break;
            case 'assessment':
                if (window.HarmoniaModules && window.HarmoniaModules.Assessment) {
                    window.HarmoniaModules.Assessment.init(HarmoniaState);
                }
                break;
            case 'analysis':
                if (window.HarmoniaModules && window.HarmoniaModules.Analysis) {
                    window.HarmoniaModules.Analysis.init(HarmoniaState);
                }
                break;
            case 'results':
                if (window.HarmoniaModules && window.HarmoniaModules.Results) {
                    window.HarmoniaModules.Results.init(HarmoniaState);
                }
                break;
        }

        initializedModules.add(moduleName);
    }

    // ============================================================================
    // GLOBAL EVENT HANDLERS
    // ============================================================================

    /**
     * Set up global event delegation
     */
    function setupEventDelegation() {
        // Navigation button clicks
        document.addEventListener('click', function(e) {
            const target = e.target;

            // Handle navigation via data-navigate attribute
            if (target.hasAttribute('data-navigate')) {
                e.preventDefault();
                const moduleName = target.getAttribute('data-navigate');
                HarmoniaState.currentModule = moduleName;
            }

            // Handle module "Continue" buttons
            if (target.classList.contains('module-continue')) {
                e.preventDefault();
                const currentModule = HarmoniaState.currentModule;
                const nextModule = getNextModule(currentModule);
                if (nextModule) {
                    HarmoniaState.currentModule = nextModule;
                }
            }
        });

        // Keyboard navigation (for accessibility)
        document.addEventListener('keydown', function(e) {
            // Alt+Left: Previous module
            if (e.altKey && e.key === 'ArrowLeft') {
                e.preventDefault();
                const prevModule = getPreviousModule(HarmoniaState.currentModule);
                if (prevModule) {
                    HarmoniaState.currentModule = prevModule;
                }
            }

            // Alt+Right: Next module
            if (e.altKey && e.key === 'ArrowRight') {
                e.preventDefault();
                const nextModule = getNextModule(HarmoniaState.currentModule);
                if (nextModule) {
                    HarmoniaState.currentModule = nextModule;
                }
            }
        });

        // Warn before page unload if data exists
        window.addEventListener('beforeunload', function(e) {
            if (HarmoniaState.calibration.scores.length > 0 ||
                Object.keys(HarmoniaState.mandatoryFive).length > 0) {
                e.preventDefault();
                e.returnValue = '';
                return '';
            }
        });

        // Handle browser back/forward
        window.addEventListener('hashchange', handleHashChange);

        // Visibility change (pause/resume)
        document.addEventListener('visibilitychange', function() {
            if (document.hidden) {
                HarmoniaState.session.lastActive = Date.now();
                saveState();
            }
        });
    }

    /**
     * Get next module in sequence
     */
    function getNextModule(currentModule) {
        const sequence = ['setup', 'calibration', 'assessment', 'analysis', 'results'];
        const currentIndex = sequence.indexOf(currentModule);
        return sequence[currentIndex + 1] || null;
    }

    /**
     * Get previous module in sequence
     */
    function getPreviousModule(currentModule) {
        const sequence = ['setup', 'calibration', 'assessment', 'analysis', 'results'];
        const currentIndex = sequence.indexOf(currentModule);
        return currentIndex > 0 ? sequence[currentIndex - 1] : null;
    }

    // ============================================================================
    // APPLICATION INITIALIZATION
    // ============================================================================

    /**
     * Initialize the Harmonia application
     */
    function init() {
        console.log('[Harmonia] Initializing application...');

        // Set session start time
        HarmoniaState.session.startTime = Date.now();

        // Try to restore previous session
        const restored = loadState();
        if (restored) {
            console.log('[Harmonia] Session restored');
        }

        // Set up global event delegation
        setupEventDelegation();

        // Handle initial hash or navigate to first module
        handleHashChange();

        // If no hash, navigate to setup
        if (!window.location.hash) {
            HarmoniaState.currentModule = 'setup';
        }

        console.log('[Harmonia] Application initialized');
    }

    // ============================================================================
    // LIFECYCLE MANAGEMENT (DOMContentLoaded Pattern)
    // ============================================================================

    /**
     * Start application when DOM is ready
     * Pattern handles both early and late script loading
     */
    function start() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            // DOM already loaded
            init();
        }
    }

    // ============================================================================
    // PUBLIC API
    // ============================================================================

    // Expose global Harmonia namespace
    window.Harmonia = {
        state: HarmoniaState,
        navigate: navigateToModule,
        saveState: saveState,
        clearState: clearState,
        version: '1.0.0'
    };

    // Expose empty modules namespace (modules will register themselves)
    window.HarmoniaModules = window.HarmoniaModules || {};

    // Auto-start
    start();

})(window, document);
