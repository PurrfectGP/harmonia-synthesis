# Design Migration Guide - React to Vanilla HTML/JS

**Purpose:** Step-by-step guides for porting Next.js features to vanilla HTML

---

## Quick Reference

| Feature | Difficulty | Time | Worth It? |
|---------|-----------|------|-----------|
| Gold Particles | ⭐⭐ Medium | 30 min | ✅ Yes - Great impact |
| Liquid Waves | ⭐⭐ Medium | 15 min | ✅ Yes - Same technique |
| Bubbles | ⭐⭐ Medium | 20 min | ✅ Yes - Nice visual |
| Spring Physics | ⭐⭐⭐ Hard | 60+ min | ⚠️ Use cubic-bezier instead |
| Stagger Animation | ⭐⭐ Medium | 10 min | ✅ Yes - Simple |

---

## 1. Gold Particles Effect

### React Version (from Next.js)

```tsx
<GoldParticles
  isActive={showParticles}
  particleCount={25}
  targetY={-120}
/>
```

### Vanilla HTML/JS Version

**Step 1: Add HTML container**
```html
<div id="particle-container" style="position: relative;">
  <!-- Your content (button, card, etc.) -->
</div>
```

**Step 2: Add CSS**
```css
.gold-particle {
  position: absolute;
  width: 4px;
  height: 4px;
  background: radial-gradient(circle, var(--gold-champagne) 0%, var(--gold) 100%);
  border-radius: 50%;
  box-shadow: 0 0 4px rgba(212, 175, 55, 0.8);
  pointer-events: none;
  animation: particleFloat var(--duration) ease-out forwards;
}

@keyframes particleFloat {
  0% {
    transform: translate(0, 0) scale(1);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  100% {
    transform: translate(var(--x), var(--y)) scale(0.5);
    opacity: 0;
  }
}
```

**Step 3: Add JavaScript function**
```javascript
function createGoldParticles(element, count = 25, targetY = -120) {
  const rect = element.getBoundingClientRect();
  const centerX = rect.left + rect.width / 2;
  const centerY = rect.top + rect.height / 2;

  for (let i = 0; i < count; i++) {
    const particle = document.createElement('div');
    particle.className = 'gold-particle';

    // Random values
    const x = Math.random() * 200 - 100; // -100 to +100
    const y = targetY + Math.random() * -50;
    const size = 2 + Math.random() * 4; // 2-6px
    const duration = 0.8 + Math.random() * 0.4; // 0.8-1.2s
    const delay = Math.random() * 0.3; // 0-300ms

    // Set custom properties
    particle.style.cssText = `
      left: ${centerX}px;
      top: ${centerY}px;
      width: ${size}px;
      height: ${size}px;
      --x: ${x}px;
      --y: ${y}px;
      --duration: ${duration}s;
      animation-delay: ${delay}s;
    `;

    document.body.appendChild(particle);

    // Remove after animation
    setTimeout(() => particle.remove(), (duration + delay) * 1000 + 100);
  }
}
```

**Step 4: Trigger on user action**
```javascript
document.getElementById('answerButton').addEventListener('click', function() {
  createGoldParticles(this, 25, -120);
  // Handle answer logic...
});
```

---

## 2. Liquid Wave Animation

### React Version

```tsx
<svg className="absolute -top-2" style={{ animation: 'liquidWave 2s ease-in-out infinite' }}>
  <path d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
        fill="var(--mediterranean-500)" opacity="0.6" />
</svg>
```

### Vanilla HTML Version

**Step 1: Add SVG to progress bar**
```html
<div class="progress-container">
  <div class="progress-fill" style="width: 75%;">
    <svg class="liquid-wave" viewBox="0 0 100 10" preserveAspectRatio="none">
      <path d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
            fill="var(--gold)" opacity="0.6" />
    </svg>
  </div>
</div>
```

**Step 2: Add CSS**
```css
.progress-container {
  position: relative;
  width: 100%;
  height: 20px;
  background: var(--cream);
  border-radius: 10px;
  overflow: hidden;
}

.progress-fill {
  position: relative;
  height: 100%;
  background: var(--gold);
  transition: width 0.5s ease;
}

.liquid-wave {
  position: absolute;
  top: -2px;
  left: 0;
  width: 100%;
  height: 10px;
  animation: liquidWave 2s ease-in-out infinite;
}

@keyframes liquidWave {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(-20px);
  }
}
```

**Step 3: Update progress via JavaScript**
```javascript
function updateProgress(percentage) {
  const fill = document.querySelector('.progress-fill');
  fill.style.width = percentage + '%';
}

// Usage
updateProgress(75); // 75% filled
```

---

## 3. Rising Bubbles

### React Version

```tsx
<motion.div
  animate={{
    y: [0, -384],
    opacity: [0, 0.6, 0],
    scale: [0.5, 1, 0.5]
  }}
  transition={{
    duration: 3 + Math.random() * 2,
    repeat: Infinity
  }}
/>
```

### Vanilla HTML/JS Version

**Step 1: Add HTML container**
```html
<div class="vertical-tube">
  <div class="liquid-fill" style="height: 75%;">
    <div id="bubbles-container"></div>
  </div>
</div>
```

**Step 2: Add CSS**
```css
.vertical-tube {
  position: relative;
  width: 60px;
  height: 400px;
  background: var(--cream);
  border-radius: 30px;
  overflow: hidden;
}

.liquid-fill {
  position: absolute;
  bottom: 0;
  width: 100%;
  background: var(--gold);
  transition: height 0.5s ease;
}

#bubbles-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.bubble {
  position: absolute;
  bottom: 0;
  background: rgba(212, 168, 83, 0.4);
  border-radius: 50%;
  animation: bubbleRise var(--duration) linear infinite;
  animation-delay: var(--delay);
}

@keyframes bubbleRise {
  0% {
    transform: translateY(0) scale(0.5);
    opacity: 0;
  }
  10% {
    opacity: 0.6;
  }
  90% {
    opacity: 0.6;
  }
  100% {
    transform: translateY(-400px) scale(1);
    opacity: 0;
  }
}
```

**Step 3: Generate bubbles with JavaScript**
```javascript
function createBubbles(container, count = 8) {
  // Clear existing
  container.innerHTML = '';

  for (let i = 0; i < count; i++) {
    const bubble = document.createElement('div');
    bubble.className = 'bubble';

    const left = 10 + Math.random() * 80; // 10-90%
    const size = 4 + Math.random() * 8; // 4-12px
    const duration = 3 + Math.random() * 2; // 3-5s
    const delay = Math.random() * 2; // 0-2s

    bubble.style.cssText = `
      left: ${left}%;
      width: ${size}px;
      height: ${size}px;
      --duration: ${duration}s;
      --delay: ${delay}s;
    `;

    container.appendChild(bubble);
  }
}

// Initialize
const bubblesContainer = document.getElementById('bubbles-container');
createBubbles(bubblesContainer, 8);
```

---

## 4. Spring Physics (Approximation)

### React Version

```tsx
transition={{
  type: "spring",
  stiffness: 300,
  damping: 30
}}
```

### Vanilla HTML Version (Cubic-Bezier Approximation)

**Option 1: Use cubic-bezier (⭐⭐ Medium)**

```css
.spring-element {
  transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

/* This creates a bounce effect similar to spring physics */
```

**Common cubic-bezier curves:**
```css
/* Bounce (like spring with stiffness: 300, damping: 30) */
cubic-bezier(0.68, -0.55, 0.27, 1.55)

/* Slight bounce */
cubic-bezier(0.34, 1.56, 0.64, 1)

/* Smooth ease (no bounce) */
cubic-bezier(0.4, 0.0, 0.2, 1)

/* Ease-out */
cubic-bezier(0.0, 0.0, 0.2, 1)
```

**JavaScript usage:**
```javascript
element.style.transform = 'scale(0.98)';
element.style.transition = 'transform 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55)';

setTimeout(() => {
  element.style.transform = 'scale(1)';
}, 50);
```

**Option 2: Use anime.js library (⭐⭐⭐ Hard)**

```html
<!-- Add library -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
```

```javascript
anime({
  targets: '.element',
  scale: 1.05,
  duration: 400,
  easing: 'spring(1, 80, 10, 0)' // mass, stiffness, damping, velocity
});
```

**Recommendation:** Use cubic-bezier. It's 95% as good and requires no library.

---

## 5. Stagger Animation

### React Version

```tsx
{items.map((item, i) => (
  <motion.div
    custom={i}
    initial={{ opacity: 0 }}
    animate={{ opacity: 1 }}
    transition={{ delay: i * 0.1 }}
  >
    {item}
  </motion.div>
))}
```

### Vanilla HTML/JS Version

**Step 1: Add HTML**
```html
<div class="items-container">
  <div class="item">Item 1</div>
  <div class="item">Item 2</div>
  <div class="item">Item 3</div>
</div>
```

**Step 2: Add CSS**
```css
.item {
  opacity: 0;
  animation: fadeIn 0.5s ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Step 3: Set delays with JavaScript**
```javascript
const items = document.querySelectorAll('.item');
items.forEach((item, index) => {
  item.style.animationDelay = `${index * 0.1}s`; // 100ms stagger
});
```

---

## 6. Selection States

### React Version

```tsx
const [selected, setSelected] = useState(null);

<button
  onClick={() => setSelected(id)}
  className={selected === id ? 'selected' : ''}
>
```

### Vanilla HTML Version

**Step 1: Add HTML**
```html
<div class="button-group">
  <button class="choice-button" data-choice="A">Choice A</button>
  <button class="choice-button" data-choice="B">Choice B</button>
</div>
```

**Step 2: Add CSS**
```css
.choice-button {
  padding: 16px 32px;
  border: 2px solid var(--gray-light);
  background: var(--cream);
  transition: all 0.3s ease;
}

.choice-button:hover {
  border-color: var(--gold);
}

.choice-button.selected {
  border-color: var(--gold);
  background: rgba(212, 168, 83, 0.1);
  box-shadow: 0 4px 12px rgba(212, 168, 83, 0.3);
}
```

**Step 3: Add JavaScript**
```javascript
const buttons = document.querySelectorAll('.choice-button');

buttons.forEach(button => {
  button.addEventListener('click', function() {
    // Remove selected from all
    buttons.forEach(btn => btn.classList.remove('selected'));

    // Add to clicked
    this.classList.add('selected');

    // Get choice value
    const choice = this.dataset.choice;
    console.log('Selected:', choice);
  });
});
```

---

## 7. Form State Management

### React Version

```tsx
const [answers, setAnswers] = useState({});

const handleAnswer = (questionId, value) => {
  setAnswers(prev => ({ ...prev, [questionId]: value }));
};
```

### Vanilla HTML Version

**Step 1: Create state object**
```javascript
const formState = {
  answers: {},
  progress: 0
};

function updateAnswer(questionId, value) {
  formState.answers[questionId] = value;
  formState.progress = Object.keys(formState.answers).length;

  // Update UI
  updateProgressBar(formState.progress);
}
```

**Step 2: Bind to inputs**
```javascript
document.getElementById('ageInput').addEventListener('input', (e) => {
  updateAnswer('age', e.target.value);
});

document.getElementById('genderSelect').addEventListener('change', (e) => {
  updateAnswer('gender', e.target.value);
});
```

**Step 3: Update progress UI**
```javascript
function updateProgressBar(answeredCount) {
  const total = 5; // Total questions
  const percentage = (answeredCount / total) * 100;
  document.querySelector('.progress-fill').style.width = percentage + '%';
}
```

---

## Conversion Cheat Sheet

| React Pattern | Vanilla HTML Equivalent |
|--------------|------------------------|
| `useState(value)` | `let value = ...` |
| `setState(newValue)` | `value = newValue; updateUI();` |
| `onClick={() => func()}` | `element.addEventListener('click', func)` |
| `className={condition ? 'a' : 'b'}` | `element.classList.toggle('a', condition)` |
| `style={{ width: value }}` | `element.style.width = value` |
| `{items.map(item => ...)}` | `items.forEach(item => ...)` |
| `useEffect(() => {}, [])` | Run code directly (no hook needed) |
| `<motion.div animate={...}>` | CSS `@keyframes` + `animation` |
| Framer Motion spring | `cubic-bezier()` or anime.js |
| Tailwind classes | Regular CSS classes |

---

## Performance Tips

### Use RequestAnimationFrame for Smooth Animations

```javascript
function animateParticle(particle, start, end) {
  const startTime = performance.now();
  const duration = 1000; // 1 second

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    // Update position
    const y = start + (end - start) * progress;
    particle.style.transform = `translateY(${y}px)`;

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      particle.remove();
    }
  }

  requestAnimationFrame(update);
}
```

### Reuse Elements (Object Pooling)

```javascript
const particlePool = [];

function getParticle() {
  if (particlePool.length > 0) {
    return particlePool.pop();
  }
  return document.createElement('div');
}

function recycleParticle(particle) {
  particle.remove();
  particlePool.push(particle);
}
```

---

## Testing Your Port

### Checklist:

- [ ] Visual appearance matches Next.js version
- [ ] Animation timing feels similar
- [ ] Performance is smooth (60fps)
- [ ] Works on mobile
- [ ] No console errors
- [ ] Accessibility maintained (keyboard navigation)

### Browser DevTools:

```javascript
// Check animation performance
// Open DevTools → Performance tab
// Record → Trigger animation → Stop → Check FPS

// Check for layout thrashing
// Look for purple bars in timeline
// Minimize reads/writes to DOM
```

---

## Common Pitfalls

### ❌ Don't: Force synchronous layout

```javascript
// BAD: Reading then writing in a loop
for (let i = 0; i < 100; i++) {
  const width = element.offsetWidth; // Read (forces layout)
  element.style.width = width + 1 + 'px'; // Write
}

// GOOD: Batch reads, then batch writes
const widths = [];
for (let i = 0; i < 100; i++) {
  widths.push(element.offsetWidth); // Batch reads
}
for (let i = 0; i < 100; i++) {
  element.style.width = widths[i] + 1 + 'px'; // Batch writes
}
```

### ❌ Don't: Animate expensive properties

```javascript
// BAD: Animates layout properties
@keyframes bad {
  from { margin-left: 0; }
  to { margin-left: 100px; }
}

// GOOD: Use transform (GPU-accelerated)
@keyframes good {
  from { transform: translateX(0); }
  to { transform: translateX(100px); }
}
```

### ✅ Do: Use CSS for simple animations

```css
/* Better than JavaScript for simple transitions */
.element {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
```

---

**Ready to port features!** Start with liquid waves (easiest), then gold particles, then bubbles.
