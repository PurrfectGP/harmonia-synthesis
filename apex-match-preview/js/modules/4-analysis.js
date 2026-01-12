/**
 * Harmonia Apex Match - Module 4: Analysis (The Labor Illusion Theater)
 *
 * Spec Reference: README.md Section 6 - "The Labor Illusion Theater"
 * HTML Template: modules/4-analysis.html
 *
 * This module handles:
 * - 5-second staged analysis sequence
 * - 4 visualization layers (DNA, Visual, Psychometric, Synthesis)
 * - Progress ring animation
 * - Match score calculation
 * - Labor illusion pattern (perceived computational effort)
 *
 * Research Applied:
 * - requestAnimationFrame for smooth animations
 * - Animation sequencing and choreography
 * - SVG circle progress indicator
 * - Time-based animation (not frame-based)
 * - Reduced motion accessibility
 */

(function(window, document) {
    'use strict';

    // ============================================================================
    // MODULE STATE
    // ============================================================================

    let state = null; // Global app state (injected on init)
    let animationFrameId = null;

    // Analysis stages configuration
    const ANALYSIS_STAGES = [
        {
            stage: 1,
            layer: 'layer-visual',
            duration: 1250, // milliseconds
            statusText: 'Analyzing visual patterns...',
            animation: 'dna-rotate-3d'
        },
        {
            stage: 2,
            layer: 'layer-psychometric',
            duration: 1250,
            statusText: 'Computing psychometric alignment...',
            animation: 'radar-scan'
        },
        {
            stage: 3,
            layer: 'layer-genetic',
            duration: 1250,
            statusText: 'Processing genetic compatibility...',
            animation: 'chromosome-pulse'
        },
        {
            stage: 4,
            layer: 'layer-synthesis',
            duration: 1250,
            statusText: 'Synthesizing final results...',
            animation: 'particle-convergence'
        }
    ];

    const TOTAL_DURATION = ANALYSIS_STAGES.reduce((sum, stage) => sum + stage.duration, 0); // 5 seconds

    // ============================================================================
    // PROGRESS RING
    // ============================================================================

    /**
     * Update circular progress ring
     */
    function updateProgressRing(percentage) {
        const progressRingFill = document.getElementById('progress-ring-fill');
        const progressPercentage = document.getElementById('progress-percentage');
        const progressBar = document.querySelector('.analysis-progress');

        if (!progressRingFill) return;

        // Calculate stroke-dashoffset for SVG circle
        const circumference = 314.159; // 2 * PI * radius (50)
        const offset = circumference - (percentage / 100) * circumference;

        progressRingFill.style.strokeDashoffset = offset;

        // Update percentage text
        if (progressPercentage) {
            progressPercentage.textContent = `${Math.round(percentage)}%`;
        }

        // Update ARIA
        if (progressBar) {
            progressBar.setAttribute('aria-valuenow', percentage);
        }
    }

    // ============================================================================
    // LAYER MANAGEMENT
    // ============================================================================

    /**
     * Activate a specific analysis layer
     */
    function activateLayer(layerId, statusMessage) {
        // Hide all layers
        document.querySelectorAll('.analysis-layer').forEach(layer => {
            layer.style.opacity = '0';
            layer.style.transform = 'scale(0.8)';
            layer.setAttribute('aria-hidden', 'true');
        });

        // Show active layer
        const activeLayer = document.getElementById(layerId);
        if (activeLayer) {
            requestAnimationFrame(() => {
                activeLayer.style.transition = 'all 0.5s cubic-bezier(0.4, 0.0, 0.2, 1)';
                activeLayer.style.opacity = '1';
                activeLayer.style.transform = 'scale(1)';
                activeLayer.setAttribute('aria-hidden', 'false');

                // Trigger layer-specific animation
                const animationClass = activeLayer.dataset.layer;
                activeLayer.classList.add(`animating-${animationClass}`);
            });
        }

        // Update status text
        const statusEl = document.getElementById('analysis-status');
        if (statusEl) {
            statusEl.textContent = statusMessage;
        }

        console.log(`[Analysis] Layer activated: ${layerId}`);
    }

    // ============================================================================
    // ANIMATION ORCHESTRATION
    // ============================================================================

    /**
     * Run the 5-second staged analysis sequence
     */
    function runAnalysisSequence() {
        let startTime = null;
        let currentStageIndex = 0;

        function animate(timestamp) {
            if (!startTime) startTime = timestamp;
            const elapsed = timestamp - startTime;

            // Calculate overall progress
            const overallProgress = Math.min((elapsed / TOTAL_DURATION) * 100, 100);
            updateProgressRing(overallProgress);

            // Determine which stage we should be in
            let cumulativeTime = 0;
            for (let i = 0; i < ANALYSIS_STAGES.length; i++) {
                const stage = ANALYSIS_STAGES[i];
                cumulativeTime += stage.duration;

                if (elapsed < cumulativeTime) {
                    // We're in this stage
                    if (i !== currentStageIndex) {
                        currentStageIndex = i;
                        state.analysis.stage = stage.stage;
                        activateLayer(stage.layer, stage.statusText);
                    }
                    break;
                }
            }

            // Continue animation if not complete
            if (elapsed < TOTAL_DURATION) {
                animationFrameId = requestAnimationFrame(animate);
            } else {
                // Analysis complete
                completeAnalysis();
            }
        }

        // Start animation loop
        animationFrameId = requestAnimationFrame(animate);

        console.log('[Analysis] Analysis sequence started');
    }

    // ============================================================================
    // RESULT CALCULATION
    // ============================================================================

    /**
     * Calculate match results from collected data
     * This is a mock implementation - production would use ML model
     */
    function calculateMatchResults() {
        // Calculate Visual score (50% weight)
        const visualScore = calculateVisualScore();

        // Calculate Psychometric score (35% weight)
        const psychometricScore = calculatePsychometricScore();

        // Calculate Genetic score (10% weight)
        const geneticScore = calculateGeneticScore();

        // Calculate Serendipity factor (5% weight)
        const serendipityScore = Math.random() * 30 + 70; // Random 70-100

        // Weighted total
        const totalScore = Math.round(
            (visualScore * 0.50) +
            (psychometricScore * 0.35) +
            (geneticScore * 0.10) +
            (serendipityScore * 0.05)
        );

        // Generate mock profile data
        const profile = generateMockProfile();

        return {
            matchScore: totalScore,
            profile: profile,
            factors: {
                visual: Math.round(visualScore),
                psychometric: Math.round(psychometricScore),
                genetic: Math.round(geneticScore),
                serendipity: Math.round(serendipityScore)
            },
            spark: totalScore >= 85 ? 'high' : totalScore >= 70 ? 'medium' : 'low',
            cardinalDrivers: calculateCardinalDriverMatch(),
            hlaCompatibility: {
                overall: Math.round(geneticScore),
                loci: [
                    { name: 'HLA-A', compatibility: Math.round(geneticScore + Math.random() * 10 - 5) },
                    { name: 'HLA-B', compatibility: Math.round(geneticScore + Math.random() * 10 - 5) },
                    { name: 'HLA-C', compatibility: Math.round(geneticScore + Math.random() * 10 - 5) }
                ]
            }
        };
    }

    /**
     * Calculate visual preference score
     */
    function calculateVisualScore() {
        if (!state.calibration.scores || state.calibration.scores.length === 0) {
            return 75; // Default if no data
        }

        const scores = state.calibration.scores.filter(s => !s.skipped);
        const avgRating = scores.reduce((sum, s) => sum + s.rating, 0) / scores.length;

        // Convert 1-5 scale to 0-100
        // Higher average rating = higher visual score
        return (avgRating / 5) * 100;
    }

    /**
     * Calculate psychometric alignment score
     */
    function calculatePsychometricScore() {
        if (!state.assessment.answers || Object.keys(state.assessment.answers).length === 0) {
            return 75; // Default if no data
        }

        // Mock calculation based on answer patterns
        // In production, this would compare to match's profile
        const answersCount = Object.keys(state.assessment.answers).length;
        const baseScore = 70 + (answersCount * 2); // 70-84 range

        return baseScore;
    }

    /**
     * Calculate genetic compatibility score
     */
    function calculateGeneticScore() {
        if (!state.biometric.uploaded && !state.biometric.kitRequested) {
            return 0; // No genetic data
        }

        // Mock HLA compatibility score
        // In production, this would use actual HLA allele comparison
        return Math.round(Math.random() * 25 + 70); // 70-95 range
    }

    /**
     * Calculate Cardinal Driver overlap
     */
    function calculateCardinalDriverMatch() {
        // Mock data - in production would compare user vs match profiles
        return {
            passion: { you: 80, match: 85 },
            indulgence: { you: 65, match: 70 },
            ambition: { you: 90, match: 85 },
            serenity: { you: 60, match: 55 },
            conviction: { you: 75, match: 80 },
            yearning: { you: 70, match: 75 },
            dignity: { you: 85, match: 90 }
        };
    }

    /**
     * Generate mock match profile
     */
    function generateMockProfile() {
        const names = ['Alexandra', 'Sophia', 'Isabella', 'Emma', 'Olivia', 'Ava', 'Charlotte', 'Amelia'];
        const locations = ['San Francisco, CA', 'New York, NY', 'Los Angeles, CA', 'Seattle, WA', 'Portland, OR'];
        const bios = [
            'Architect by day, painter by night. Passionate about sustainable design and finding beauty in unexpected places.',
            'Neuroscience researcher with a love for classical music and long hikes. Believes in the power of curiosity.',
            'Entrepreneur building ethical tech. Avid reader, amateur chef, and believer in meaningful conversations.',
            'Environmental scientist turned photographer. Documenting climate stories and chasing golden hour light.',
            'Philosophy professor who moonlights as a jazz pianist. Forever searching for the perfect espresso.'
        ];

        return {
            id: `user_${Math.random().toString(36).substring(7)}`,
            name: names[Math.floor(Math.random() * names.length)],
            age: Math.floor(Math.random() * 10) + 25, // 25-34
            location: locations[Math.floor(Math.random() * locations.length)],
            portraitUrl: 'https://via.placeholder.com/400x600/e6ddd0/2a4e6c?text=Match+Profile',
            bio: bios[Math.floor(Math.random() * bios.length)]
        };
    }

    // ============================================================================
    // COMPLETION
    // ============================================================================

    /**
     * Complete analysis and prepare results
     */
    function completeAnalysis() {
        console.log('[Analysis] Analysis complete!');

        // Calculate final results
        const results = calculateMatchResults();

        // Store in state
        state.results = results;
        state.analysis.completed = true;
        state.analysis.progress = 100;

        console.log('[Analysis] Match Results:', results);

        // Update UI to show completion
        const statusEl = document.getElementById('analysis-status');
        if (statusEl) {
            statusEl.textContent = 'Analysis complete. Preparing your results...';
        }

        // Navigate to results after brief delay
        setTimeout(() => {
            state.currentModule = 'results';
        }, 1000);
    }

    // ============================================================================
    // AMBIENT EFFECTS
    // ============================================================================

    /**
     * Create ambient floating particles in background
     */
    function createAmbientParticles() {
        const container = document.querySelector('.analysis-ambient-particles');
        if (!container) return;

        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.className = 'ambient-particle';
            particle.style.left = `${Math.random() * 100}%`;
            particle.style.top = `${Math.random() * 100}%`;
            particle.style.animationDelay = `${Math.random() * 5}s`;
            particle.style.animationDuration = `${5 + Math.random() * 5}s`;
            container.appendChild(particle);
        }

        console.log('[Analysis] Ambient particles created');
    }

    // ============================================================================
    // MODULE INITIALIZATION
    // ============================================================================

    /**
     * Initialize Module 4: Analysis
     */
    function init(appState) {
        console.log('[Analysis] Initializing Module 4...');

        // Store reference to global state
        state = appState;

        // Initialize state
        state.analysis.stage = 0;
        state.analysis.progress = 0;

        // Create ambient effects
        createAmbientParticles();

        // Start analysis sequence after brief delay (for dramatic effect)
        setTimeout(() => {
            runAnalysisSequence();
        }, 500);

        console.log('[Analysis] Module 4 initialized');
    }

    /**
     * Cleanup function (called when leaving module)
     */
    function cleanup() {
        // Cancel any running animation
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
            animationFrameId = null;
        }

        console.log('[Analysis] Module cleaned up');
    }

    // ============================================================================
    // PUBLIC API
    // ============================================================================

    // Register module in global namespace
    window.HarmoniaModules = window.HarmoniaModules || {};
    window.HarmoniaModules.Analysis = {
        init: init,
        cleanup: cleanup,
        calculateMatchResults: calculateMatchResults
    };

})(window, document);
