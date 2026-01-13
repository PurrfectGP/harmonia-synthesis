# Next.js Instructions for Avery - Option 2

**Branch:** `claude/avery-design-option2-JtI2J`
**Purpose:** Design work with React components and advanced features
**Primary Directory:** `harmonia-nextjs/`

---

## Quick Start

### 1. Check Out This Branch

```bash
git checkout claude/avery-design-option2-JtI2J
```

### 2. Navigate to Next.js Directory

```bash
cd harmonia-nextjs
```

### 3. Install Dependencies (First Time Only)

```bash
npm install
```

This installs:
- Next.js 16.1.1
- React 19
- TypeScript
- Tailwind CSS v4
- Framer Motion (animations)

**Time:** ~2-3 minutes

### 4. Start Development Server

```bash
npm run dev
```

**Output:**
```
▲ Next.js 16.1.1
- Local:        http://localhost:3000
- Network:      http://[your-ip]:3000

✓ Starting...
✓ Ready in 2.1s
```

**Open browser:** http://localhost:3000

---

## What You Can Edit

### Design System (Colors, Typography, Spacing)

**File:** `app/globals.css`
**Lines:** 1-100 (design tokens)

```css
@theme {
  /* Colors - Edit these! */
  --color-cream: #FAF6F1;
  --color-gold: #D4A853;
  --color-navy: #1E293B;

  /* Spacing */
  --spacing-1: 0.25rem;
  --spacing-4: 1rem;

  /* Typography */
  --font-serif: 'Cormorant Garamond', serif;
  --font-sans: 'DM Sans', sans-serif;
}
```

**Hot reload:** Changes appear instantly in browser!

### Pages (Module Layouts)

**Files:**
- `app/page.tsx` - Home/Dashboard
- `app/setup/page.tsx` - Module 1: Mandatory Five Questions
- `app/calibration/page.tsx` - Module 2: Portrait Rating
- `app/assessment/page.tsx` - Module 3: Seven Cardinal Drivers

**Edit to:**
- Change page layouts
- Modify module structure
- Adjust spacing and composition

### Components (Individual UI Elements)

**Files:** See COMPONENT_GUIDE.md for detailed map

**Edit to:**
- Style individual components
- Modify animations
- Change interactions
- Adjust visual effects

---

## File Structure

```
harmonia-nextjs/
├── app/                      ← Pages and layouts
│   ├── globals.css           ← DESIGN SYSTEM (edit here!)
│   ├── layout.tsx            ← Root layout
│   ├── page.tsx              ← Home page
│   ├── setup/page.tsx        ← Module 1
│   ├── calibration/page.tsx  ← Module 2
│   └── assessment/page.tsx   ← Module 3
│
├── components/               ← Reusable UI components
│   ├── PageTransition.tsx    ← Page animations
│   │
│   ├── setup/                ← Module 1 components
│   │   ├── QuestionCard.tsx
│   │   ├── MandatoryQuestions.tsx
│   │   ├── BiometricSeal.tsx
│   │   └── InkWellProgress.tsx
│   │
│   ├── calibration/          ← Module 2 components
│   │   ├── PortraitGallery.tsx
│   │   └── RatingSlider.tsx
│   │
│   ├── assessment/           ← Module 3 components
│   │   ├── CardinalDrivers.tsx
│   │   ├── DriverCard.tsx
│   │   └── VerticalTube.tsx
│   │
│   └── effects/              ← Visual effects
│       └── GoldParticles.tsx
│
├── public/                   ← Static assets (images, etc.)
├── package.json              ← Dependencies
└── tsconfig.json             ← TypeScript config
```

---

## Common Tasks

### Change a Color

1. Open `app/globals.css`
2. Find the color variable (e.g., `--color-gold: #D4A853;`)
3. Change the hex value
4. Save - browser updates automatically!

**Example:**
```css
/* Before */
--color-gold: #D4A853;

/* After (warmer) */
--color-gold: #E8C97A;
```

### Modify Component Styling

1. Open component file (e.g., `components/setup/QuestionCard.tsx`)
2. Find the `className` prop
3. Modify Tailwind classes
4. Save - browser updates!

**Example:**
```tsx
{/* Before */}
<div className="bg-card-bg p-6 rounded-lg">

{/* After (larger padding, more rounded) */}
<div className="bg-card-bg p-8 rounded-xl">
```

### Adjust Animation Timing

1. Open component with animation (e.g., `components/effects/GoldParticles.tsx`)
2. Find `transition` prop in `<motion.div>`
3. Modify duration or delay
4. Save and test!

**Example:**
```tsx
{/* Before */}
transition={{ duration: 0.8 }}

{/* After (slower) */}
transition={{ duration: 1.2 }}
```

### Change Typography

1. Open `app/globals.css`
2. Modify font size classes
3. Save - all components using that class update!

**Example:**
```css
/* Before */
.text-lg { font-size: 1.125rem; }

/* After (larger) */
.text-lg { font-size: 1.25rem; }
```

---

## Understanding React Components

### Basic Component Structure

```tsx
// Import React and types
import React from 'react';

// Define props (inputs to component)
interface QuestionCardProps {
  question: string;
  answer: string;
  onChange: (value: string) => void;
}

// Component function
export default function QuestionCard({
  question,
  answer,
  onChange
}: QuestionCardProps) {
  return (
    <div className="bg-card-bg p-6 rounded-lg">
      <h3 className="text-navy font-serif text-xl">
        {question}
      </h3>
      <input
        value={answer}
        onChange={(e) => onChange(e.target.value)}
        className="w-full p-3 border border-gray-light rounded"
      />
    </div>
  );
}
```

### Key Concepts

**Props:** Data passed into component
```tsx
<QuestionCard question="What is your age?" />
//           ^^^^^^^^ This is a prop
```

**State:** Data that changes
```tsx
const [answer, setAnswer] = useState('');
//     ^^^^^^ current value
//             ^^^^^^^^^ function to update
```

**className:** CSS classes (Tailwind)
```tsx
<div className="bg-cream p-4 rounded-lg">
//   ^^^^^^^^^^ Tailwind classes
```

---

## Working with Framer Motion

### Basic Animation

```tsx
import { motion } from 'framer-motion';

<motion.div
  initial={{ opacity: 0 }}     // Start state
  animate={{ opacity: 1 }}     // End state
  transition={{ duration: 0.5 }} // Timing
>
  Content
</motion.div>
```

### Spring Physics

```tsx
<motion.div
  animate={{ scale: 1.05 }}
  transition={{
    type: "spring",
    stiffness: 300,  // Higher = bouncier
    damping: 30      // Higher = less bounce
  }}
>
  Bouncy element
</motion.div>
```

### Common Properties

```tsx
{/* Fade in */}
initial={{ opacity: 0 }}
animate={{ opacity: 1 }}

{/* Slide up */}
initial={{ y: 20 }}
animate={{ y: 0 }}

{/* Scale */}
initial={{ scale: 0.9 }}
animate={{ scale: 1 }}

{/* Rotate */}
initial={{ rotate: -10 }}
animate={{ rotate: 0 }}
```

---

## Tailwind CSS Classes

### Layout

```tsx
{/* Flexbox */}
<div className="flex flex-col gap-4">
<div className="flex flex-row justify-between items-center">

{/* Grid */}
<div className="grid grid-cols-3 gap-6">

{/* Spacing */}
<div className="p-4 m-2">        {/* padding 4, margin 2 */}
<div className="px-6 py-4">      {/* horizontal 6, vertical 4 */}
```

### Colors

```tsx
{/* Background */}
<div className="bg-cream">
<div className="bg-gold">

{/* Text */}
<p className="text-navy">
<p className="text-slate">

{/* Border */}
<div className="border border-gold">
```

### Typography

```tsx
{/* Font family */}
<h1 className="font-serif">      {/* Cormorant Garamond */}
<p className="font-sans">         {/* DM Sans */}

{/* Size */}
<h1 className="text-4xl">
<p className="text-base">

{/* Weight */}
<span className="font-bold">
<span className="font-medium">
```

### Effects

```tsx
{/* Shadows */}
<div className="shadow-lg">

{/* Rounded corners */}
<div className="rounded-lg">

{/* Opacity */}
<div className="opacity-50">

{/* Transitions */}
<div className="transition-all duration-300">
```

---

## Development Workflow

### 1. Start Dev Server

```bash
cd harmonia-nextjs
npm run dev
```

Keep this running while you work!

### 2. Edit Files

- Use your code editor (VS Code, WebStorm, etc.)
- Make changes to `.tsx` or `.css` files
- Save file

### 3. View Changes

- Browser automatically refreshes
- See your changes instantly
- No manual reload needed!

### 4. Commit When Satisfied

```bash
git status
git add harmonia-nextjs/
git commit -m "Update gold color to warmer tone"
git push
```

---

## Troubleshooting

### Server Won't Start

**Error:** `Cannot find module 'next'`
```bash
# Solution: Install dependencies
npm install
```

**Error:** `Port 3000 already in use`
```bash
# Solution: Use different port
npm run dev -- -p 3001

# Or kill process on port 3000
lsof -ti:3000 | xargs kill
```

### Changes Not Appearing

1. Check dev server is running (`npm run dev`)
2. Hard refresh browser (Cmd+Shift+R or Ctrl+Shift+R)
3. Check for errors in terminal
4. Check browser console (F12)

### TypeScript Errors

**Red squiggles in editor:**
- Often auto-fixable by saving file
- Check for typos in variable names
- Make sure props match interface

**Build errors:**
```bash
# Check all errors
npm run build

# Fix errors, then restart dev server
npm run dev
```

### Git Conflicts

```bash
# If you get conflicts when pulling
git stash              # Save your changes
git pull               # Get latest
git stash pop          # Restore your changes
# Resolve conflicts manually
```

---

## Best Practices

### File Organization

✅ **Do:**
- Keep component files focused (one component per file)
- Use descriptive names (`QuestionCard.tsx`, not `Card.tsx`)
- Group related components in folders (`setup/`, `calibration/`)

❌ **Don't:**
- Put multiple components in one file
- Use generic names that could mean anything
- Mix different module components in same folder

### Styling

✅ **Do:**
- Use Tailwind classes for consistency
- Edit design tokens in `globals.css` for global changes
- Use component-specific classes for unique styling

❌ **Don't:**
- Write inline styles (`style={{...}}`) unless necessary
- Duplicate color hex values (use design tokens)
- Override Tailwind with custom CSS unless needed

### State Management

✅ **Do:**
- Keep state as local as possible
- Use `useState` for simple state
- Pass props down from parent components

❌ **Don't:**
- Over-complicate state management
- Store everything in top-level component
- Mutate state directly (always use setState)

### Commits

✅ **Do:**
- Commit working changes
- Write clear commit messages
- Test before committing

❌ **Don't:**
- Commit broken code
- Make giant commits with many changes
- Commit `node_modules/` or `.next/`

---

## Keyboard Shortcuts (VS Code)

```
Cmd/Ctrl + P       → Quick file open
Cmd/Ctrl + Shift + F → Search in all files
Cmd/Ctrl + D       → Select next occurrence
Cmd/Ctrl + /       → Comment/uncomment
Cmd/Ctrl + B       → Toggle sidebar
F2                 → Rename symbol
```

---

## Resources

### Documentation in This Repo

- **COMPONENT_GUIDE.md** - Detailed component map
- **DESIGN_TOKENS.md** - Tailwind configuration
- **CHANGELOG_SESSIONS_1-11.md** - What was built and why
- **BRANCH_GUIDE.md** - Repository navigation

### External Resources

- **Next.js Docs:** https://nextjs.org/docs
- **React Docs:** https://react.dev
- **Tailwind CSS:** https://tailwindcss.com/docs
- **Framer Motion:** https://www.framer.com/motion/

---

## Quick Command Reference

```bash
# Development
npm run dev          # Start dev server
npm run build        # Build for production
npm run lint         # Check for errors

# Git
git status           # See changed files
git add .            # Stage all changes
git commit -m "msg"  # Commit changes
git push             # Push to remote

# Navigation
cd harmonia-nextjs   # Enter project
cd ..                # Go up one level
pwd                  # Show current directory
```

---

## Next Steps

1. ✅ Check out this branch
2. ✅ Run `npm install` in `harmonia-nextjs/`
3. ✅ Run `npm run dev`
4. ✅ Open http://localhost:3000
5. ✅ Make your first change to `app/globals.css`
6. ✅ See it update in browser!
7. ✅ Explore components in COMPONENT_GUIDE.md
8. ✅ Read session history in CHANGELOG_SESSIONS_1-11.md

**Ready to build with React!** 🚀
