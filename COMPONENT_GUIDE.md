# Component Guide - Harmonia Next.js

**Complete map of all 17 React components**
**Location:** `harmonia-nextjs/`

---

## Component Overview

| Module | Components | Count |
|--------|-----------|-------|
| **Pages** | Home, Setup, Calibration, Assessment | 4 |
| **Setup (Module 1)** | QuestionCard, MandatoryQuestions, BiometricSeal, InkWellProgress | 4 |
| **Calibration (Module 2)** | PortraitGallery, RatingSlider | 2 |
| **Assessment (Module 3)** | CardinalDrivers, DriverCard, VerticalTube | 3 |
| **Effects** | GoldParticles | 1 |
| **Shared** | PageTransition, Layout | 2 |
| **Config** | globals.css | 1 |

**Total:** 17 files

---

## Pages (4 files)

### 1. `app/page.tsx` - Home/Dashboard

**Purpose:** Landing page with module navigation
**Route:** `/` (http://localhost:3000)

**What it does:**
- Displays Harmonia title and tagline
- Shows navigation to 3 modules
- Provides visual entry point

**Key sections:**
```tsx
<h1>Harmonia</h1>
<p>The Compatibility Engine</p>

<Link href="/setup">Module 1: Setup</Link>
<Link href="/calibration">Module 2: Calibration</Link>
<Link href="/assessment">Module 3: Assessment</Link>
```

**Edit to:**
- Change homepage layout
- Modify navigation structure
- Add introductory content

---

### 2. `app/setup/page.tsx` - Module 1: Setup

**Purpose:** Five mandatory questions for initial data collection
**Route:** `/setup`

**What it does:**
- Renders `<MandatoryQuestions />` component
- Handles questionnaire flow
- Shows completion state

**Components used:**
- `MandatoryQuestions` (main container)
- `QuestionCard` (individual questions)
- `BiometricSeal` (completion animation)
- `InkWellProgress` (progress indicator)

**Edit to:**
- Modify page layout
- Change module introduction
- Adjust spacing

---

### 3. `app/calibration/page.tsx` - Module 2: Calibration

**Purpose:** Portrait rating for visual calibration
**Route:** `/calibration`

**What it does:**
- Displays portrait gallery
- Allows user to rate portraits 0-100
- Tracks rating progress

**Components used:**
- `PortraitGallery` (grid of portraits)
- `RatingSlider` (0-100 slider)

**Edit to:**
- Change gallery layout
- Modify instructions
- Adjust portrait count

---

### 4. `app/assessment/page.tsx` - Module 3: Assessment

**Purpose:** Seven Cardinal Drivers assessment
**Route:** `/assessment`

**What it does:**
- Presents 7 compatibility drivers
- Collects user responses
- Shows progress with vertical tubes

**Components used:**
- `CardinalDrivers` (main container)
- `DriverCard` (individual driver questions)
- `VerticalTube` (liquid progress indicator)

**Edit to:**
- Modify assessment layout
- Change driver presentation
- Adjust progress visualization

---

## Setup Components (Module 1)

### 5. `components/setup/QuestionCard.tsx`

**Purpose:** Individual question card with binary choice
**File:** `harmonia-nextjs/components/setup/QuestionCard.tsx:1`

**Props:**
```typescript
interface QuestionCardProps {
  question: Question;       // Question object
  selectedChoice?: string;  // Current selection ('A' or 'B')
  onSelect: (choice: 'A' | 'B') => void; // Selection handler
}
```

**Features:**
- ✨ **Gold particles** on answer selection (Session 10)
- 🎯 Spring animation when clicked
- 🎨 Two-button choice interface (A/B)
- 📱 Responsive grid layout

**Key code sections:**
```tsx
// Line 54: Gold particles trigger
<GoldParticles isActive={showParticles} particleCount={25} targetY={-120} />

// Lines 69-86: Choice A button
<button onClick={() => handleChoice('A')}>
  <div>Choice A</div>
  <div>{question.choiceA}</div>
</button>

// Lines 88-105: Choice B button (same structure)
```

**Edit to:**
- Change button styling (lines 71-79, 90-98)
- Modify particle count (line 54: `particleCount={25}`)
- Adjust spring physics (lines 48-50)
- Change text sizing (line 63: `text-2xl`)

---

### 6. `components/setup/MandatoryQuestions.tsx`

**Purpose:** Container for all 5 mandatory questions
**File:** `harmonia-nextjs/components/setup/MandatoryQuestions.tsx:1`

**What it manages:**
- Question flow (1-5)
- Answer state for all questions
- Progress tracking
- Navigation (Previous/Next)
- Completion modal

**Features:**
- State management with `useState`
- Progress calculation
- Validation before proceeding

**Edit to:**
- Change number of questions
- Modify navigation buttons
- Adjust progress display

---

### 7. `components/setup/BiometricSeal.tsx`

**Purpose:** HLA processing animation on completion
**File:** `harmonia-nextjs/components/setup/BiometricSeal.tsx:1`

**What it does:**
- Shows "Biometric Ingestion Seal" text
- Animated HLA processing message
- Completion confirmation

**Features:**
- Text animation
- Seal visual
- Completion state

**Edit to:**
- Change animation timing
- Modify text content
- Adjust visual styling

---

### 8. `components/setup/InkWellProgress.tsx`

**Purpose:** Horizontal liquid fill progress indicator
**File:** `harmonia-nextjs/components/setup/InkWellProgress.tsx:1`

**Props:**
```typescript
interface InkWellProgressProps {
  progress: number;  // 0-100
  label?: string;    // Optional label
}
```

**Features:**
- ✨ **Liquid wave animation** on top edge (Session 11)
- Horizontal fill based on progress
- Smooth transitions

**Key sections:**
- Liquid fill background
- Wave SVG overlay
- Progress percentage display

**Edit to:**
- Change wave animation timing
- Modify liquid color
- Adjust height/width

---

## Calibration Components (Module 2)

### 9. `components/calibration/PortraitGallery.tsx`

**Purpose:** Grid of 20 portrait cards for rating
**File:** `harmonia-nextjs/components/calibration/PortraitGallery.tsx:1`

**Props:**
```typescript
interface PortraitGalleryProps {
  onPortraitSelect: (portraitId: number) => void;
  selectedPortrait?: number;
}
```

**Features:**
- Grid layout (4 columns on desktop, responsive)
- Portrait selection
- Visual selection state
- Hover effects

**Portrait data structure:**
```typescript
{
  id: number,
  name: string,
  age: number,
  occupation: string,
  imageUrl: string
}
```

**Edit to:**
- Change grid columns (adjust `grid-cols-*`)
- Modify portrait count (add/remove from array)
- Change card styling
- Adjust hover effects

---

### 10. `components/calibration/RatingSlider.tsx`

**Purpose:** 0-100 slider with spring physics
**File:** `harmonia-nextjs/components/calibration/RatingSlider.tsx:1`

**Props:**
```typescript
interface RatingSliderProps {
  value: number;           // Current value (0-100)
  onChange: (value: number) => void;
  label?: string;
}
```

**Features:**
- ✨ **Spring physics** on drag (Session 9)
- Visual feedback with color changes
- Smooth value transitions
- Percentage display

**Spring configuration:**
```typescript
transition={{
  type: "spring",
  stiffness: 300,
  damping: 30
}}
```

**Edit to:**
- Adjust spring stiffness (line ~45: `stiffness: 300`)
- Change color gradient
- Modify slider track height
- Adjust label styling

---

## Assessment Components (Module 3)

### 11. `components/assessment/CardinalDrivers.tsx`

**Purpose:** Container for 7 cardinal driver questions
**File:** `harmonia-nextjs/components/assessment/CardinalDrivers.tsx:1`

**What it manages:**
- All 7 driver states
- Progress across drivers
- Completion tracking

**7 Cardinal Drivers:**
1. Emotional Intimacy
2. Intellectual Compatibility
3. Physical Attraction
4. Shared Values
5. Communication Style
6. Life Goals Alignment
7. Conflict Resolution

**Edit to:**
- Change number of drivers
- Modify driver questions
- Adjust layout grid

---

### 12. `components/assessment/DriverCard.tsx`

**Purpose:** Individual driver question card
**File:** `harmonia-nextjs/components/assessment/DriverCard.tsx:1`

**Props:**
```typescript
interface DriverCardProps {
  driver: {
    id: number;
    name: string;
    question: string;
  };
  answer?: number;  // 1-7 scale
  onAnswer: (value: number) => void;
}
```

**Features:**
- ✨ **Gold particles** on answer selection (Session 10)
- 7-point scale buttons
- Visual selection state
- Spring animation

**Key sections:**
```tsx
// Gold particles
<GoldParticles isActive={showParticles} />

// 7 buttons (1-7 scale)
{[1, 2, 3, 4, 5, 6, 7].map(value => (
  <button onClick={() => handleAnswer(value)}>
    {value}
  </button>
))}
```

**Edit to:**
- Change scale range (modify array)
- Adjust button styling
- Modify particle effect
- Change layout

---

### 13. `components/assessment/VerticalTube.tsx`

**Purpose:** Vertical liquid progress indicator with bubbles
**File:** `harmonia-nextjs/components/assessment/VerticalTube.tsx:1`

**Props:**
```typescript
interface VerticalTubeProps {
  progress: number;  // 0-100
  driverName: string;
}
```

**Features:**
- ✨ **Liquid fill animation** (Session 11)
- ✨ **Bubble particles** rising through liquid (Session 11)
- Wave animation on top edge
- Vertical fill from bottom

**Key animations:**

**1. Liquid wave (top edge):**
```tsx
<svg className="absolute -top-2">
  <path d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
    style={{ animation: 'liquidWave 2s ease-in-out infinite' }} />
</svg>
```

**2. Rising bubbles:**
```tsx
<motion.div
  animate={{
    y: [0, -384],          // Rise from bottom to top
    opacity: [0, 0.6, 0],  // Fade in and out
    scale: [0.5, 1, 0.5]   // Size variation
  }}
  transition={{
    duration: 3-5s,
    repeat: Infinity
  }}
/>
```

**Edit to:**
- Change wave frequency (animation duration)
- Adjust bubble count (modify `bubbles` array)
- Modify bubble speed (transition duration)
- Change liquid color

---

## Effects Components

### 14. `components/effects/GoldParticles.tsx`

**Purpose:** Reusable gold particle dissolution effect
**File:** `harmonia-nextjs/components/effects/GoldParticles.tsx:1`

**Props:**
```typescript
interface GoldParticlesProps {
  isActive: boolean;      // Show/hide particles
  particleCount?: number; // Default: 30
  targetY?: number;       // Default: -100
}
```

**How it works:**
1. Generates random particle configurations
2. Particles start at center (50%, 50%)
3. Float upward with random spread
4. Dissolve as they rise (opacity fade)
5. Random sizes, delays, durations

**Particle configuration:**
```typescript
{
  x: Math.random() * 200 - 100,  // Horizontal spread
  y: targetY + Math.random() * -50, // Vertical variation
  delay: Math.random() * 0.3,    // Stagger
  duration: 0.8 + Math.random() * 0.4, // 0.8-1.2s
  size: 2 + Math.random() * 4    // 2-6px
}
```

**Used in:**
- `QuestionCard` (25 particles, targetY: -120)
- `DriverCard` (30 particles, default)

**Edit to:**
- Adjust particle count (prop)
- Change target height (prop)
- Modify particle size range (line 21)
- Change colors (line 39: `--champagne-400`)
- Adjust duration range (line 20)

---

## Shared Components

### 15. `components/PageTransition.tsx`

**Purpose:** Fade transition between pages
**File:** `harmonia-nextjs/components/PageTransition.tsx:1`

**What it does:**
- Wraps page content
- Animates on page load
- Provides consistent transitions

**Animation:**
```tsx
<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  exit={{ opacity: 0 }}
  transition={{ duration: 0.3 }}
>
  {children}
</motion.div>
```

**Edit to:**
- Change transition duration
- Modify animation type (fade, slide, scale)
- Add additional effects

---

### 16. `app/layout.tsx` - Root Layout

**Purpose:** Top-level application wrapper
**File:** `harmonia-nextjs/app/layout.tsx:1`

**What it includes:**
- Google Fonts loading
- Metadata (title, description)
- Root HTML structure
- Global styles (`globals.css`)

**Fonts loaded:**
```tsx
const cormorant = Cormorant_Garamond({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700']
});

const dmSans = DM_Sans({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700']
});
```

**Edit to:**
- Change fonts
- Modify metadata
- Add global providers
- Include analytics

---

## Design System

### 17. `app/globals.css` - Design Tokens

**Purpose:** Complete design system with Tailwind @theme
**File:** `harmonia-nextjs/app/globals.css:1`

**Structure:**
```css
@theme {
  /* Lines 1-50: Color tokens */
  --color-parchment-*
  --color-champagne-*
  --color-mediterranean-*

  /* Lines 51-70: Spacing */
  --spacing-*

  /* Lines 71-90: Typography */
  --font-serif
  --font-sans
  --text-*

  /* Lines 91-110: Shadows, borders, etc. */
}
```

**Key sections to edit:**

**Colors (lines 1-50):**
```css
--color-cream: #FAF6F1;
--color-gold: #D4A853;
--color-navy: #1E293B;
```

**Spacing (lines 51-70):**
```css
--spacing-1: 0.25rem;
--spacing-4: 1rem;
--spacing-12: 3rem;
```

**Typography (lines 71-90):**
```css
--font-serif: 'Cormorant Garamond', serif;
--font-sans: 'DM Sans', sans-serif;
--text-xs: 0.75rem;
--text-4xl: 2.25rem;
```

**Edit to:**
- Change color palette (update hex values)
- Adjust spacing scale
- Modify typography sizes
- Add new design tokens

---

## Component Relationships

### Module 1: Setup Flow
```
app/setup/page.tsx
└── MandatoryQuestions.tsx
    ├── QuestionCard.tsx (×5)
    │   └── GoldParticles.tsx
    ├── InkWellProgress.tsx
    └── BiometricSeal.tsx
```

### Module 2: Calibration Flow
```
app/calibration/page.tsx
└── PortraitGallery.tsx
    └── RatingSlider.tsx
```

### Module 3: Assessment Flow
```
app/assessment/page.tsx
└── CardinalDrivers.tsx
    └── DriverCard.tsx (×7)
        ├── GoldParticles.tsx
        └── VerticalTube.tsx
```

---

## Quick Reference: Where to Edit

| To change... | Edit file... | Line/Section |
|-------------|-------------|--------------|
| Colors | `app/globals.css` | Lines 1-50 |
| Fonts | `app/globals.css` | Lines 71-90 |
| Spacing | `app/globals.css` | Lines 51-70 |
| Gold particle count | Component using it | `particleCount` prop |
| Spring physics | Component with motion | `stiffness`, `damping` |
| Wave animation | `InkWellProgress` or `VerticalTube` | `@keyframes liquidWave` |
| Bubble count | `VerticalTube` | `bubbles` array |
| Button styling | Individual component | `className` prop |

---

## Animation Timing Reference

| Effect | Duration | File |
|--------|----------|------|
| Gold particles | 0.8-1.2s | `GoldParticles.tsx` |
| Spring animation | ~300ms | Various (stiffness: 300) |
| Liquid wave | 2s loop | `InkWellProgress`, `VerticalTube` |
| Bubble rise | 3-5s | `VerticalTube` |
| Page transition | 0.3s | `PageTransition.tsx` |

---

## Best Practices

### When Editing Components

✅ **Do:**
- Read the component first to understand structure
- Test changes in browser immediately
- Make small, incremental changes
- Keep component focused on single responsibility

❌ **Don't:**
- Change props without updating parent components
- Remove TypeScript types
- Modify shared components without considering impact
- Over-complicate simple components

### Component Organization

✅ **Do:**
- Keep related components in same folder (e.g., `setup/`)
- Use descriptive file names
- Export one main component per file
- Document complex props with comments

❌ **Don't:**
- Mix module components in wrong folders
- Create unnecessary sub-folders
- Export multiple unrelated components from one file

---

## Next Steps

1. ✅ Read this guide to understand component structure
2. ✅ Open `app/globals.css` to see design tokens
3. ✅ Explore a simple component (e.g., `GoldParticles.tsx`)
4. ✅ Make a small change and see it in browser
5. ✅ Read `CHANGELOG_SESSIONS_1-11.md` to understand what was built
6. ✅ Experiment with Framer Motion animations

**Now you understand all 17 components!** 🎯
