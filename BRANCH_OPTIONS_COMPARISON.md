# Branch Options Comparison for Avery

Quick reference guide to help choose the right branch for design work.

---

## Quick Decision Matrix

| If Avery wants to... | Use Branch | Complexity |
|---------------------|------------|------------|
| Edit the existing HTML file | **Option 1** (fresh-from-main) | ⭐ Easy |
| Learn what was built on merge-design | **Option 3** (hybrid hub) | ⭐⭐ Medium |
| Work with React components | **Option 2** (nextjs-components) | ⭐⭐⭐ Advanced |

---

## Detailed Comparison

| Feature | Option 1: Fresh | Option 2: Next.js | Option 3: Hybrid |
|---------|----------------|-------------------|------------------|
| **Branch Name** | `avery/design-fresh-from-main` | `avery/design-nextjs-components` | `avery/design-hub` |
| **Source Branch** | `origin/main` | `claude/quiz-design-merge-JtI2J` | `origin/main` + docs |
| **Technology** | Vanilla HTML/CSS/JS | Next.js + React + Tailwind | HTML + Documentation |
| **Primary File** | `frontend/index.html` | `harmonia-nextjs/app/**/*.tsx` | `frontend/index.html` |
| **Component Count** | 1 file | 17 TypeScript files | 1 file + references |
| **Setup Required** | None (open in browser) | Node.js + npm install | None (open in browser) |
| **Gold Particles** | ❌ Not included | ✅ Fully implemented | 📚 Documented for reference |
| **Liquid Animations** | ❌ Not included | ✅ Fully implemented | 📚 Documented for reference |
| **Spring Physics** | ❌ Not included | ✅ Framer Motion | 📚 Documented for reference |
| **Design System** | Basic CSS variables | Tailwind @theme | CSS variables + Tailwind docs |
| **Learning Curve** | Low | High | Low (reading) |
| **Best For** | Quick CSS tweaks | Component-level design | Understanding context |

---

## Technology Stack by Option

### Option 1: Fresh from Main
```
HTML5
├── Inline CSS (<style> tag)
├── Vanilla JavaScript
├── Google Fonts (Cormorant Garamond, DM Sans)
└── No build tools required
```

**Avery can edit:**
- Colors and typography
- Layout and spacing
- CSS animations
- Page structure

---

### Option 2: Next.js Components
```
Next.js 16.1.1
├── React 19
├── TypeScript
├── Tailwind CSS v4 (@theme directive)
├── Framer Motion (spring physics)
└── Build tools: Turbopack
```

**Avery can edit:**
- Component-level styles
- Tailwind design tokens
- Animation parameters
- React component structure

**Files to edit:**
- `harmonia-nextjs/app/globals.css` - Design system
- `harmonia-nextjs/components/**/*.tsx` - Components
- `harmonia-nextjs/app/**/page.tsx` - Pages

---

### Option 3: Hybrid Hub
```
HTML5 (working file)
├── Documentation folder
│   ├── Next.js reference docs
│   ├── Component structure maps
│   ├── Design token definitions
│   └── Session-by-session changelog
└── Cross-reference system
```

**Avery can:**
- Edit `frontend/index.html`
- Read about advanced implementations
- Port features from Next.js to HTML
- Understand full project scope

---

## File Structure Comparison

### Option 1: Fresh from Main
```
avery/design-fresh-from-main/
├── frontend/
│   └── index.html          ← PRIMARY WORK FILE
├── INSTRUCTIONS.md          ← How to get started
├── BRANCH_GUIDE.md          ← Where other work lives
├── DESIGN_SYSTEM.md         ← Color tokens, typography
└── OTHER_IMPLEMENTATIONS.md ← What exists on merge-design
```

### Option 2: Next.js Components
```
avery/design-nextjs-components/
├── harmonia-nextjs/
│   ├── app/
│   │   ├── globals.css      ← DESIGN SYSTEM
│   │   ├── page.tsx         ← Home page
│   │   ├── setup/page.tsx   ← Module 1
│   │   ├── calibration/page.tsx ← Module 2
│   │   └── assessment/page.tsx  ← Module 3
│   │
│   └── components/
│       ├── setup/
│       │   ├── QuestionCard.tsx      ← Gold particles
│       │   ├── MandatoryQuestions.tsx
│       │   ├── BiometricSeal.tsx
│       │   └── InkWellProgress.tsx   ← Liquid fill
│       │
│       ├── calibration/
│       │   ├── PortraitGallery.tsx
│       │   └── RatingSlider.tsx      ← Spring physics
│       │
│       ├── assessment/
│       │   ├── CardinalDrivers.tsx
│       │   ├── DriverCard.tsx
│       │   └── VerticalTube.tsx      ← Liquid + bubbles
│       │
│       └── effects/
│           └── GoldParticles.tsx     ← Reusable effect
│
├── NEXTJS_INSTRUCTIONS.md    ← How to run Next.js
├── COMPONENT_GUIDE.md        ← Component map
├── DESIGN_TOKENS.md          ← Tailwind config
├── CHANGELOG_SESSIONS_1-11.md ← Build history
└── SPECIFICATIONS.md         ← Design decisions
```

### Option 3: Hybrid Hub
```
avery/design-hub/
├── frontend/
│   └── index.html           ← PRIMARY WORK FILE
│
├── docs/
│   ├── NEXTJS_REFERENCE.md        ← Link to Next.js work
│   ├── BRANCH_COMPARISON.md       ← Feature comparison
│   ├── DESIGN_MIGRATION.md        ← How to port features
│   ├── SESSION_HISTORY.md         ← Complete changelog
│   └── COMPONENT_SCREENSHOTS.md   ← Visual references
│
├── INSTRUCTIONS.md           ← How to get started
└── BRANCH_GUIDE.md           ← Master branch reference
```

---

## Recommended Choice by Use Case

### Use Option 1 if Avery wants to:
- ✅ Make quick design changes to existing HTML
- ✅ Work with familiar vanilla web technologies
- ✅ Avoid learning React/Next.js
- ✅ Keep things simple and focused
- ✅ Merge changes back to main easily

### Use Option 2 if Avery wants to:
- ✅ Work with modern React components
- ✅ Edit advanced features (particles, animations)
- ✅ Leverage Tailwind design system
- ✅ Build scalable component library
- ✅ Use TypeScript for type safety

### Use Option 3 if Avery wants to:
- ✅ Understand full project scope first
- ✅ Work on HTML but reference React implementation
- ✅ Port features from Next.js to vanilla
- ✅ Have comprehensive documentation access
- ✅ See both implementations side-by-side

---

## Migration Path

If Avery starts with Option 1 or 3 and later wants to work with Next.js:

1. Read the documentation in Option 1/3
2. Switch to Option 2 branch
3. Run `npm install` in `harmonia-nextjs/`
4. Run `npm run dev`
5. Start editing components

**All options are non-destructive** - Avery can switch between them at any time.

---

## Session-by-Session Build History (for reference)

### Next.js Implementation (Sessions 1-11)

| Session | What Was Built | Key Features |
|---------|---------------|--------------|
| **1** | Next.js + Tailwind Setup | Design system foundation |
| **2-3** | Typography & Layout | Fonts, spacing, colors |
| **4-6** | Module 1: Setup | 5 Mandatory Questions, HLA processing |
| **7** | Module 2: Calibration | Portrait gallery, rating slider |
| **8** | Module 3: Assessment | 7 Cardinal Drivers |
| **9** | Framer Motion Integration | Spring physics animations |
| **10** | Gold Particle Effects | Visual data capture feedback |
| **11** | Liquid Fill Animations | Waves, bubbles, progress indicators |

### HTML Implementation (Earlier Sessions)

| Session | What Was Built | Files |
|---------|---------------|-------|
| **1-4** | HTML Foundation | CSS modules, animations, templates |
| **5-10** | DOM Integration | Added 43+ missing elements across 5 modules |

---

## Design System Tokens (consistent across all options)

### Colors
```css
/* Parchment Base */
--cream: #FAF6F1
--blush: #F5EDE6
--rose: #EFE5DC
--card-bg: #F0E8DF

/* Gold Accents */
--gold: #D4A853
--gold-champagne: #E8C97A
--gold-rose: #D4A574

/* Mediterranean Blues */
--navy: #1E293B
--slate: #475569
--blue-med: #3B5998

/* Maroon/Wine */
--maroon: #722F37
--wine: #8B3A3A
```

### Typography
```css
/* Serif (Headers) */
font-family: 'Cormorant Garamond', serif;

/* Sans-serif (Body) */
font-family: 'DM Sans', sans-serif;
```

---

## Next Step

**Choose an option and say "continue" to proceed with Session 2**

Session 2 will create the first branch option with complete documentation.
