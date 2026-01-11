/**
 * Harmonia Chart.js Configuration
 * Pre-configured donut and radar charts for Tri-Factor visualization
 * Requires: Chart.js 4.4.0+
 */

class HarmoniaCharts {
    constructor() {
        // Harmonia color palette
        this.colors = {
            mediterraneanBlue: '#2a4e6c',
            deepBurgundy: '#8b0000',
            goldChampagne: '#d4af37',
            goldDark: '#c5a028',
            parchmentLight: '#f5f0e6',
            parchmentDark: '#e6ddd0',
            textDark: '#2c241b'
        };

        // Default font configuration
        this.defaultFont = {
            family: "'DM Sans', sans-serif",
            size: 12,
            weight: '500'
        };
    }

    /**
     * Create Tri-Factor Donut Chart
     * Shows: Visual 50%, Psychometric 35%, Genetic 10%, Serendipity 5%
     */
    createTriFactorDonut(canvasId, options = {}) {
        const canvas = typeof canvasId === 'string'
            ? document.getElementById(canvasId)
            : canvasId;

        if (!canvas) {
            console.error('Canvas element not found');
            return null;
        }

        const data = options.data || {
            visual: 50,
            psychometric: 35,
            genetic: 10,
            serendipity: 5
        };

        const config = {
            type: 'doughnut',
            data: {
                labels: [
                    `Visual (${data.visual}%)`,
                    `Psychometric (${data.psychometric}%)`,
                    `Genetic (${data.genetic}%)`,
                    `Serendipity (${data.serendipity}%)`
                ],
                datasets: [{
                    data: [data.visual, data.psychometric, data.genetic, data.serendipity],
                    backgroundColor: [
                        this.colors.mediterraneanBlue,
                        this.colors.deepBurgundy,
                        this.colors.goldChampagne,
                        'rgba(255, 255, 255, 0.3)'
                    ],
                    borderColor: [
                        this.colors.mediterraneanBlue,
                        this.colors.deepBurgundy,
                        this.colors.goldChampagne,
                        this.colors.parchmentDark
                    ],
                    borderWidth: 2,
                    hoverOffset: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                aspectRatio: 1,
                plugins: {
                    legend: {
                        display: options.showLegend !== false,
                        position: 'bottom',
                        labels: {
                            font: this.defaultFont,
                            color: this.colors.textDark,
                            padding: 15,
                            usePointStyle: true,
                            pointStyle: 'circle'
                        }
                    },
                    tooltip: {
                        enabled: true,
                        backgroundColor: this.colors.mediterraneanBlue,
                        titleFont: {
                            ...this.defaultFont,
                            size: 14,
                            weight: '600'
                        },
                        bodyFont: this.defaultFont,
                        padding: 12,
                        cornerRadius: 8,
                        displayColors: true
                    }
                },
                cutout: options.cutout || '70%',
                animation: {
                    animateRotate: true,
                    animateScale: true,
                    duration: 1000,
                    easing: 'easeOutQuart'
                }
            }
        };

        return new Chart(canvas, config);
    }

    /**
     * Create Cardinal Drivers Radar Chart
     * 7 axes: Passion, Indulgence, Ambition, Serenity, Conviction, Yearning, Dignity
     */
    createCardinalRadar(canvasId, options = {}) {
        const canvas = typeof canvasId === 'string'
            ? document.getElementById(canvasId)
            : canvasId;

        if (!canvas) {
            console.error('Canvas element not found');
            return null;
        }

        const userScores = options.userScores || [5, 3, 4, 3, 4, 2, 5];
        const matchScores = options.matchScores || [4, 4, 3, 5, 3, 3, 4];

        const config = {
            type: 'radar',
            data: {
                labels: [
                    'Passion',
                    'Indulgence',
                    'Ambition',
                    'Serenity',
                    'Conviction',
                    'Yearning',
                    'Dignity'
                ],
                datasets: [
                    {
                        label: options.userLabel || 'You',
                        data: userScores,
                        backgroundColor: `${this.colors.mediterraneanBlue}33`, // 20% opacity
                        borderColor: this.colors.mediterraneanBlue,
                        borderWidth: 2,
                        pointBackgroundColor: this.colors.mediterraneanBlue,
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2,
                        pointRadius: 4,
                        pointHoverRadius: 6
                    },
                    {
                        label: options.matchLabel || 'Match',
                        data: matchScores,
                        backgroundColor: `${this.colors.deepBurgundy}33`, // 20% opacity
                        borderColor: this.colors.deepBurgundy,
                        borderWidth: 2,
                        pointBackgroundColor: this.colors.deepBurgundy,
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2,
                        pointRadius: 4,
                        pointHoverRadius: 6
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                aspectRatio: 1.2,
                plugins: {
                    legend: {
                        display: options.showLegend !== false,
                        position: 'top',
                        labels: {
                            font: this.defaultFont,
                            color: this.colors.textDark,
                            padding: 15,
                            usePointStyle: true
                        }
                    },
                    tooltip: {
                        enabled: true,
                        backgroundColor: this.colors.mediterraneanBlue,
                        titleFont: {
                            ...this.defaultFont,
                            size: 14,
                            weight: '600'
                        },
                        bodyFont: this.defaultFont,
                        padding: 12,
                        cornerRadius: 8
                    }
                },
                scales: {
                    r: {
                        min: 0,
                        max: options.maxScore || 5,
                        ticks: {
                            stepSize: 1,
                            font: this.defaultFont,
                            color: this.colors.textDark,
                            backdropColor: 'transparent'
                        },
                        grid: {
                            color: this.colors.parchmentDark,
                            lineWidth: 1
                        },
                        angleLines: {
                            color: this.colors.parchmentDark,
                            lineWidth: 1
                        },
                        pointLabels: {
                            font: {
                                ...this.defaultFont,
                                size: 13,
                                weight: '600'
                            },
                            color: this.colors.textDark,
                            padding: 10
                        }
                    }
                },
                animation: {
                    duration: 1200,
                    easing: 'easeOutQuart'
                }
            }
        };

        return new Chart(canvas, config);
    }

    /**
     * Create Compatibility Donut Chart
     * Single value showing overall match percentage
     */
    createCompatibilityDonut(canvasId, options = {}) {
        const canvas = typeof canvasId === 'string'
            ? document.getElementById(canvasId)
            : canvasId;

        if (!canvas) {
            console.error('Canvas element not found');
            return null;
        }

        const compatibility = options.percentage || 87;
        const remaining = 100 - compatibility;

        const config = {
            type: 'doughnut',
            data: {
                labels: ['Compatible', 'Remaining'],
                datasets: [{
                    data: [compatibility, remaining],
                    backgroundColor: [
                        this.colors.goldChampagne,
                        this.colors.parchmentLight
                    ],
                    borderColor: [
                        this.colors.goldDark,
                        this.colors.parchmentDark
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                aspectRatio: 1,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: false
                    }
                },
                cutout: '75%',
                rotation: -90,
                circumference: 360,
                animation: {
                    animateRotate: true,
                    duration: 1500,
                    easing: 'easeInOutQuart'
                }
            },
            plugins: [{
                id: 'centerText',
                afterDraw: (chart) => {
                    const ctx = chart.ctx;
                    const centerX = chart.chartArea.left + (chart.chartArea.right - chart.chartArea.left) / 2;
                    const centerY = chart.chartArea.top + (chart.chartArea.bottom - chart.chartArea.top) / 2;

                    ctx.save();
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';

                    // Percentage
                    ctx.font = `600 2.5rem ${this.defaultFont.family}`;
                    ctx.fillStyle = this.colors.textDark;
                    ctx.fillText(`${compatibility}%`, centerX, centerY - 15);

                    // Label
                    ctx.font = `500 0.875rem ${this.defaultFont.family}`;
                    ctx.fillStyle = this.colors.mediterraneanBlue;
                    ctx.fillText('Compatible', centerX, centerY + 20);

                    ctx.restore();
                }
            }]
        };

        return new Chart(canvas, config);
    }

    /**
     * Destroy chart instance
     */
    destroy(chart) {
        if (chart && typeof chart.destroy === 'function') {
            chart.destroy();
        }
    }
}

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HarmoniaCharts;
}
