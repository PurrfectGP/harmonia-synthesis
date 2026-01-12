# Other Implementations - What Exists on Other Branches

This document describes advanced implementations that exist on other branches in this repository. You can reference these for inspiration or to understand the full scope of the Harmonia project.

---

## Branch: `claude/quiz-design-merge-JtI2J`

**Technology:** Next.js 16.1.1 + React 19 + TypeScript + Tailwind CSS v4
**Location:** `harmonia-nextjs/` directory
**Status:** 11 sessions complete (Sessions 1-11)
**Purpose:** Modern React component library with advanced animations

### What Was Built (Sessions 1-11)

#### Session 1: Next.js + Tailwind Setup
**Commit:** `edf0c4b`
**What:** Foundation setup with Harmonia design system

**Files Created:**
- `harmonia-nextjs/package.json` - Dependencies (Next.js, React, Tailwind, Framer Motion)
- `harmonia-nextjs/app/globals.css` - Design system with Tailwind @theme directive
- `harmonia-nextjs/app/layout.tsx` - Root layout with fonts
- `harmonia-nextjs/tsconfig.json` - TypeScript configuration

**Design System:**
- Tailwind CSS v4 with inline `@theme` directive
- All color tokens converted to Tailwind format
- Cormorant Garamond + DM Sans font integration

---

#### Sessions 2-3: Typography & Layout
**What:** Design foundation for all components

**Implemented:**
- Typography scale (text-sm to text-4xl)
- Spacing system (spacing-1 to spacing-24)
- Border radius utilities (radius-sm to radius-full)
- Shadow system (shadow-sm to shadow-xl)
- Responsive breakpoints (sm, md, lg, xl)

---

#### Sessions 4-6: Module 1 - Setup (Mandatory Five Questions)
**Commit:** `9142685`
**What:** Complete first module with 5 mandatory questions

**Components Created:**

1. **`components/setup/QuestionCard.tsx`**
   - Individual question card with animation
   - Input field with validation states
   - Hover effects and transitions
   - **Future enhancement:** Gold particle effect on answer (Session 10)

2. **`components/setup/MandatoryQuestions.tsx`**
   - Container for all 5 questions
   - Progress tracking
   - Navigation between questions
   - Form state management

3. **`components/setup/BiometricSeal.tsx`**
   - HLA processing text animation
   - "Biometric Ingestion Seal" visual
   - Loading states

4. **`components/setup/InkWellProgress.tsx`**
   - Horizontal liquid fill animation
   - Progress percentage display
   - **Future enhancement:** Wave animation (Session 11)

5. **`app/setup/page.tsx`**
   - Setup module page
   - Orchestrates all setup components
   - Handles form submission to waitlist

**Features:**
- 5 mandatory questions:
  1. Age
  2. Gender
  3. Sexual Orientation
  4. Location
  5. Email
- Real-time validation
- Progress indicator
- Waitlist modal on completion

---

#### Session 7: Module 2 - Calibration (Portrait Gallery)
**Commit:** `52f1557`
**What:** Visual calibration system for rating portraits

**Components Created:**

1. **`components/calibration/PortraitGallery.tsx`**
   - Grid of 20 portrait cards
   - Portrait data structure (name, age, occupation, image)
   - Selection and rating workflow
   - Gallery animations

2. **`components/calibration/RatingSlider.tsx`**
   - Custom slider component
   - Range: 0-100 with step: 1
   - Visual feedback with color changes
   - **Future enhancement:** Spring physics (Session 9)

3. **`app/calibration/page.tsx`**
   - Calibration module page
   - Gallery + slider integration
   - Rating state management

**Features:**
- 20 diverse portraits (placeholder data)
- Click to select portrait
- Drag slider to rate (0-100)
- Submit rating and move to next portrait
- Visual feedback on selection

---

#### Session 8: Module 3 - Assessment (Seven Cardinal Drivers)
**Commit:** `7964c84`
**What:** Assessment of 7 cardinal drivers of compatibility

**Components Created:**

1. **`components/assessment/CardinalDrivers.tsx`**
   - Container for all 7 driver cards
   - Grid layout with animations
   - Progress tracking across drivers

2. **`components/assessment/DriverCard.tsx`**
   - Individual driver card
   - Question display
   - Answer selection (scale 1-7)
   - **Future enhancement:** Gold particles on answer (Session 10)

3. **`components/assessment/VerticalTube.tsx`**
   - Vertical liquid fill indicator
   - Shows progress for each driver
   - **Future enhancement:** Bubbles animation (Session 11)

4. **`app/assessment/page.tsx`**
   - Assessment module page
   - 7 drivers workflow
   - Completion tracking

**7 Cardinal Drivers:**
1. Emotional Intimacy
2. Intellectual Compatibility
3. Physical Attraction
4. Shared Values
5. Communication Style
6. Life Goals Alignment
7. Conflict Resolution

**Features:**
- Each driver has a question
- 7-point scale for answers
- Vertical tube fills as you answer
- Visual progress indicator

---

#### Session 9: Framer Motion Integration
**Commit:** `b8a8211`
**What:** Added spring physics animations throughout

**Changes:**
- Installed `framer-motion` package
- Added `<motion.div>` wrappers to components
- Implemented spring physics for smooth animations
- Enhanced RatingSlider with spring-based drag

**Spring Physics Configuration:**
```typescript
const springConfig = {
  type: "spring",
  stiffness: 300,
  damping: 30,
  mass: 1
}
```

**Animated Components:**
- QuestionCard: Slide up on mount
- DriverCard: Scale in with spring
- RatingSlider: Spring-based value changes
- PortraitGallery: Stagger animation for grid items

---

#### Session 10: Gold Particle Dissolution
**Commit:** `70b8fe0`
**What:** Visual feedback when user captures data

**Component Created:**

**`components/effects/GoldParticles.tsx`**
- Reusable particle effect system
- Configurable particle count (default: 20)
- Customizable target position
- Dissolution animation (float up, fade out)

**Integration:**
- QuestionCard: Particles appear when answering
- DriverCard: Particles on driver selection

**Animation Details:**
```typescript
// Particles float upward and fade
animate={{
  y: [0, targetY],
  opacity: [1, 0.6, 0],
  scale: [1, 0.5]
}}

// Duration: 0.8-1.2s with stagger
transition={{
  duration: 0.8 + Math.random() * 0.4,
  delay: Math.random() * 0.3
}}
```

**Visual Effect:**
- Gold particles (--gold color)
- Float upward toward data collection point
- Dissolve as they rise
- Creates "data capture" metaphor

---

#### Session 11: Liquid Fill Animations
**Commit:** `a5f63d3`
**What:** Wave and bubble effects for progress indicators

**Enhancements:**

1. **InkWellProgress (Horizontal Tube):**
   - Added liquid wave animation on top edge
   - SVG path creates wave shape
   - Continuous wave motion

2. **VerticalTube (Vertical Progress):**
   - Added wave animation at top of liquid
   - Bubble particles rising through liquid
   - Bubbles appear when progress > 10%

**Wave Animation:**
```css
@keyframes liquidWave {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(-20px);
  }
}
```

**Bubble Animation:**
```typescript
// Random bubbles rise through tube
animate={{
  y: [0, -384],  // Rise from bottom to top
  opacity: [0, 0.6, 0],
  scale: [0.5, 1, 0.5]
}}

// Duration: 3-5s, infinite loop
transition={{
  duration: 3 + Math.random() * 2,
  repeat: Infinity
}}
```

---

## Key Technical Differences from This Branch

### This Branch (Option 1)
- **Technology:** Vanilla HTML/CSS/JavaScript
- **File:** Single `frontend/index.html` (5,820 lines)
- **Animations:** CSS keyframes, basic transitions
- **State:** JavaScript variables
- **Build:** None required (open in browser)

### Next.js Branch (merge-design)
- **Technology:** Next.js + React + TypeScript
- **Files:** 17 TypeScript component files
- **Animations:** Framer Motion with spring physics
- **State:** React hooks (useState, useEffect)
- **Build:** `npm run dev` (requires Node.js)

---

## How to Port Features from Next.js to HTML

### 1. Gold Particles Effect

**Next.js (Framer Motion):**
```tsx
<motion.div
  animate={{
    y: [0, -100],
    opacity: [1, 0]
  }}
  transition={{ duration: 1 }}
/>
```

**HTML/CSS Equivalent:**
```html
<div class="particle" style="
  animation: particleRise 1s ease-out forwards;
"></div>

<style>
@keyframes particleRise {
  from {
    transform: translateY(0);
    opacity: 1;
  }
  to {
    transform: translateY(-100px);
    opacity: 0;
  }
}
</style>
```

**JavaScript:**
```javascript
function createParticle() {
  const particle = document.createElement('div');
  particle.className = 'particle';
  particle.style.cssText = `
    position: absolute;
    width: 4px;
    height: 4px;
    background: var(--gold);
    border-radius: 50%;
    left: ${Math.random() * 200 - 100}px;
  `;
  document.body.appendChild(particle);

  setTimeout(() => particle.remove(), 1000);
}
```

---

### 2. Liquid Wave Animation

**Already in HTML!** The wave animation uses CSS keyframes:

```html
<svg>
  <path d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
    fill="var(--gold)"
    style="animation: liquidWave 2s ease-in-out infinite;" />
</svg>

<style>
@keyframes liquidWave {
  0%, 100% { d: path("M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"); }
  50% { d: path("M0,5 Q25,10 50,5 T100,5 L100,10 L0,10 Z"); }
}
</style>
```

---

### 3. Spring Physics

**Next.js (Framer Motion):**
```tsx
<motion.div
  animate={{ scale: 1.05 }}
  transition={{
    type: "spring",
    stiffness: 300,
    damping: 30
  }}
/>
```

**HTML/CSS (Approximate with cubic-bezier):**
```css
.element {
  transition: transform 300ms cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.element:hover {
  transform: scale(1.05);
}
```

**Note:** True spring physics require JavaScript. Libraries like:
- `popmotion` (standalone spring animations)
- `anime.js` (spring easing functions)

---

### 4. Stagger Animation

**Next.js:**
```tsx
<motion.div variants={container}>
  {items.map((item, i) => (
    <motion.div
      key={i}
      custom={i}
      variants={item}
    />
  ))}
</motion.div>
```

**HTML/JavaScript:**
```javascript
const items = document.querySelectorAll('.item');
items.forEach((item, i) => {
  item.style.animationDelay = `${i * 0.1}s`;
  item.classList.add('fade-in');
});
```

```css
.fade-in {
  animation: fadeIn 0.5s ease-out forwards;
  opacity: 0;
}

@keyframes fadeIn {
  to { opacity: 1; }
}
```

---

## Advanced Features You Can Implement

### 1. Add Gold Particles to Question Cards

**When to show:** After user answers a question
**How:** Create particles that float toward the progress bar

```javascript
// Add to your HTML's <script> section
function showGoldParticles(targetElement) {
  const rect = targetElement.getBoundingClientRect();
  const particleCount = 20;

  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.className = 'gold-particle';
    particle.style.cssText = `
      position: fixed;
      left: ${rect.left + rect.width / 2 + Math.random() * 100 - 50}px;
      top: ${rect.top + rect.height / 2}px;
      width: 4px;
      height: 4px;
      background: var(--gold);
      border-radius: 50%;
      pointer-events: none;
      animation: particleFloat ${0.8 + Math.random() * 0.4}s ease-out forwards;
      animation-delay: ${Math.random() * 0.3}s;
    `;
    document.body.appendChild(particle);

    setTimeout(() => particle.remove(), 1500);
  }
}

// CSS
@keyframes particleFloat {
  0% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translateY(-100px) scale(0.5);
    opacity: 0;
  }
}
```

---

### 2. Add Bubbles to Progress Indicators

```javascript
function createBubble(container) {
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.style.cssText = `
    position: absolute;
    bottom: 0;
    left: ${Math.random() * 80 + 10}%;
    width: ${4 + Math.random() * 8}px;
    height: ${4 + Math.random() * 8}px;
    background: rgba(212, 168, 83, 0.4);
    border-radius: 50%;
    animation: bubbleRise ${3 + Math.random() * 2}s linear infinite;
  `;
  container.appendChild(bubble);
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

---

## Viewing the Next.js Implementation

If you want to see the actual Next.js code:

```bash
# Switch to the merge-design branch
git checkout claude/quiz-design-merge-JtI2J

# Navigate to Next.js directory
cd harmonia-nextjs

# Install dependencies
npm install

# Run development server
npm run dev

# Visit http://localhost:3000
```

**Files to explore:**
- `app/globals.css` - Complete Tailwind design system
- `components/effects/GoldParticles.tsx` - Particle system
- `components/assessment/VerticalTube.tsx` - Liquid + bubbles
- `components/setup/QuestionCard.tsx` - Card animations

---

## When to Use Next.js vs HTML

### Use HTML (This Branch) if:
- ✅ You want simple, direct control
- ✅ No build tools or dependencies
- ✅ Quick iterations and previews
- ✅ Single-page application is sufficient

### Use Next.js (merge-design) if:
- ✅ You need component reusability
- ✅ Want TypeScript type safety
- ✅ Advanced animations with Framer Motion
- ✅ Plan to scale to larger application
- ✅ Want server-side rendering benefits

---

## Summary of Advanced Features

| Feature | Next.js Branch | Can Port to HTML? |
|---------|---------------|-------------------|
| Gold Particles | ✅ Implemented | ✅ Yes (CSS + JS) |
| Liquid Waves | ✅ Implemented | ✅ Yes (SVG + CSS) |
| Bubbles | ✅ Implemented | ✅ Yes (CSS + JS) |
| Spring Physics | ✅ Framer Motion | ⚠️ Approximate with cubic-bezier |
| Stagger Animation | ✅ Framer Motion | ✅ Yes (CSS animation-delay) |
| Component System | ✅ React | ⚠️ Can use Web Components |
| TypeScript | ✅ Full support | ❌ HTML/vanilla JS only |
| Tailwind @theme | ✅ Tailwind v4 | ⚠️ Can use CSS variables |

---

**Key Takeaway:** Most visual effects from the Next.js implementation can be ported to vanilla HTML/CSS/JavaScript, though some features (like true spring physics) are easier with libraries.
