# Next.js Reference - What Exists on the Next.js Branch

**Branch:** `claude/avery-design-option2-JtI2J`
**Location:** `harmonia-nextjs/` directory
**Sessions:** 1-11 complete

This document provides a complete reference to the Next.js implementation for cross-reference purposes. Use `DESIGN_MIGRATION.md` for porting guides.

---

## Quick Overview

**What was built:**
- 17 TypeScript/React component files
- 3 modules (Setup, Calibration, Assessment)
- Gold particle effects
- Liquid fill animations with waves and bubbles
- Spring physics animations

**Technology stack:**
- Next.js 16.1.1
- React 19
- TypeScript
- Tailwind CSS v4
- Framer Motion

---

## File Structure

```
harmonia-nextjs/
├── app/
│   ├── globals.css           ← Design system (Tailwind @theme)
│   ├── layout.tsx            ← Root layout
│   ├── page.tsx              ← Home/Dashboard
│   ├── setup/page.tsx        ← Module 1: Five Questions
│   ├── calibration/page.tsx  ← Module 2: Portrait Rating
│   └── assessment/page.tsx   ← Module 3: Seven Drivers
│
├── components/
│   ├── PageTransition.tsx
│   │
│   ├── setup/ (Module 1)
│   │   ├── QuestionCard.tsx          ← Binary choice + gold particles
│   │   ├── MandatoryQuestions.tsx    ← Container for 5 questions
│   │   ├── BiometricSeal.tsx         ← Completion animation
│   │   └── InkWellProgress.tsx       ← Horizontal liquid fill + waves
│   │
│   ├── calibration/ (Module 2)
│   │   ├── PortraitGallery.tsx       ← 20 portrait grid
│   │   └── RatingSlider.tsx          ← 0-100 slider + spring physics
│   │
│   ├── assessment/ (Module 3)
│   │   ├── CardinalDrivers.tsx       ← Container for 7 drivers
│   │   ├── DriverCard.tsx            ← 7-point scale + gold particles
│   │   └── VerticalTube.tsx          ← Liquid fill + waves + bubbles
│   │
│   └── effects/
│       └── GoldParticles.tsx         ← Reusable particle effect
│
└── package.json, tsconfig.json, etc.
```

---

## Component Details

### GoldParticles (Reusable Effect)

**File:** `components/effects/GoldParticles.tsx`
**Purpose:** Visual feedback for data capture
**Lines:** 64

**Props:**
```typescript
interface GoldParticlesProps {
  isActive: boolean;        // Show/hide particles
  particleCount?: number;   // Default: 30
  targetY?: number;         // Default: -100px
}
```

**How it works:**
1. Generates random particle configurations (position, size, timing)
2. Particles spawn at center of parent element
3. Float upward with random horizontal spread (-100px to +100px)
4. Dissolve while floating (opacity: 1 → 0)
5. Each particle has unique timing (stagger effect)

**Particle configuration:**
```typescript
{
  x: Math.random() * 200 - 100,           // Horizontal spread
  y: targetY + Math.random() * -50,       // Vertical variation
  delay: Math.random() * 0.3,             // 0-300ms stagger
  duration: 0.8 + Math.random() * 0.4,   // 0.8-1.2 seconds
  size: 2 + Math.random() * 4,            // 2-6px
  opacity: 0.6 + Math.random() * 0.4      // 60-100%
}
```

**Framer Motion animation:**
```tsx
<motion.div
  initial={{
    x: 0,
    y: 0,
    opacity: 0,
    scale: 0
  }}
  animate={{
    x: particle.x,                        // Float to random X
    y: particle.y,                        // Float upward
    opacity: [0, particle.opacity, 0],    // Fade in and out
    scale: [0, 1, 0.5]                    // Grow then shrink
  }}
  transition={{
    duration: particle.duration,
    delay: particle.delay,
    ease: [0.4, 0.0, 0.2, 1]             // Custom easing
  }}
/>
```

**Styling:**
```tsx
style={{
  background: 'radial-gradient(circle, var(--champagne-400) 0%, var(--champagne-500) 100%)',
  boxShadow: '0 0 4px rgba(212, 175, 55, 0.8)'
}}
```

**Used in:**
- QuestionCard: 25 particles, targetY: -120px
- DriverCard: 30 particles, targetY: -100px

**Visual metaphor:** "Data Capture" - particles represent data being collected

---

### QuestionCard (Module 1)

**File:** `components/setup/QuestionCard.tsx`
**Purpose:** Individual question card with binary choice (A/B)
**Lines:** 110

**Props:**
```typescript
interface QuestionCardProps {
  question: Question;
  selectedChoice?: string;  // 'A' or 'B'
  onSelect: (choice: 'A' | 'B') => void;
}

interface Question {
  id: number;
  text: string;
  choiceA: string;
  choiceB: string;
  category: string;
}
```

**Features:**
- ✨ Gold particles on selection (Session 10)
- 🎯 Spring animation when clicked
- 📱 Responsive grid layout
- ✅ Visual selection state

**Key sections:**

**1. Gold particle trigger (line 54):**
```tsx
<GoldParticles
  isActive={showParticles}
  particleCount={25}
  targetY={-120}
/>
```

**2. Spring animation (lines 42-51):**
```tsx
<motion.div
  className="glass-panel p-8 rounded-lg"
  animate={{
    scale: isAnimating ? 0.98 : 1    // Slight shrink on click
  }}
  transition={{
    type: 'spring',
    stiffness: 400,                   // High stiffness = snappy
    damping: 25                       // Low damping = some bounce
  }}
>
```

**3. Choice buttons (lines 69-105):**
```tsx
<button
  onClick={() => handleChoice('A')}
  className={`
    p-6 rounded-lg border-2 transition-all duration-300
    ${selectedChoice === 'A'
      ? 'border-champagne-400 bg-champagne-400/10 shadow-lg'
      : 'border-parchment-200 hover:border-mediterranean-500/30'
    }
  `}
>
  <div className="text-sm text-champagne-500">Choice A</div>
  <div className="text-base">{question.choiceA}</div>
</button>
```

**Selection flow:**
1. User clicks choice A or B
2. `handleChoice` sets `isAnimating = true` and `showParticles = true`
3. Card shrinks slightly (spring animation)
4. 25 gold particles spawn and float upward
5. After 150ms, calls `onSelect(choice)`
6. After 1200ms, hides particles

---

### InkWellProgress (Module 1)

**File:** `components/setup/InkWellProgress.tsx`
**Purpose:** Horizontal liquid fill progress indicator
**Features:** Liquid wave animation on top edge (Session 11)

**Props:**
```typescript
interface InkWellProgressProps {
  progress: number;    // 0-100
  label?: string;
}
```

**Wave SVG (added Session 11):**
```tsx
{progress > 0 && progress < 100 && (
  <svg className="absolute -top-2 left-0 w-full h-4"
    style={{ animation: 'liquidWave 2s ease-in-out infinite' }}>
    <path
      d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
      fill="var(--mediterranean-500)"
      opacity="0.6"
    />
  </svg>
)}
```

**CSS animation:**
```css
@keyframes liquidWave {
  0%, 100% { transform: translateX(0); }
  50% { transform: translateX(-20px); }
}
```

**Effect:** Continuous 2-second wave motion on liquid surface

---

### VerticalTube (Module 3)

**File:** `components/assessment/VerticalTube.tsx`
**Purpose:** Vertical liquid progress with waves AND bubbles
**Features:** Wave + bubble animations (Session 11)

**Props:**
```typescript
interface VerticalTubeProps {
  progress: number;      // 0-100
  driverName: string;
}
```

**Wave animation (same as InkWellProgress):**
```tsx
<svg className="absolute -top-2">
  <path
    d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
    fill="var(--mediterranean-500)"
    style={{ animation: 'liquidWave 2s ease-in-out infinite' }}
  />
</svg>
```

**Bubble generation:**
```typescript
const bubbles = useMemo(() => {
  return Array.from({ length: 8 }, (_, i) => ({
    id: i,
    left: 10 + Math.random() * 80,      // 10-90% horizontal position
    size: 4 + Math.random() * 8,        // 4-12px size
    delay: Math.random() * 2,           // 0-2s delay
    duration: 3 + Math.random() * 2     // 3-5s duration
  }));
}, []);
```

**Bubble animation:**
```tsx
<motion.div
  className="absolute rounded-full"
  style={{
    left: `${bubble.left}%`,
    bottom: 0,
    width: bubble.size,
    height: bubble.size,
    background: 'rgba(212, 168, 83, 0.4)',
  }}
  animate={{
    y: [0, -384],                       // Rise from bottom to top
    opacity: [0, 0.6, 0],               // Fade in at bottom, out at top
    scale: [0.5, 1, 0.5]                // Grow in middle, shrink at top
  }}
  transition={{
    duration: bubble.duration,
    delay: bubble.delay,
    repeat: Infinity                    // Continuous loop
  }}
/>
```

**Effect:**
- 8 bubbles per tube
- Each rises from bottom to top in 3-5 seconds
- Random sizes (4-12px)
- Only visible when progress > 10%

---

### RatingSlider (Module 2)

**File:** `components/calibration/RatingSlider.tsx`
**Purpose:** 0-100 slider with spring physics
**Features:** Spring-based drag interaction (Session 9)

**Props:**
```typescript
interface RatingSliderProps {
  value: number;           // Current value (0-100)
  onChange: (value: number) => void;
  label?: string;
}
```

**Spring physics:**
```tsx
<motion.div
  drag="x"
  dragConstraints={{ left: 0, right: 100 }}
  dragElastic={0}
  onDrag={(event, info) => {
    const newValue = Math.round((info.point.x / trackWidth) * 100);
    onChange(newValue);
  }}
  transition={{
    type: "spring",
    stiffness: 300,        // How tight the spring is
    damping: 30,           // How quickly it settles
    mass: 1                // Weight of the object
  }}
>
  {/* Slider thumb */}
</motion.div>
```

**Effect:**
- Smooth drag interaction
- Spring bounce on release
- Natural physics feel

---

### DriverCard (Module 3)

**File:** `components/assessment/DriverCard.tsx`
**Purpose:** Individual driver question with 7-point scale
**Features:** Gold particles on answer selection (Session 10)

**Props:**
```typescript
interface DriverCardProps {
  driver: {
    id: number;
    name: string;
    question: string;
  };
  answer?: number;  // 1-7
  onAnswer: (value: number) => void;
}
```

**7-point scale buttons:**
```tsx
{[1, 2, 3, 4, 5, 6, 7].map(value => (
  <button
    onClick={() => handleAnswer(value)}
    className={`
      w-12 h-12 rounded-full border-2
      ${answer === value
        ? 'bg-champagne-400 border-champagne-400'
        : 'border-parchment-200 hover:border-champagne-400'
      }
    `}
  >
    {value}
  </button>
))}
```

**Gold particles integration:**
```tsx
<GoldParticles isActive={showParticles} />
```

Triggers when user selects any rating (1-7)

---

## Design System (globals.css)

**File:** `app/globals.css`
**System:** Tailwind CSS v4 with `@theme inline` directive

### Color Tokens

```css
/* Parchment - Warm backgrounds */
--color-parchment-50: #fbf9f5;
--color-parchment-100: #f5f0e6;
--color-parchment-200: #e6ddd0;
--color-parchment-900: #2c241b;

/* Mediterranean - Primary actions */
--color-mediterranean-500: #2a4e6c;
--color-mediterranean-600: #1f3b54;

/* Champagne - Gold accents */
--color-champagne-400: #d4af37;
--color-champagne-500: #c5a028;
--color-champagne-600: #a88b20;

/* Danger - Alerts */
--color-danger-500: #8b0000;
```

### Typography Tokens

```css
--font-serif: 'Cormorant Garamond', serif;
--font-sans: 'DM Sans', sans-serif;

--font-size-xs: 0.75rem;     /* 12px */
--font-size-sm: 0.875rem;    /* 14px */
--font-size-base: 1rem;      /* 16px */
--font-size-lg: 1.125rem;    /* 18px */
--font-size-xl: 1.25rem;     /* 20px */
--font-size-2xl: 1.5rem;     /* 24px */
--font-size-3xl: 1.875rem;   /* 30px */
--font-size-4xl: 2.25rem;    /* 36px */
```

### Spacing Tokens

```css
--spacing-1: 0.25rem;    /* 4px */
--spacing-2: 0.5rem;     /* 8px */
--spacing-3: 0.75rem;    /* 12px */
--spacing-4: 1rem;       /* 16px */
--spacing-6: 1.5rem;     /* 24px */
--spacing-8: 2rem;       /* 32px */
--spacing-12: 3rem;      /* 48px */
--spacing-16: 4rem;      /* 64px */
```

---

## Animation Configurations

### Spring Physics (Framer Motion)

**QuestionCard click:**
```typescript
{
  type: 'spring',
  stiffness: 400,    // High = snappy
  damping: 25        // Low = bouncy
}
```

**RatingSlider drag:**
```typescript
{
  type: 'spring',
  stiffness: 300,    // Medium = balanced
  damping: 30        // Medium = some bounce
}
```

**General guideline:**
- **Stiffness:** 200-500 (higher = faster, snappier)
- **Damping:** 20-40 (lower = more bounce)
- **Mass:** 0.5-2 (higher = slower, heavier)

### CSS Animations

**Liquid wave:**
```css
@keyframes liquidWave {
  0%, 100% { transform: translateX(0); }
  50% { transform: translateX(-20px); }
}

/* Duration: 2s
   Easing: ease-in-out
   Loop: infinite */
```

**Particle float (if not using Framer Motion):**
```css
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

/* Duration: 0.8-1.2s
   Easing: ease-out
   Loop: none (forwards) */
```

---

## Component Relationships

### Module 1 Flow
```
setup/page.tsx
  └── MandatoryQuestions
      ├── QuestionCard (×5)
      │   └── GoldParticles
      ├── InkWellProgress
      └── BiometricSeal
```

### Module 2 Flow
```
calibration/page.tsx
  └── PortraitGallery
      └── RatingSlider
```

### Module 3 Flow
```
assessment/page.tsx
  └── CardinalDrivers
      └── DriverCard (×7)
          ├── GoldParticles
          └── VerticalTube
```

---

## Key Implementation Patterns

### State Management

**Component-level state:**
```tsx
const [answer, setAnswer] = useState<string>('');
const [showParticles, setShowParticles] = useState(false);
```

**Parent → Child (props down):**
```tsx
<QuestionCard
  question={currentQuestion}
  selectedChoice={answers[currentQuestion.id]}
  onSelect={(choice) => handleAnswer(currentQuestion.id, choice)}
/>
```

**Child → Parent (callbacks up):**
```tsx
// Child calls parent's function
onSelect('A');

// Parent handles the update
const handleAnswer = (questionId, choice) => {
  setAnswers(prev => ({ ...prev, [questionId]: choice }));
};
```

### Animation Triggers

**On user action:**
```tsx
const handleClick = () => {
  setShowParticles(true);           // Trigger effect
  setTimeout(() => {
    setShowParticles(false);        // Hide after animation
  }, 1200);
};
```

**On mount:**
```tsx
<motion.div
  initial={{ opacity: 0 }}          // Starting state
  animate={{ opacity: 1 }}          // Ending state
  transition={{ duration: 0.3 }}
>
```

### Conditional Rendering

**Show only when condition met:**
```tsx
{progress > 0 && progress < 100 && (
  <WaveAnimation />
)}

{showParticles && (
  <GoldParticles isActive={true} />
)}
```

---

## Feature Summary

| Feature | File | Lines | Session Added |
|---------|------|-------|---------------|
| Gold Particles | GoldParticles.tsx | 64 | Session 10 |
| Question Card | QuestionCard.tsx | 110 | Sessions 4-6, enhanced 10 |
| Liquid Waves | InkWellProgress, VerticalTube | ~50 each | Session 11 |
| Rising Bubbles | VerticalTube | ~80 | Session 11 |
| Spring Slider | RatingSlider.tsx | ~120 | Session 7, enhanced 9 |
| Driver Card | DriverCard.tsx | ~130 | Session 8, enhanced 10 |

---

## Technology Choices

### Why Framer Motion?

**Pros:**
- Easy spring physics
- Declarative animations
- Great performance
- TypeScript support

**Alternative in HTML:**
- CSS animations (simpler features)
- anime.js or popmotion (spring physics)
- GSAP (complex timelines)

### Why Tailwind CSS v4?

**Pros:**
- Inline `@theme` directive
- No external config file
- Native CSS variables
- Utility-first workflow

**Alternative in HTML:**
- Regular CSS variables
- CSS Modules
- Styled-components

### Why TypeScript?

**Pros:**
- Type safety
- Better IDE support
- Fewer runtime errors
- Self-documenting props

**Alternative in HTML:**
- JavaScript with JSDoc
- PropTypes (React)
- Just vanilla JS

---

## Quick Reference

### To view this implementation:

```bash
git checkout claude/avery-design-option2-JtI2J
cd harmonia-nextjs
npm install
npm run dev
# Visit http://localhost:3000
```

### To see specific files:

```bash
# Design system
cat harmonia-nextjs/app/globals.css

# Gold particles
cat harmonia-nextjs/components/effects/GoldParticles.tsx

# Liquid animations
cat harmonia-nextjs/components/setup/InkWellProgress.tsx
cat harmonia-nextjs/components/assessment/VerticalTube.tsx

# Spring physics
cat harmonia-nextjs/components/calibration/RatingSlider.tsx
```

---

**Use DESIGN_MIGRATION.md to port these features to vanilla HTML!**
