# Harmonia Apex Match - Professional Resources & Libraries

This document contains all researched professional templates, libraries, animations, and assets for building the Apex Match preview.

---

## Professional Full-Page Templates

### Free CSS Template Collections
- **[NicePage CSS Templates](https://nicepage.com/css-templates)** - 15,000+ open source templates
- **[Colorlib Free Templates](https://colorlib.com/wp/free-css-website-templates/)** - 67 modern & free CSS website templates 2026, including "WebApp" template perfect for web applications
- **[TemplateMo](https://templatemo.com/)** - 602+ free HTML CSS templates, 100% free download instantly without email/login
- **[Free-CSS.com](https://www.free-css.com/free-css-templates)** - 3,552+ open source, creative commons templates
- **[Webflow Free Templates](https://webflow.com/free-website-templates)** - 93+ free website templates with pre-built responsive layouts
- **[TeleportHQ Static Templates](https://teleporthq.io/static-website-templates)** - Free static website templates with CSS & HTML export
- **[TemplatesJungle](https://templatesjungle.com/free-html-css-templates/)** - 120+ free templates with source code

**Key Features**: Bootstrap 5, responsive designs, mobile-ready, professional styling for web applications

---

## Animation Libraries

### Particle Effects (Gold Dust, Floating Elements)

**Recommended: tsParticles**
- **[tsParticles](https://particles.js.org/)** - Most feature-rich particle library
- 12+ million monthly downloads on npm
- React, Vue.js, Angular, Svelte, jQuery components available
- Highly customizable particles, confetti, and fireworks animations
- **Usage**: Perfect for gold dust dissolve effects, floating particles

**Alternative Options**:
- **[CSS Particle Backgrounds](https://devsnap.me/css-particle-backgrounds)** - 20+ pure CSS particle backgrounds
- **[CSS Script Particle Tag](https://www.cssscript.com/tag/particle/)** - Collection of JavaScript & CSS particle effects
- **[CodePen Pure CSS Particle Animation](https://codepen.io/hf666/pen/WVrpWe)** - Layered animations, pseudo-elements, box-shadow tricks

**Implementation**:
```javascript
// tsParticles for gold dust effect
tsParticles.load("container", {
  particles: {
    color: { value: "#d4af37" }, // Gold Champagne
    move: { enable: true, speed: 2 },
    opacity: { value: 0.5, animation: { enable: true } }
  }
});
```

---

### Liquid Fill Animations (Circle Progress, DNA Seal)

**Top Libraries**:
- **[Wavify](https://www.jqueryscript.net/animation/Smooth-Wave-Liquid-Animation-jQuery-GSAP-SVG.html)** - Smooth wave/liquid animation with jQuery, GSAP, and SVG
- **[Loading.io Liquid Spinner](https://loading.io/spinner/liquid/-liquid-water-fill-alcohol-bottle-cup)** - Build GIF, SVG, APNG, CSS and Lottie preloaders
- **[GitHub: fill-water-animation](https://github.com/coiger/fill-water-animation)** - Fill wavy water in circle with pure CSS code

**Tutorials**:
- **[Smashing Magazine: SVG Fill Animation](https://www.smashingmagazine.com/2019/01/html5-svg-fill-animation-css3-vanilla-javascript/)** - HTML5 SVG circle element with stroke properties
- **[Madras Academy: Liquid Fill Animation](https://www.madrasacademy.com/liquid-fill-animation-with-html-and-css/)** - Dynamic water-like motion inside circular progress
- **[CSS-Tricks: Building a Progress Ring](https://css-tricks.com/building-progress-ring-quickly/)** - stroke-dasharray and stroke-dashoffset techniques

**Implementation**:
```css
/* Circular liquid fill */
.liquid-circle {
  stroke-dasharray: 628; /* 2 * π * radius */
  stroke-dashoffset: 628;
  animation: fill 2s ease-in-out forwards;
}

@keyframes fill {
  to { stroke-dashoffset: 0; }
}
```

---

### Spring Physics Sliders

**Recommended: Motion**
- **[Motion](https://motion.dev)** - Free and open source, 12+ million monthly downloads
- Fastest-growing animation library, supports React, JavaScript, Vue
- Built-in spring physics: `spring({ mass, stiffness, damping })`

**Alternative Libraries**:
- **[react-spring](https://github.com/pmndrs/react-spring)** - Spring-physics based React animation library
- **[Popmotion](https://popmotion.io/)** - Powers Framer Motion, <5kb, supports spring animations
- **[springTo.js](https://matthaeuskrenn.com/springto/)** - Lightweight, single line of code implementation

**Educational**:
- **[Josh W. Comeau: Spring Physics Introduction](https://www.joshwcomeau.com/animation/a-friendly-introduction-to-spring-physics/)** - Hand-rolled spring animation system with mass, stiffness, damping

**Implementation**:
```javascript
import { animate, spring } from "motion"

animate(slider,
  { x: 100 },
  { easing: spring({ stiffness: 300, damping: 20 }) }
)
```

---

### SVG Morphing (Face Mesh, DNA Helix Transitions)

**Top Open Source Libraries**:
- **[Flubber](https://github.com/veltman/flubber)** - Best-guess interpolation for arbitrary shapes, smooth animation
- **[KUTE.js SVG Morph](https://thednp.github.io/kute.js/svgMorph.html)** - Animates SVG path 'd' attribute with performance tools
- **[Animatry](https://animatry.com/)** - Lightweight, morph any SVG path even with different point counts
- **[Snap.svg](http://snapsvg.io/)** - jQuery-like working with SVG assets

**Note**: GSAP has SVG morphing but requires paid license for commercial use

**Implementation**:
```javascript
// Flubber example
import flubber from "flubber"

const interpolator = flubber.interpolate(pathD1, pathD2)
path.setAttribute("d", interpolator(0.5)) // 50% morphed
```

---

### Glassmorphism Effects

**CSS Generators** (Free Tools):
- **[Glass UI Generator](https://ui.glass/generator/)** - Based on Glass UI library, generate CSS and HTML
- **[CSS.glass](https://css.glass/)** - Popular glassmorphism effect generator
- **[Glasscss.com (Liquid Glass)](https://glasscss.com/)** - Professional liquid glass generator with export
- **[10015.io Glassmorphism Generator](https://10015.io/tools/css-glassmorphism-generator)** - Customizable with color selection
- **[Glassmorphism.online](https://glassmorphism.online/)** - Real-time preview, instant CSS export

**Best Practices**:
- Use `backdrop-filter: blur()` with semi-transparent backgrounds
- Use white on dark backgrounds (10-30% opacity)
- Blue-tinted shadows for atmospheric depth (not grey)

**Implementation**:
```css
.glass-panel {
  background: rgba(245, 240, 230, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 10px 15px rgba(42, 78, 108, 0.1);
}
```

---

## Asset Libraries

### DNA Helix SVG Animations

**Free Downloads**:
- **[GitHub: DNA-Helix by edisedis777](https://github.com/edisedis777/DNA-Helix)** - Dynamic, interactive DNA double helix with CreateJS, animated particles
- **[CodePen: DNA Double Helix](https://codepen.io/hugo/pen/nbLzBQ)** - CSS animation example
- **[FreeSVG DNA Helix](https://freesvg.org/hs-dna-helix)** - Public domain SVG (CC0 license)
- **[UXWing DNA Icon](https://uxwing.com/dna-icon/)** - Free SVG/PNG, no attribution required
- **[Vecteezy DNA Helix](https://www.vecteezy.com/free-vector/dna-helix)** - 10,511+ vectors, royalty-free
- **[FreeVectorFinder DNA Helix](http://freevectorfinder.com/free-vectors/dna-helix/)** - 161 files in AI, EPS, SVG formats

---

### Paper Grain Texture Overlays

**SVG Generators** (Recommended):
- **[gggrain (fffuel)](https://www.fffuel.co/gggrain/)** - SVG generator for organic grainy gradients
- **[nnnoise (fffuel)](https://www.fffuel.co/nnnoise/)** - Online SVG noise texture generator

**Free Downloads**:
- **[Vecteezy Paper Texture SVG](https://www.vecteezy.com/free-svg/paper-texture)** - 44,649+ SVGs, royalty-free
- **[Freepik Paper Texture SVG](https://www.freepik.com/free-photos-vectors/paper-texture-svg)** - Free for commercial use
- **[FreeSVG Grainy Textures](https://freesvg.org/grainy-textures)** - Creative Commons public domain

**Tutorials**:
- **[FreeCodeCamp: Grainy CSS Backgrounds](https://www.freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters/)** - feTurbulence filter tutorial
- **[CodePen: Rough Paper Texture](https://codepen.io/Chokcoco/pen/OJWLXPY)** - SVG filters demo

**Implementation** (Inline SVG):
```svg
<svg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'>
  <filter id='noiseFilter'>
    <feTurbulence type='fractalNoise' baseFrequency='2.5' numOctaves='4' stitchTiles='stitch'/>
  </filter>
  <rect width='100%' height='100%' filter='url(#noiseFilter)' opacity='0.03'/>
</svg>
```

---

## Chart Libraries

### Radar Charts (7-Axis Heptagonal for "Sins")

**Top Open Source Options**:
- **[svg-radar-chart](https://github.com/derhuerst/svg-radar-chart)** - No D3 required, 3k minified, FOSS
- **[RadarChartJS (radar-chart-js)](https://github.com/NicoCaldo/radar-chart-js)** - Lightweight vanilla JS, SVG-based with smooth gradients
- **[Chart.js Radar](https://www.chartjs.org/docs/latest/charts/radar.html)** - Part of Chart.js, open source HTML5 charts
- **[react-svg-radar-chart](https://www.npmjs.com/package/react-svg-radar-chart)** - React wrapper for svg-radar-chart

**Features**:
- Customizable axes, colors, scale circles
- SVG output for crisp rendering
- Lightweight and performant

**Implementation**:
```javascript
// svg-radar-chart example
import radarChart from 'svg-radar-chart'

const chart = radarChart({
  captions: { Passion: 5, Ambition: 4, Serenity: 3, Conviction: 4, Yearning: 2, Indulgence: 3, Dignity: 5 },
  chartColors: ['#2a4e6c', '#8b0000'], // Mediterranean, Burgundy
  axes: true,
  scales: 5,
  circles: true
})
```

---

### Donut Charts (Tri-Factor Model Visualization)

**Top Free Libraries**:
- **[Chart.js Doughnut](https://www.chartjs.org/docs/latest/charts/doughnut.html)** - Open source, 60kb, customizable colors via `backgroundColor`
- **[ApexCharts](https://apexcharts.com/)** - MIT licensed, free for commercial, 10+ color palettes
- **[donut-chart-js](https://github.com/Seogeurim/donut-chart-js)** - Simple HTML5 Canvas implementation
- **[Google Charts](https://developers.google.com/chart)** - Free JavaScript chart library

**Implementation**:
```javascript
// Chart.js donut chart
new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Visual (50%)', 'Psychometric (35%)', 'Genetic (10%)', 'Serendipity (5%)'],
    datasets: [{
      data: [50, 35, 10, 5],
      backgroundColor: ['#2a4e6c', '#8b0000', '#d4af37', 'rgba(255, 255, 255, 0.3)']
    }]
  }
});
```

---

## UI Component Patterns

### Floating Label Inputs (Underlined Paper Form Style)

**Tutorials**:
- **[Medium: Floating Label Input CSS Animation](https://medium.com/@srishti.srajput/floating-label-input-css-animation-296f5d45762c)** - Complete HTML/CSS examples
- **[Florin Pop: CSS3 Floating Label](https://www.florin-pop.com/blog/2017/08/css3-floating-label/)** - Classic implementation
- **[Webflow: Input Field Floating Label](https://webflow.com/made-in-webflow/website/input-field-floating-label)** - Material Design style, cloneable
- **[W3bits: Pure CSS Floating Labels](https://w3bits.com/css-floating-labels/)** - No JavaScript required
- **[CodingNepal: Input Label Animation](https://www.codingnepalweb.com/css-animation-input-label/)** - HTML & CSS only

**Bootstrap 5**: Built-in floating labels with `.form-floating`

**Implementation**:
```css
.input-container input:focus ~ label,
.input-container input:not(:placeholder-shown) ~ label {
  transform: translateY(-1.5rem) scale(0.85);
  color: var(--mediterranean-500);
}

.input-container label {
  transition: all 0.2s ease-in-out;
}
```

---

### Segmented Controls / Toggle Switches

**Resources**:
- **[FreeFrontend: JavaScript Toggle Switches](https://freefrontend.com/javascript-toggle-switches/)** - Includes GSAP animated segmented control with 3D tilt
- **[CSS Script: Segmented Control](https://www.cssscript.com/tag/segmented-control/)** - iOS/macOS-style with radio buttons, CSS3
- **[CSS Script: Toggle Radios](https://www.cssscript.com/segmented-control-toggle-radio/)** - Pure CSS, converts radios to toggle button groups
- **[uiCookies: 35 CSS Toggle Templates](https://uicookies.com/css-toggles/)** - Ready-to-use templates
- **[Devsnap: 75+ CSS Toggle Switches](https://devsnap.me/css-toggle-switches/)** - No JavaScript required

**Features**:
- Pure CSS with `:checked` selector
- Cubic-bezier easing for smooth transitions
- Keyboard navigation via radio buttons
- Sliding gold background for active state

**Implementation** (Sliding Gold Background):
```css
.segmented-control {
  position: relative;
  display: flex;
  background: var(--parchment-100);
  border-radius: 999px;
}

.segmented-control::after {
  content: '';
  position: absolute;
  background: var(--champagne-400);
  border-radius: 999px;
  transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.segmented-control input:checked + label {
  color: var(--parchment-900);
}
```

---

## Modern CSS Layout Techniques (2025)

### Full-Page Vertical Centering

**Best Practices (2025)**:
- **[design.dev: CSS Centering Complete Guide](https://design.dev/guides/css-centering/)** - Flexbox, Grid, positioning techniques
- **[MDN: Center an Element](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element)** - Official cookbook
- **[DEV Community: Master CSS Alignment 2025](https://dev.to/satyam_gupta_0d1ff2152dcc/master-css-alignment-complete-guide-to-centering-positioning-elements-2025-3h1l)** - Complete guide

**Modern Flexbox Approach**:
```css
.full-page-center {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
```

**Modern CSS Grid Approach** (Most concise):
```css
.full-page-center {
  display: grid;
  place-items: center;
  min-height: 100vh;
}
```

**2025 Recommendation**: For modern browsers, `place-items: center` with Grid is cleanest. For broader support, Flexbox's `justify-content: center` + `align-items: center` is excellent.

---

### Full-Page Web App Layouts

**Resources**:
- **[Flexbox Full Page Web App Layout](http://geon.github.io/programming/2016/02/24/flexbox-full-page-web-app-layout)** - Classic pattern with header, main, footer
- **[Webflow Flexbox Builder](https://flexbox.webflow.com/)** - Visual CSS flexbox builder
- **[Quackit: Flexbox Templates](https://www.quackit.com/html/templates/css_flexbox_templates.cfm)** - Ready-to-use templates
- **[Tobias Ahlin: Common Flexbox Patterns](https://tobiasahlin.com/blog/common-flexbox-patterns/)** - Example code
- **[CodingChefs: Modern CSS Layouts 2025](https://codingchefs.com/articles/modern-css-layouts-mastering-grid-flexbox-and-subgrid-in-2025)** - Mastering Grid, Flexbox, Subgrid

**2025 Strategy**: Don't choose between Flexbox vs Grid—strategically combine both:
- **CSS Grid**: Overall page structure (two-dimensional control)
- **Flexbox**: Individual components within grid areas (content-aware alignment)

**Full-Page Pattern**:
```css
html, body {
  height: 100%;
}

body {
  display: flex;
  flex-direction: column;
}

main {
  flex: 1; /* Expand to fill available space */
  display: flex;
  align-items: center;
  justify-content: center;
}
```

---

## Implementation Priority

### Immediate Integration (Session 1-2)
1. ✅ CSS Variables (colors, typography, spacing)
2. ✅ Browser reset and normalization
3. ✅ Base typography and paper grain texture
4. ✅ Full-page Flexbox/Grid centering patterns
5. 🔄 Glassmorphism utilities (glass-panel, vellum effect)
6. 🔄 Floating label input animations
7. 🔄 Segmented control/toggle switch

### Medium Priority (Session 3-4)
1. tsParticles integration for gold dust effects
2. Liquid fill animations for biometric seal
3. Spring physics slider (Motion or Popmotion)
4. SVG morphing library (Flubber for face mesh transitions)
5. Chart.js for donut and radar charts

### Future Enhancements
1. DNA helix SVG animation
2. Advanced particle backgrounds
3. Custom SVG filters for paper texture
4. GSAP timeline for 5-second analysis theater

---

## License Notes

All libraries and resources listed are:
- ✅ **Free for commercial use**
- ✅ **Open source** (MIT, BSD, CC0, or similar permissive licenses)
- ✅ **No attribution required** (except where explicitly stated)

**Exceptions**:
- GSAP: Free for most uses, but advanced plugins require commercial license
- Some Freepik/Vecteezy assets may require attribution (check individual licenses)

---

## Additional Resources

### Learning & Tutorials
- **[CSS-Tricks](https://css-tricks.com/)** - Comprehensive CSS guides
- **[Smashing Magazine](https://www.smashingmagazine.com/)** - Web design/development articles
- **[FreeCodeCamp](https://www.freecodecamp.org/)** - Free coding tutorials
- **[MDN Web Docs](https://developer.mozilla.org/)** - Official web documentation

### Code Examples
- **[CodePen](https://codepen.io/)** - Live code examples and demos
- **[JSFiddle](https://jsfiddle.net/)** - Online code editor
- **[StackBlitz](https://stackblitz.com/)** - Instant dev environments

---

**Last Updated**: Session 1 - January 2026
**Maintained By**: Claude Agent for Harmonia Apex Match Project
