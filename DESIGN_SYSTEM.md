# Harmonia Design System

**Philosophy:** "Scientific Humanism" aesthetic
**Palette:** Warm parchment base with Mediterranean blues and champagne gold accents

---

## Color Palette

### Parchment Base (Light Mode)

```css
--cream: #FAF6F1;        /* Lightest - page background */
--blush: #F5EDE6;        /* Light surface */
--rose: #EFE5DC;         /* Medium surface */
--card-bg: #F0E8DF;      /* Card background */
```

**Usage:**
- `--cream`: Main page background, creates warm, inviting feel
- `--blush`: Section backgrounds, subtle depth
- `--rose`: Hover states, slightly darker surface
- `--card-bg`: Cards, modals, elevated components

### Gold Accents

```css
--gold: #D4A853;              /* Primary gold */
--gold-light: rgba(212, 168, 83, 0.15);  /* Translucent overlay */
--gold-champagne: #E8C97A;    /* Lighter, warmer gold */
--gold-rose: #D4A574;         /* Rose-tinted gold */
```

**Usage:**
- `--gold`: Primary accent color, CTAs, highlights
- `--gold-light`: Subtle backgrounds, hover effects
- `--gold-champagne`: Lighter accents, secondary CTAs
- `--gold-rose`: Warm highlights, special states

### Mediterranean Blues

```css
--navy: #1E293B;         /* Darkest - primary text */
--navy-med: #2C3E50;     /* Medium navy */
--slate: #475569;        /* Gray-blue - secondary text */
--blue-med: #3B5998;     /* Mediterranean blue - links */
```

**Usage:**
- `--navy`: Headings, primary text, strong contrast
- `--navy-med`: Subheadings, important secondary text
- `--slate`: Body text, descriptions, labels
- `--blue-med`: Links, interactive elements, accents

### Maroon/Wine Accents

```css
--maroon: #722F37;               /* Deep maroon */
--maroon-deep: #5C1A1B;          /* Darkest maroon */
--maroon-light: rgba(114, 47, 55, 0.12);  /* Translucent */
--wine: #8B3A3A;                 /* Wine red */
--wine-light: rgba(139, 58, 58, 0.15);    /* Translucent wine */
```

**Usage:**
- `--maroon`: Error states, important warnings
- `--maroon-deep`: Dark accents, strong contrast
- `--maroon-light`: Subtle error backgrounds
- `--wine`: Alerts, special highlights

### Dark Mode (Wine Black)

```css
[data-theme="dark"] {
  --cream: #12090A;           /* Background - wine black */
  --blush: #1A0F10;           /* Slightly lighter surface */
  --card-bg: #2D1A1C;         /* Card background */
  --dark-surface: #2D1A1C;    /* General surface */
  --dark-border: #3D2426;     /* Borders */

  --navy: #F5F0E8;            /* Text (inverted) */
  --slate: #C4B8B0;           /* Secondary text */

  --gold: #F0C86E;            /* Brighter gold for dark bg */
  --gold-champagne: #F5D98A;  /* Lighter gold */
}
```

### Neutral Grays

```css
--gray-light: #E8E0D8;   /* Light mode borders */
/* In dark mode: #2D1A1C */
```

---

## Typography

### Font Families

```css
/* Serif - Headers, Elegant Text */
font-family: 'Cormorant Garamond', serif;
/* Weights: 400 (regular), 500 (medium), 600 (semibold), 700 (bold) */

/* Sans-serif - Body, UI Text */
font-family: 'DM Sans', sans-serif;
/* Weights: 400 (regular), 500 (medium), 600 (semibold), 700 (bold) */
```

**Google Fonts Import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Font Sizes

```css
/* Headers */
h1: 2.5rem (40px)    /* Page titles */
h2: 2rem (32px)      /* Section headers */
h3: 1.5rem (24px)    /* Subsection headers */
h4: 1.25rem (20px)   /* Component headers */
h5: 1.125rem (18px)  /* Small headers */
h6: 1rem (16px)      /* Tiny headers */

/* Body */
body: 1rem (16px)         /* Standard body text */
small: 0.875rem (14px)    /* Small text, labels */
.caption: 0.75rem (12px)  /* Captions, metadata */
```

### Font Weights

```css
.light: 400      /* Regular body text */
.medium: 500     /* Slightly emphasized */
.semibold: 600   /* Subheadings, important text */
.bold: 700       /* Headlines, strong emphasis */
```

### Line Heights

```css
/* Headers */
h1-h6: 1.2       /* Tight for headers */

/* Body */
body: 1.6        /* Comfortable reading */
p: 1.75          /* Extra comfortable for paragraphs */

/* UI Elements */
buttons: 1.5     /* Balanced for UI */
labels: 1.4      /* Compact for forms */
```

---

## Spacing Scale

### Base Unit: 0.25rem (4px)

```css
--spacing-1: 0.25rem;   /* 4px */
--spacing-2: 0.5rem;    /* 8px */
--spacing-3: 0.75rem;   /* 12px */
--spacing-4: 1rem;      /* 16px - base */
--spacing-5: 1.25rem;   /* 20px */
--spacing-6: 1.5rem;    /* 24px */
--spacing-8: 2rem;      /* 32px */
--spacing-10: 2.5rem;   /* 40px */
--spacing-12: 3rem;     /* 48px */
--spacing-16: 4rem;     /* 64px */
--spacing-20: 5rem;     /* 80px */
--spacing-24: 6rem;     /* 96px */
```

### Common Usage

```css
/* Padding */
.card-padding: 2rem (32px)
.button-padding: 1rem 2rem (16px 32px)
.section-padding: 4rem 2rem (64px 32px)

/* Margin */
.element-margin-bottom: 1.5rem (24px)
.section-margin-bottom: 3rem (48px)

/* Gap */
.grid-gap: 1.5rem (24px)
.flex-gap: 1rem (16px)
```

---

## Border Radius

```css
--radius-sm: 0.25rem;    /* 4px - small elements */
--radius-md: 0.5rem;     /* 8px - cards, buttons */
--radius-lg: 1rem;       /* 16px - large cards */
--radius-xl: 1.5rem;     /* 24px - modals */
--radius-full: 9999px;   /* Fully rounded - pills, avatars */
```

---

## Shadows

### Light Mode

```css
/* Subtle elevation */
box-shadow: 0 1px 3px rgba(30, 41, 59, 0.08);

/* Card elevation */
box-shadow: 0 4px 6px rgba(30, 41, 59, 0.1);

/* Modal/Popup */
box-shadow: 0 10px 25px rgba(30, 41, 59, 0.15);

/* Strong depth */
box-shadow: 0 20px 40px rgba(30, 41, 59, 0.2);
```

### Dark Mode

```css
/* Subtle elevation */
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);

/* Card elevation */
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);

/* Modal/Popup */
box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
```

### Gold Glow (Accent)

```css
box-shadow: 0 0 20px rgba(212, 168, 83, 0.3);  /* Subtle gold glow */
box-shadow: 0 0 30px rgba(212, 168, 83, 0.5);  /* Strong gold glow */
```

---

## Animations

### Timing Functions

```css
/* Ease-out - Starts fast, ends slow (most common) */
transition-timing-function: cubic-bezier(0.33, 1, 0.68, 1);

/* Ease-in-out - Smooth start and end */
transition-timing-function: cubic-bezier(0.65, 0, 0.35, 1);

/* Bounce */
transition-timing-function: cubic-bezier(0.68, -0.55, 0.27, 1.55);
```

### Durations

```css
--duration-fast: 150ms;      /* Quick feedback */
--duration-normal: 300ms;    /* Standard transition */
--duration-slow: 500ms;      /* Dramatic effect */
--duration-slower: 800ms;    /* Page transitions */
```

### Common Animations

```css
/* Fade In */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Slide Up */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Scale In */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Pulse */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
```

---

## Component Patterns

### Buttons

```css
/* Primary Button */
.btn-primary {
  background: var(--gold);
  color: var(--navy);
  padding: 1rem 2rem;
  border-radius: var(--radius-md);
  font-weight: 600;
  transition: all 300ms ease;
}

.btn-primary:hover {
  background: var(--gold-champagne);
  box-shadow: 0 4px 12px rgba(212, 168, 83, 0.3);
  transform: translateY(-2px);
}

/* Secondary Button */
.btn-secondary {
  background: transparent;
  color: var(--navy);
  border: 2px solid var(--gold);
  padding: 1rem 2rem;
}

.btn-secondary:hover {
  background: var(--gold-light);
}
```

### Cards

```css
.card {
  background: var(--card-bg);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(30, 41, 59, 0.1);
  transition: all 300ms ease;
}

.card:hover {
  box-shadow: 0 10px 25px rgba(30, 41, 59, 0.15);
  transform: translateY(-4px);
}
```

### Inputs

```css
.input {
  background: var(--cream);
  border: 2px solid var(--gray-light);
  border-radius: var(--radius-md);
  padding: 0.75rem 1rem;
  color: var(--navy);
  font-family: 'DM Sans', sans-serif;
  transition: border-color 300ms ease;
}

.input:focus {
  border-color: var(--gold);
  outline: none;
  box-shadow: 0 0 0 3px var(--gold-light);
}
```

---

## Responsive Breakpoints

```css
/* Mobile First Approach */

/* Small devices (phones) */
@media (min-width: 640px) { /* sm */ }

/* Medium devices (tablets) */
@media (min-width: 768px) { /* md */ }

/* Large devices (desktops) */
@media (min-width: 1024px) { /* lg */ }

/* Extra large devices */
@media (min-width: 1280px) { /* xl */ }

/* 2X large devices */
@media (min-width: 1536px) { /* 2xl */ }
```

### Common Responsive Patterns

```css
/* Mobile: stack vertically */
.container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Desktop: horizontal layout */
@media (min-width: 768px) {
  .container {
    flex-direction: row;
    gap: 2rem;
  }
}
```

---

## Accessibility

### Color Contrast Ratios

All color combinations meet **WCAG AA** standards:

- Navy text on Cream background: **12.5:1** (AAA)
- Slate text on Cream background: **7.2:1** (AA)
- Gold on Navy background: **4.8:1** (AA for large text)

### Focus States

```css
*:focus-visible {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}
```

### Screen Reader Support

Use semantic HTML and ARIA labels where appropriate:
```html
<button aria-label="Submit questionnaire">Submit</button>
<nav aria-label="Main navigation">...</nav>
```

---

## Usage Examples

### Creating a New Component

```html
<div class="my-component" style="
  background: var(--card-bg);
  padding: var(--spacing-6);
  border-radius: var(--radius-lg);
  color: var(--navy);
  box-shadow: 0 4px 6px rgba(30, 41, 59, 0.1);
">
  <h3 style="
    font-family: 'Cormorant Garamond', serif;
    color: var(--navy);
    margin-bottom: var(--spacing-4);
  ">Component Title</h3>

  <p style="
    font-family: 'DM Sans', sans-serif;
    color: var(--slate);
    line-height: 1.75;
  ">Component description text</p>

  <button style="
    background: var(--gold);
    color: var(--navy);
    padding: var(--spacing-3) var(--spacing-6);
    border-radius: var(--radius-md);
    font-weight: 600;
  ">Action Button</button>
</div>
```

---

## Design Principles

1. **Warmth:** Use parchment tones to create inviting, human-centered feel
2. **Clarity:** Mediterranean blues provide crisp text contrast
3. **Elegance:** Gold accents add sophistication without overwhelming
4. **Hierarchy:** Serif headers + sans body creates clear visual hierarchy
5. **Consistency:** Use spacing scale consistently (4px base unit)
6. **Accessibility:** Always maintain AA color contrast standards
7. **Responsiveness:** Mobile-first, progressive enhancement

---

**This design system creates the "Scientific Humanism" aesthetic:** sophisticated, warm, precise, and human-centered.
