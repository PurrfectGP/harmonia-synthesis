# Design Tokens - Tailwind CSS v4

**File:** `harmonia-nextjs/app/globals.css`
**System:** Tailwind CSS v4 with `@theme inline` directive

---

## Quick Start: Editing Design Tokens

**To change a color globally:**

1. Open `harmonia-nextjs/app/globals.css`
2. Find the token (e.g., `--color-champagne-400`)
3. Update the value
4. Save - all components using that color update instantly!

**Example:**
```css
/* Before */
--color-champagne-400: #d4af37;

/* After (brighter gold) */
--color-champagne-400: #f0c86e;
```

---

## Color System

### Parchment (Warm Paper Backgrounds)

**Purpose:** Main backgrounds, surfaces, cards
**Usage:** `bg-parchment-*`, `text-parchment-*`

```css
--color-parchment-50: #fbf9f5;    /* Lightest - page bg */
--color-parchment-100: #f5f0e6;   /* Light surface */
--color-parchment-200: #e6ddd0;   /* Medium surface */
--color-parchment-900: #2c241b;   /* Dark text */
```

**In components:**
```tsx
<div className="bg-parchment-50">         {/* Page background */}
<div className="bg-parchment-100">        {/* Card surface */}
<p className="text-parchment-900">        {/* Dark text */}
```

**RGB variants** (for opacity):
```css
--parchment-50-rgb: 251, 249, 245;
--parchment-100-rgb: 245, 240, 230;
```

**Usage:**
```tsx
<div className="bg-[rgba(var(--parchment-50-rgb),0.5)]">
{/* 50% opacity parchment */}
```

---

### Mediterranean (Primary Actions & Depth)

**Purpose:** Primary text, buttons, important elements
**Usage:** `bg-mediterranean-*`, `text-mediterranean-*`

```css
--color-mediterranean-500: #2a4e6c;  /* Primary - text, buttons */
--color-mediterranean-600: #1f3b54;  /* Darker - hover states */
```

**In components:**
```tsx
<h1 className="text-mediterranean-500">   {/* Headings */}
<button className="bg-mediterranean-500   {/* Primary button */}
         hover:bg-mediterranean-600">
```

**RGB variant:**
```css
--mediterranean-500-rgb: 42, 78, 108;
```

---

### Champagne (Gold Accents & "The Spark")

**Purpose:** Accents, highlights, CTAs, particles
**Usage:** `bg-champagne-*`, `text-champagne-*`

```css
--color-champagne-400: #d4af37;  /* Light gold - particles, hover */
--color-champagne-500: #c5a028;  /* Medium gold - accents */
--color-champagne-600: #a88b20;  /* Dark gold - pressed state */
```

**In components:**
```tsx
<div className="text-champagne-400">      {/* Gold labels */}
<button className="bg-champagne-500       {/* Gold button */}
         hover:bg-champagne-400">
```

**RGB variant:**
```css
--champagne-400-rgb: 212, 175, 55;
```

**Used for:**
- Gold particle effects (`GoldParticles.tsx`)
- Accent highlights
- Selected states
- Progress indicators

---

### Danger (Passion & Alerts)

**Purpose:** Error states, warnings, passionate highlights
**Usage:** `bg-danger-*`, `text-danger-*`

```css
--color-danger-500: #8b0000;  /* Deep burgundy red */
```

**In components:**
```tsx
<div className="text-danger-500">         {/* Error message */}
<div className="border-danger-500">       {/* Warning border */}
```

---

## Typography System

### Font Families

```css
/* Display Font - Cormorant Garamond (Humanist Serif) */
--font-serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;

/* Body Font - DM Sans (Geometric Sans) */
--font-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

**In components:**
```tsx
<h1 className="font-serif">               {/* Headings, elegant text */}
<p className="font-sans">                 {/* Body, UI text */}
```

**Fallback stack:**
- Serif: Georgia → Times New Roman → system serif
- Sans: System fonts (Apple, Windows, Linux compatibility)

---

### Font Sizes

| Class | CSS Variable | Size | Pixels | Usage |
|-------|-------------|------|--------|-------|
| `text-xs` | `--font-size-xs` | 0.75rem | 12px | Labels, captions |
| `text-sm` | `--font-size-sm` | 0.875rem | 14px | Small text |
| `text-base` | `--font-size-base` | 1rem | 16px | **Body text** |
| `text-lg` | `--font-size-lg` | 1.125rem | 18px | Large body |
| `text-xl` | `--font-size-xl` | 1.25rem | 20px | Subheadings |
| `text-2xl` | `--font-size-2xl` | 1.5rem | 24px | H3 |
| `text-3xl` | `--font-size-3xl` | 1.875rem | 30px | H2 |
| `text-4xl` | `--font-size-4xl` | 2.25rem | 36px | **H1** |
| `text-5xl` | `--font-size-5xl` | 3rem | 48px | Large titles |
| `text-6xl` | `--font-size-6xl` | 3.75rem | 60px | Hero text |

**Editing:**
```css
/* Make text-4xl larger */
--font-size-4xl: 2.5rem;  /* Instead of 2.25rem */
```

---

## Spacing Scale

**Base unit:** 0.25rem (4px)

| Class | CSS Variable | Size | Pixels |
|-------|-------------|------|--------|
| `p-1`, `m-1` | `--spacing-1` | 0.25rem | 4px |
| `p-2`, `m-2` | `--spacing-2` | 0.5rem | 8px |
| `p-3`, `m-3` | `--spacing-3` | 0.75rem | 12px |
| `p-4`, `m-4` | `--spacing-4` | 1rem | **16px** |
| `p-5`, `m-5` | `--spacing-5` | 1.25rem | 20px |
| `p-6`, `m-6` | `--spacing-6` | 1.5rem | **24px** |
| `p-8`, `m-8` | `--spacing-8` | 2rem | **32px** |
| `p-10`, `m-10` | `--spacing-10` | 2.5rem | 40px |
| `p-12`, `m-12` | `--spacing-12` | 3rem | 48px |
| `p-16`, `m-16` | `--spacing-16` | 4rem | 64px |
| `p-20`, `m-20` | `--spacing-20` | 5rem | 80px |
| `p-24`, `m-24` | `--spacing-24` | 6rem | 96px |

**Common usage:**
```tsx
<div className="p-6">                     {/* Padding: 24px all sides */}
<div className="px-8 py-4">              {/* 32px horizontal, 16px vertical */}
<div className="gap-4">                   {/* Grid/flex gap: 16px */}
<div className="mb-12">                   {/* Margin bottom: 48px */}
```

**Editing:**
```css
/* Make p-6 larger */
--spacing-6: 2rem;  /* Instead of 1.5rem (32px instead of 24px) */
```

---

## Border Radius

| Class | CSS Variable | Size | Pixels | Usage |
|-------|-------------|------|--------|-------|
| `rounded-none` | `--radius-none` | 0 | 0px | No rounding |
| `rounded-sm` | `--radius-sm` | 0.125rem | 2px | Subtle |
| `rounded` | `--radius-DEFAULT` | 0.25rem | 4px | Default |
| `rounded-md` | `--radius-md` | 0.375rem | 6px | Medium |
| `rounded-lg` | `--radius-lg` | 0.5rem | **8px** | **Cards** |
| `rounded-xl` | `--radius-xl` | 0.75rem | 12px | Large cards |
| `rounded-2xl` | `--radius-2xl` | 1rem | 16px | Modals |
| `rounded-3xl` | `--radius-3xl` | 1.5rem | 24px | Very round |
| `rounded-full` | `--radius-full` | 9999px | ∞ | Circles |

**In components:**
```tsx
<div className="rounded-lg">              {/* 8px rounded corners */}
<button className="rounded-full">         {/* Pill shape */}
<div className="rounded-t-lg">           {/* Only top corners */}
```

---

## Shadows

| Class | CSS Variable | Usage |
|-------|-------------|-------|
| `shadow-sm` | `--shadow-sm` | Subtle elevation |
| `shadow` | `--shadow-DEFAULT` | Default card shadow |
| `shadow-md` | `--shadow-md` | Medium elevation |
| `shadow-lg` | `--shadow-lg` | Large elevation |
| `shadow-xl` | `--shadow-xl` | Very large elevation |

**Shadow values:**
```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-DEFAULT: 0 1px 3px rgba(0, 0, 0, 0.1);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);
```

**In components:**
```tsx
<div className="shadow-lg">               {/* Large shadow */}
<div className="hover:shadow-xl">        {/* Shadow on hover */}
```

---

## Custom Utility Classes

### Glass Panel Effect

**File:** `globals.css` (below @theme)

```css
.glass-panel {
  background: rgba(var(--parchment-100-rgb), 0.95);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(var(--parchment-200-rgb), 0.5);
}
```

**Usage:**
```tsx
<div className="glass-panel p-6 rounded-lg">
  {/* Frosted glass effect */}
</div>
```

---

## How to Edit Design Tokens

### Change Global Color

**Goal:** Make all gold accents warmer

1. Open `harmonia-nextjs/app/globals.css`
2. Find champagne colors (lines ~21-23):
```css
--champagne-400: #d4af37;
--champagne-500: #c5a028;
--champagne-600: #a88b20;
```
3. Update to warmer values:
```css
--champagne-400: #f0c86e;  /* Warmer, brighter */
--champagne-500: #e8c97a;
--champagne-600: #d4af37;
```
4. Save - all components update automatically!

**Affects:**
- Gold particles
- Selected states
- Accent highlights
- Progress indicators

---

### Change Font Size

**Goal:** Make headings larger

1. Find font sizes (lines ~69-80)
2. Update:
```css
/* Before */
--font-size-4xl: 2.25rem;  /* 36px */

/* After */
--font-size-4xl: 2.75rem;  /* 44px */
```
3. Save - all `text-4xl` elements get larger!

---

### Adjust Spacing

**Goal:** Make card padding larger

1. Find spacing scale (lines ~82-95)
2. Update:
```css
/* Before */
--spacing-6: 1.5rem;  /* 24px */

/* After */
--spacing-6: 2rem;    /* 32px */
```
3. Save - all `p-6` padding increases!

---

## Using Design Tokens in Components

### Access via CSS Variables

```tsx
<div style={{
  color: 'var(--color-champagne-400)',
  padding: 'var(--spacing-6)'
}}>
```

### Access via Tailwind Classes (Preferred)

```tsx
<div className="text-champagne-400 p-6">
  {/* Cleaner, more maintainable */}
</div>
```

### Dynamic with Template Literals

```tsx
const isSelected = true;

<div className={`
  p-6 rounded-lg
  ${isSelected
    ? 'bg-champagne-400 text-parchment-900'
    : 'bg-parchment-100 text-mediterranean-500'
  }
`}>
```

---

## Opacity Utilities

Tailwind supports opacity via `/` syntax:

```tsx
<div className="bg-champagne-400/50">     {/* 50% opacity */}
<div className="bg-mediterranean-500/10"> {/* 10% opacity */}
```

Or use RGB variants:
```tsx
<div style={{
  background: `rgba(var(--champagne-400-rgb), 0.5)`
}}>
```

---

## Responsive Design Tokens

Tailwind breakpoints (standard):

```tsx
<div className="text-base md:text-lg lg:text-xl">
  {/*
    Mobile: 16px
    Tablet (md): 18px
    Desktop (lg): 20px
  */}
</div>
```

**Breakpoints:**
- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

---

## Best Practices

### ✅ Do:

- **Use design tokens** instead of hardcoded values
- **Edit `globals.css`** for global changes
- **Use Tailwind classes** over inline styles
- **Test changes** in browser immediately

```tsx
{/* ✅ Good */}
<div className="bg-parchment-100 text-mediterranean-500">

{/* ❌ Bad */}
<div style={{ background: '#f5f0e6', color: '#2a4e6c' }}>
```

### ❌ Don't:

- **Hardcode colors** in component styles
- **Use arbitrary values** excessively
- **Override design system** without reason
- **Mix color systems** (stay consistent)

---

## Common Combinations

### Card Style
```tsx
<div className="bg-parchment-100 p-6 rounded-lg shadow-md">
```

### Primary Button
```tsx
<button className="bg-champagne-500 hover:bg-champagne-400
                   text-parchment-50 px-8 py-3 rounded-lg
                   font-sans font-medium transition-all">
```

### Heading
```tsx
<h1 className="text-4xl font-serif text-mediterranean-500 mb-6">
```

### Body Text
```tsx
<p className="text-base font-sans text-parchment-900 leading-relaxed">
```

---

## Quick Reference Card

```
COLORS
------
Backgrounds: bg-parchment-{50,100,200}
Text:        text-mediterranean-{500,600}
             text-parchment-900
Accents:     bg-champagne-{400,500,600}
             text-champagne-{400,500,600}

TYPOGRAPHY
----------
Serif:   font-serif
Sans:    font-sans
Sizes:   text-{xs,sm,base,lg,xl,2xl,3xl,4xl,5xl,6xl}

SPACING
-------
Padding: p-{1,2,3,4,5,6,8,10,12,16,20,24}
Margin:  m-{1,2,3,4,5,6,8,10,12,16,20,24}
Gap:     gap-{1,2,3,4,5,6,8,10,12}

BORDERS
-------
Radius:  rounded-{none,sm,md,lg,xl,2xl,3xl,full}
Shadows: shadow-{sm,md,lg,xl}
```

---

## Editing Workflow

1. **Identify** what you want to change (color, spacing, etc.)
2. **Open** `harmonia-nextjs/app/globals.css`
3. **Find** the relevant token (use Cmd/Ctrl+F)
4. **Update** the value
5. **Save** file
6. **Check** browser (hot reload!)
7. **Adjust** if needed
8. **Commit** when satisfied

---

## Next Steps

1. ✅ Open `harmonia-nextjs/app/globals.css`
2. ✅ Find the `@theme inline` section (line 36)
3. ✅ Make a small change (e.g., adjust champagne-400)
4. ✅ See changes in browser instantly
5. ✅ Read COMPONENT_GUIDE.md to see how components use tokens
6. ✅ Experiment with different values

**Now you control the entire design system!** 🎨
