# CDN Links & Library Integration

Quick reference for adding animation libraries and resources to your HTML.

---

## Core Animation Libraries

### tsParticles (Particle Effects - Gold Dust, Floating Elements)
```html
<!-- tsParticles Core -->
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/engine@3/tsparticles.engine.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/basic@3/tsparticles.basic.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/move-base@3/tsparticles.move.base.min.js"></script>

<!-- Usage -->
<div id="particles-container"></div>
<script>
tsParticles.load("particles-container", {
  particles: {
    number: { value: 80 },
    color: { value: "#d4af37" }, // Gold Champagne
    opacity: { value: 0.5 },
    size: { value: 3 },
    move: { enable: true, speed: 2 }
  }
});
</script>
```

---

### Motion (Spring Physics Animations)
```html
<!-- Motion One CDN -->
<script src="https://cdn.jsdelivr.net/npm/motion@11.2.0/dist/motion.js"></script>

<!-- Usage -->
<script>
const { animate, spring } = Motion;

animate(
  document.querySelector('.slider-thumb'),
  { x: 100 },
  { easing: spring({ stiffness: 300, damping: 20 }) }
);
</script>
```

---

### Chart.js (Donut & Radar Charts)
```html
<!-- Chart.js CDN -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<!-- Donut Chart Example -->
<canvas id="donutChart"></canvas>
<script>
new Chart(document.getElementById('donutChart'), {
  type: 'doughnut',
  data: {
    labels: ['Visual (50%)', 'Psychometric (35%)', 'Genetic (10%)', 'Serendipity (5%)'],
    datasets: [{
      data: [50, 35, 10, 5],
      backgroundColor: ['#2a4e6c', '#8b0000', '#d4af37', 'rgba(255, 255, 255, 0.3)']
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: { enabled: true }
    },
    cutout: '70%' // Donut hole size
  }
});
</script>

<!-- Radar Chart Example -->
<canvas id="radarChart"></canvas>
<script>
new Chart(document.getElementById('radarChart'), {
  type: 'radar',
  data: {
    labels: ['Passion', 'Indulgence', 'Ambition', 'Serenity', 'Conviction', 'Yearning', 'Dignity'],
    datasets: [{
      label: 'You',
      data: [5, 3, 4, 3, 4, 2, 5],
      backgroundColor: 'rgba(42, 78, 108, 0.2)',
      borderColor: '#2a4e6c',
      borderWidth: 2
    }, {
      label: 'Match',
      data: [4, 4, 3, 5, 3, 3, 4],
      backgroundColor: 'rgba(139, 0, 0, 0.2)',
      borderColor: '#8b0000',
      borderWidth: 2
    }]
  },
  options: {
    scales: {
      r: {
        min: 0,
        max: 5,
        ticks: { stepSize: 1 }
      }
    }
  }
});
</script>
```

---

### GSAP (Advanced SVG Morphing & Timelines)
```html
<!-- GSAP Core (Free) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

<!-- GSAP ScrollTrigger (Free) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>

<!-- Usage - 5-Second Analysis Theater -->
<script>
gsap.timeline()
  .to('.dna-helix', { rotation: 360, duration: 1.5, ease: 'power2.inOut' })
  .to('.face-mesh', { morphSVG: '.target-shape', duration: 1.5 }, 1.5)
  .to('.radar-chart', { scale: 1.2, rotation: 180, duration: 1.5 }, 3)
  .to('.synthesis-point', { scale: 0, duration: 0.5, onComplete: showResults }, 4.5);
</script>
```

**Note**: MorphSVG plugin requires Club GreenSock membership for commercial use.
**Free Alternative**: Use [Flubber](#flubber-svg-morphing-free) below.

---

### Flubber (SVG Morphing - Free)
```html
<!-- Flubber CDN -->
<script src="https://unpkg.com/flubber@0.4.2"></script>

<!-- Usage -->
<svg viewBox="0 0 400 400">
  <path id="morphPath" d="..." fill="#d4af37"></path>
</svg>

<script>
const path1 = "M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z";
const path2 = "M 50,50 m -40,0 a 40,40 0 1,0 80,0 a 40,40 0 1,0 -80,0";

const interpolator = flubber.interpolate(path1, path2, {maxSegmentLength: 2});

function animate(t) {
  document.getElementById('morphPath').setAttribute('d', interpolator(t));
  if (t < 1) requestAnimationFrame(() => animate(t + 0.01));
}

animate(0);
</script>
```

---

### Anime.js (Lightweight Alternative to GSAP)
```html
<!-- Anime.js CDN (MIT License, Free) -->
<script src="https://cdn.jsdelivr.net/npm/animejs@3.2.2/lib/anime.min.js"></script>

<!-- Usage - Gold Particle Dissolve -->
<script>
anime({
  targets: '.gold-particle',
  translateY: [-100, 0],
  opacity: [0, 1, 0],
  scale: [0.5, 1.2, 0],
  duration: 2000,
  delay: anime.stagger(100), // Stagger by 100ms
  easing: 'easeOutExpo'
});
</script>
```

---

## Utility Libraries

### Vivus.js (SVG Line Drawing Animation)
```html
<!-- Vivus.js CDN -->
<script src="https://cdn.jsdelivr.net/npm/vivus@0.4.6/dist/vivus.min.js"></script>

<!-- Usage - DNA Helix Drawing Effect -->
<svg id="dna-helix">
  <path stroke="#d4af37" fill="none" d="..."></path>
</svg>

<script>
new Vivus('dna-helix', {
  type: 'delayed',
  duration: 200,
  animTimingFunction: Vivus.EASE
});
</script>
```

---

### Lottie (After Effects Animations)
```html
<!-- Lottie Web CDN -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>

<!-- Usage -->
<div id="lottie-animation"></div>

<script>
lottie.loadAnimation({
  container: document.getElementById('lottie-animation'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'animations/dna-helix.json' // After Effects export
});
</script>
```

---

## CSS-Only Solutions (No CDN Required)

### Paper Grain Texture (Inline SVG)
```html
<!-- Add to body or main container -->
<style>
body {
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='2.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.03'/%3E%3C/svg%3E");
}
</style>
```

---

### Glassmorphism (Pure CSS)
```html
<style>
.glass-panel {
  background: rgba(245, 240, 230, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 10px 15px rgba(42, 78, 108, 0.1);
  border-radius: 12px;
}
</style>

<div class="glass-panel">
  <h2>Glassmorphism Card</h2>
  <p>Vellum-like translucent effect</p>
</div>
```

---

### Floating Label Inputs (Pure CSS)
```html
<style>
.input-wrapper {
  position: relative;
  margin: 2rem 0;
}

.input-wrapper input {
  width: 100%;
  padding: 0.75rem 0;
  border: none;
  border-bottom: 1px solid #e6ddd0;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.input-wrapper input:focus {
  outline: none;
  border-bottom-color: #2a4e6c;
}

.input-wrapper label {
  position: absolute;
  left: 0;
  top: 0.75rem;
  color: #2a4e6c;
  font-size: 1rem;
  pointer-events: none;
  transition: all 0.3s ease;
}

.input-wrapper input:focus ~ label,
.input-wrapper input:not(:placeholder-shown) ~ label {
  top: -1rem;
  font-size: 0.75rem;
  color: #2a4e6c;
  font-weight: 500;
}
</style>

<div class="input-wrapper">
  <input type="text" placeholder=" " value="Felix Patel" required>
  <label>Name</label>
</div>
```

---

### Liquid Fill Progress (Pure CSS)
```html
<style>
.liquid-container {
  position: relative;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid #2a4e6c;
}

.liquid-fill {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 0%;
  background: linear-gradient(to top, #d4af37, #c5a028);
  animation: fill-up 3s ease-in-out forwards;
}

.liquid-fill::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(ellipse at center, transparent 40%, #d4af37 50%);
  animation: wave 4s linear infinite;
}

@keyframes fill-up {
  to { height: 75%; }
}

@keyframes wave {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>

<div class="liquid-container">
  <div class="liquid-fill"></div>
</div>
```

---

### Segmented Control (Pure CSS)
```html
<style>
.segmented-control {
  position: relative;
  display: inline-flex;
  background: #f5f0e6;
  border-radius: 999px;
  padding: 4px;
}

.segmented-control input[type="radio"] {
  display: none;
}

.segmented-control label {
  position: relative;
  padding: 0.75rem 2rem;
  cursor: pointer;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  color: #2c241b;
  transition: color 0.3s;
  z-index: 1;
}

.segmented-control .slider {
  position: absolute;
  top: 4px;
  left: 4px;
  width: calc(50% - 4px);
  height: calc(100% - 8px);
  background: #d4af37;
  border-radius: 999px;
  transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.segmented-control input:nth-of-type(2):checked ~ .slider {
  transform: translateX(100%);
}

.segmented-control input:checked + label {
  color: #2c241b;
}
</style>

<div class="segmented-control">
  <input type="radio" name="gender" id="male" checked>
  <label for="male">Male</label>

  <input type="radio" name="gender" id="female">
  <label for="female">Female</label>

  <div class="slider"></div>
</div>
```

---

## Complete Integration Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Harmonia Apex Match</title>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Your CSS Files -->
  <link rel="stylesheet" href="css/1-variables.css">
  <link rel="stylesheet" href="css/2-reset.css">
  <link rel="stylesheet" href="css/3-base.css">
  <link rel="stylesheet" href="css/4-layout.css">
</head>
<body>

  <!-- Your HTML Content -->

  <!-- External Libraries -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/motion@11.2.0/dist/motion.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@tsparticles/engine@3/tsparticles.engine.min.js"></script>

  <!-- Your JavaScript -->
  <script src="js/app.js"></script>
</body>
</html>
```

---

## NPM Installation (For Build Tools)

If using Node.js/build tools instead of CDN:

```bash
# tsParticles
npm install @tsparticles/engine @tsparticles/basic @tsparticles/move-base

# Motion
npm install motion

# Chart.js
npm install chart.js

# Flubber
npm install flubber

# Anime.js
npm install animejs

# Vivus
npm install vivus
```

---

## Performance Tips

1. **Load order**: Load CSS before JavaScript
2. **Defer non-critical JS**: Use `defer` attribute on script tags
3. **Lazy load animations**: Initialize only when element is in viewport
4. **Preload fonts**:
   ```html
   <link rel="preload" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond" as="style">
   ```
5. **Use CDN versions**: Faster delivery via global CDNs

---

**Last Updated**: Session 1 - January 2026
