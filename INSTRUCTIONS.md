# Instructions for Avery - Option 1: Fresh Design Branch

**Branch:** `claude/avery-design-option1-JtI2J`
**Purpose:** Make design changes to Harmonia's frontend
**Primary Work File:** `frontend/index.html`

---

## Quick Start

### 1. Check Out This Branch

```bash
git checkout claude/avery-design-option1-JtI2J
```

### 2. Open the HTML File

Your primary work file is:
```
frontend/index.html
```

This is a **5,820-line single-page application** with:
- Complete Harmonia design system (parchment, gold, Mediterranean blues)
- All 5 modules (Setup, Calibration, Assessment, Analysis, Results)
- Vanilla HTML/CSS/JavaScript (no build tools required)

### 3. Preview Your Changes

**Option A: Simple File Open**
```bash
# Just open in your browser
open frontend/index.html
# or
firefox frontend/index.html
```

**Option B: Local Server (recommended)**
```bash
# Using Python
cd frontend
python3 -m http.server 8000
# Visit: http://localhost:8000

# Or using Node.js
npx http-server frontend -p 8000
```

### 4. Make Design Changes

Edit `frontend/index.html` directly:
- **Lines 1-500:** CSS variables and design system
- **Lines 500-1500:** Global styles and animations
- **Lines 1500+:** HTML structure and components

### 5. Commit Your Work

```bash
git add frontend/index.html
git commit -m "Description of your design changes"
git push -u origin claude/avery-design-option1-JtI2J
```

---

## What's in This Branch

### File Structure

```
harmonia-synthesis/
├── frontend/
│   └── index.html          ← YOUR PRIMARY WORK FILE
│
├── INSTRUCTIONS.md          ← This file
├── DESIGN_SYSTEM.md         ← Color tokens, typography reference
├── OTHER_IMPLEMENTATIONS.md ← What exists on other branches
├── BRANCH_GUIDE.md          ← Master branch reference
│
├── Python backend files/
│   ├── main.py
│   ├── config.py
│   └── services/
│       ├── gemini_service.py
│       └── visual_service.py
│
└── deployment/              ← Deployment guides (ignore for design work)
```

### What You Can Edit

✅ **Safe to edit:**
- `frontend/index.html` - All design changes go here
- CSS variables (colors, spacing, typography)
- HTML structure (layout, components)
- Inline JavaScript (animations, interactions)

❌ **Do NOT edit** (unless specifically working on backend):
- `main.py` or any Python files
- `config.py`
- Files in `services/` directory
- Deployment configuration files

---

## Design System Reference

See `DESIGN_SYSTEM.md` for complete color tokens and typography.

### Quick Color Reference

```css
/* Parchment Base */
--cream: #FAF6F1
--blush: #F5EDE6
--rose: #EFE5DC
--card-bg: #F0E8DF

/* Gold Accents */
--gold: #D4A853
--gold-champagne: #E8C97A

/* Mediterranean Blues */
--navy: #1E293B
--slate: #475569

/* Maroon/Wine */
--maroon: #722F37
--wine: #8B3A3A
```

### Typography

```css
/* Headers */
font-family: 'Cormorant Garamond', serif;

/* Body Text */
font-family: 'DM Sans', sans-serif;
```

---

## Common Tasks

### Change a Color

1. Find the CSS variable in `frontend/index.html` (around lines 8-60)
2. Update the hex value
3. Save and refresh browser

Example:
```css
/* Before */
--gold: #D4A853;

/* After (warmer gold) */
--gold: #E8C97A;
```

### Modify Typography

1. Find font declarations (around lines 50-80)
2. Update font-family, size, or weight
3. Save and refresh

Example:
```css
/* Before */
h1 {
  font-size: 2.5rem;
  font-weight: 600;
}

/* After (larger, bolder) */
h1 {
  font-size: 3rem;
  font-weight: 700;
}
```

### Add New Component

1. Find the module section you want to modify (search for module names)
2. Add your HTML structure
3. Style it inline or in the `<style>` section
4. Test in browser

### Adjust Animations

1. Find CSS animations (around lines 200-400)
2. Modify timing, easing, or keyframes
3. Save and test

---

## Understanding the HTML Structure

### Module Breakdown

The `frontend/index.html` contains **5 modules**:

1. **Module 1: Setup** (Mandatory Five Questions)
   - Location: Search for `<!-- MODULE 1` or `.module-setup`
   - Features: Question cards, input fields, progress indicators

2. **Module 2: Calibration** (Portrait Rating)
   - Location: Search for `<!-- MODULE 2` or `.module-calibration`
   - Features: Portrait gallery, rating slider

3. **Module 3: Assessment** (Seven Cardinal Drivers)
   - Location: Search for `<!-- MODULE 3` or `.module-assessment`
   - Features: Driver cards, selection interface

4. **Module 4: Analysis** (Processing)
   - Location: Search for `<!-- MODULE 4` or `.module-analysis`
   - Features: Loading animations, data visualization

5. **Module 5: Results** (Compatibility Report)
   - Location: Search for `<!-- MODULE 5` or `.module-results`
   - Features: Charts, personality breakdown, match insights

### CSS Organization

```
<style>
  /* Lines 8-60: CSS Variables (Design System) */
  :root { ... }

  /* Lines 60-150: Reset & Base Styles */
  * { box-sizing: border-box; }
  body { ... }

  /* Lines 150-400: Animations & Effects */
  @keyframes fadeIn { ... }

  /* Lines 400-1500: Component Styles */
  .module-setup { ... }
  .module-calibration { ... }

  /* Lines 1500+: Responsive Design */
  @media (max-width: 768px) { ... }
</style>
```

---

## Tips for Efficient Editing

### Use Search to Navigate

Since `index.html` is 5,820 lines, use search to jump to sections:

```
Cmd+F (Mac) or Ctrl+F (Windows)

Search for:
- ":root" → CSS variables
- "--gold" → Gold color definitions
- ".module-setup" → Setup module styles
- "@keyframes" → Animation definitions
- "<!-- MODULE 1" → Module 1 HTML
```

### Use Your Editor's "Go to Line" Feature

Key sections:
- **Lines 1-60:** Design system variables
- **Lines 60-200:** Base styles
- **Lines 200-400:** Animations
- **Lines 400-1000:** Module 1 & 2 styles
- **Lines 1000-1500:** Module 3, 4, 5 styles
- **Lines 1500+:** HTML structure

### Make Small, Testable Changes

1. Change one thing at a time
2. Save and refresh browser
3. Verify it looks good
4. Commit if satisfied
5. Repeat

---

## Need More Context?

### See What Was Built on Other Branches

Read `OTHER_IMPLEMENTATIONS.md` to learn about:
- Next.js React implementation (Sessions 1-11 on merge-design branch)
- Advanced features (gold particles, liquid animations, spring physics)
- How to port features from React to vanilla HTML

### Understand the Full Project

Read `BRANCH_GUIDE.md` for:
- All branches in the repository
- What each branch contains
- How they relate to each other

---

## Getting Help

### If You Get Stuck

1. **Check documentation:**
   - `DESIGN_SYSTEM.md` - Colors, typography
   - `OTHER_IMPLEMENTATIONS.md` - Advanced features
   - `BRANCH_GUIDE.md` - Repository structure

2. **Ask in your chat instance:**
   - Describe what you're trying to change
   - Share the line numbers you're editing
   - Show error messages if any

3. **Switch branches if needed:**
   - Option 2: `claude/avery-design-option2-JtI2J` (Next.js components)
   - Option 3: `claude/avery-design-option3-JtI2J` (Hybrid with docs)

---

## Important Notes

### This Branch is Independent

- Your changes here **will not** affect other branches
- You can experiment freely without breaking anything
- Other collaborators' work is preserved on their branches

### Git Best Practices

```bash
# Before starting work
git pull origin claude/avery-design-option1-JtI2J

# After making changes
git status                    # See what you changed
git diff frontend/index.html  # Review your changes
git add frontend/index.html   # Stage changes
git commit -m "Clear message" # Commit with description
git push                      # Push to remote

# If you want to undo changes (before commit)
git checkout frontend/index.html  # Discard changes
```

### Keep Commits Focused

Good commit messages:
- ✅ "Update gold color to warmer champagne tone"
- ✅ "Increase heading font sizes for better hierarchy"
- ✅ "Add subtle shadow to question cards"

Bad commit messages:
- ❌ "Changes"
- ❌ "Update"
- ❌ "Fix stuff"

---

## Next Steps

1. ✅ Check out this branch: `git checkout claude/avery-design-option1-JtI2J`
2. ✅ Open `frontend/index.html` in your editor
3. ✅ Start a local server to preview
4. ✅ Make your first design change
5. ✅ Commit and push when satisfied

**Ready to start designing!** 🎨
