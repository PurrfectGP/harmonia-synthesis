# Harmonia Apex Match - Integration Guide

Quick reference for using all the integrated resources created in Session 1.

## 🎯 Quick Start

### View the Complete Demo
```bash
open integrated-demo.html
```

This demonstrates all components working together:
- Floating label inputs with validation
- Segmented controls with spring physics
- Biometric seal with liquid fill animation
- Interactive particle effects
- Chart.js visualizations (Tri-Factor, Cardinal Drivers, Compatibility)

## 📁 Project Structure

```
apex-match-preview/
├── assets/svg/          # SVG assets (DNA helix, icons, textures)
├── css/                 # Stylesheets (variables, reset, base, layout)
├── js/
│   ├── lib/            # Animation libraries (spring, liquid, particles, charts)
│   └── components/     # UI components (inputs, controls, seal)
├── integrated-demo.html # Full demonstration of all components
├── example.html        # Initial layout examples
├── RESOURCES.md        # Research documentation
├── CDN-LINKS.md        # CDN reference guide
└── SESSION-1-COMPLETE.md # Session completion summary
```

## 🛠️ Components Available

### JavaScript Libraries (`js/lib/`)

| Library | Purpose | Size | Dependencies |
|---------|---------|------|--------------|
| `spring-physics.js` | Natural spring-based animations | 194 lines | None |
| `liquid-fill.js` | Circular liquid fill with waves | ~150 lines | None |
| `particles.js` | Gold dust particle system | 176 lines | None |
| `chart-config.js` | Chart.js configuration helpers | 300+ lines | Chart.js |

### UI Components (`js/components/`)

| Component | Purpose | Size | Uses |
|-----------|---------|------|------|
| `floating-input.js` | Material Design floating label input | ~200 lines | None |
| `segmented-control.js` | iOS-style segmented picker | ~200 lines | spring-physics.js |
| `biometric-seal.js` | Circular file upload with progress | ~180 lines | liquid-fill.js, dna-helix.svg |

### SVG Assets (`assets/svg/`)

| Asset | Purpose | Size |
|-------|---------|------|
| `dna-helix.svg` | DNA double helix icon | 60 lines |
| `paper-grain.svg` | Background texture filter | ~30 lines |
| `icons.svg` | 7 Cardinal Driver icons | ~90 lines |

## 💻 Usage Examples

### Floating Label Input
```javascript
const input = new FloatingInput('#container', {
    label: 'Full Name',
    value: 'Felix Patel',
    required: true,
    onChange: (value) => console.log(value)
});
```

### Segmented Control
```javascript
const control = new SegmentedControl('#container', {
    segments: ['Male', 'Female', 'Non-Binary'],
    selected: 0,
    onChange: (index, label) => console.log(label)
});
```

### Biometric Seal
```javascript
const seal = new BiometricSeal('#container', {
    size: 200,
    showProgress: true,
    onUpload: (file, progress) => console.log(file.name, progress)
});
```

### Particle Effects
```javascript
const particles = new HarmoniaParticles('#container', {
    particleCount: 50,
    color: '#d4af37',
    direction: 'up'
});

particles.burst(x, y, 30); // Create burst at position
```

### Charts
```javascript
const charts = new HarmoniaCharts();

// Tri-Factor Donut Chart
const donutChart = charts.createTriFactorDonut('canvasId', {
    data: { visual: 50, psychometric: 35, genetic: 10, serendipity: 5 }
});

// Cardinal Drivers Radar Chart
const radarChart = charts.createCardinalRadar('canvasId', {
    userScores: [5, 3, 4, 3, 4, 2, 5],
    matchScores: [4, 4, 3, 5, 3, 3, 4]
});

// Compatibility Donut with Center Text
const compatChart = charts.createCompatibilityDonut('canvasId', {
    percentage: 87
});
```

## 🎨 Design System

### Color Palette
- **Parchment**: `#fbf9f5`, `#f5f0e6`, `#e6ddd0`, `#2c241b`
- **Mediterranean Blue**: `#2a4e6c`, `#1f3b54`
- **Gold Champagne**: `#d4af37`, `#c5a028`
- **Deep Burgundy**: `#8b0000`

### Typography
- **Display**: Cormorant Garamond (humanist serif)
- **Body**: DM Sans (geometric sans)

## 📊 Tri-Factor Model

The matching algorithm weights:
- **Visual** (50%): Facial analysis, phenotype compatibility
- **Psychometric** (35%): Cardinal Drivers alignment, personality metrics
- **Genetic** (10%): HLA compatibility, immune system diversity
- **Serendipity** (5%): Randomness factor, unexpected connections

## 🎭 Cardinal Drivers

7-axis personality framework:
1. **Passion** - Intensity of emotional engagement
2. **Indulgence** - Openness to sensory experiences
3. **Ambition** - Drive for achievement
4. **Serenity** - Capacity for calm and reflection
5. **Conviction** - Strength of beliefs
6. **Yearning** - Depth of romantic desire
7. **Dignity** - Self-respect and composure

## 📝 All Files Created in Session 1

### CSS Files (4 files)
1. **1-variables.css** - Design tokens, color palette, typography scales
2. **2-reset.css** - Modern CSS reset, browser normalization
3. **3-base.css** - Base styles, typography, buttons, utilities
4. **4-layout.css** - Full-page layouts, grid patterns, responsive

### JavaScript Files (7 files)

**Libraries** (4):
- spring-physics.js - Spring animation engine
- liquid-fill.js - Circular liquid animations
- particles.js - Particle system
- chart-config.js - Chart.js helpers

**Components** (3):
- floating-input.js - Input fields
- segmented-control.js - Segment pickers
- biometric-seal.js - File uploads

### SVG Assets (3 files)
- dna-helix.svg - DNA double helix
- paper-grain.svg - Texture filter
- icons.svg - Cardinal Driver icons

### Documentation (4 files)
- **INTEGRATION-GUIDE.md** - This file
- **SESSION-1-COMPLETE.md** - Session completion summary
- **RESOURCES.md** - Research documentation
- **CDN-LINKS.md** - CDN reference guide

## 🚀 Next Steps

### Session 2: CSS Modules & Animations
- css/5-modules.css - Module-specific styles
- css/6-animations.css - Keyframes and transitions
- css/7-components.css - Component details

### Session 3+: Module Implementations
- Build 5 individual modules
- Analysis theater (5-second animation)
- Complete flow integration

---

**Status**: ✅ Resources Complete | 🚧 Modules In Progress

**View Demo**: `open integrated-demo.html`
