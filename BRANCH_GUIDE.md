# Branch Guide - Harmonia Synthesis Repository

**Repository:** `PurrfectGP/harmonia-synthesis`
**Purpose:** Complete map of all branches and what they contain
**Last Updated:** 2026-01-13 (All 3 Avery options created)

---

## Current Branch: `claude/avery-design-option1-JtI2J`

**You are here!** ⭐

**Purpose:** Clean HTML design workspace (Option 1)
**Source:** `origin/main`
**Primary File:** `frontend/index.html`
**Technology:** Vanilla HTML/CSS/JavaScript
**Documentation:** 42 KB (4 files)

---

## Quick Branch Selector

| Need to... | Use Branch |
|-----------|------------|
| Simple HTML design work | **Option 1** ⭐ (this branch) |
| Work with React components | **Option 2** |
| HTML work + Next.js reference | **Option 3** |
| View original work | **quiz-design-merge** |

---

## All Branches

### 1. `main` (Production Branch)

**Status:** ✅ Stable
**Contains:**
- Python backend (Flask/FastAPI)
  - `main.py` - Main application
  - `services/gemini_service.py` - Gemini AI integration
  - `services/visual_service.py` - Image processing
- Frontend: `frontend/index.html` (5,820 lines)
- Deployment configurations (Railway, Render, Cloudflare)
- Documentation (DEPLOYMENT.md, README.md)

**Use for:** Production deployments, stable features

---

### 2. `claude/quiz-design-merge-JtI2J` (Original Development Branch)

**Status:** ✅ Active (11 sessions complete)
**Contains:**
- **`harmonia-nextjs/`** - Complete Next.js app
  - Next.js 16.1.1 + React 19
  - TypeScript components (17 files)
  - Tailwind CSS v4 design system
  - Framer Motion animations
  - Gold particle effects
  - Liquid fill animations with bubbles

- **`apex-match-preview/`** - Modular HTML implementation
  - Sessions 1-10: HTML integration work
  - Comprehensive audit documents

**Sessions Completed:**
1. Next.js + Tailwind Setup
2-3. Typography & Layout
4-6. Module 1: Setup (Mandatory Five Questions)
7. Module 2: Calibration (Portrait Gallery)
8. Module 3: Assessment (Seven Cardinal Drivers)
9. Framer Motion Integration (spring physics)
10. Gold Particle Dissolution
11. Liquid Fill Animations (waves + bubbles)

**Last Commit:** `a5f63d3` - Session 11: Liquid Fill Animations Complete
**Use for:** Reference implementation, understanding what was built

---

### 3. `claude/fix-gemini-empty-responses-JtI2J`

**Status:** ✅ Backend fixes
**Contains:**
- Python backend improvements
- Gemini API error handling
- Visual service enhancements

**Use for:** Backend development, API fixes

---

## Avery's Branch Options (All Created!)

### Option 1: `claude/avery-design-option1-JtI2J` ⭐ (You Are Here)

**Status:** ✅ Created (Session 2)
**Source:** `origin/main`
**Primary File:** `frontend/index.html` (5,820 lines)
**Technology:** Vanilla HTML/CSS/JavaScript

**Documentation (42 KB):**
- `INSTRUCTIONS.md` - How to get started (8.3 KB)
- `DESIGN_SYSTEM.md` - Colors, typography, spacing (11 KB)
- `OTHER_IMPLEMENTATIONS.md` - What exists on other branches (14 KB)
- `BRANCH_GUIDE.md` - This file (8.9 KB)

**Purpose:** Clean slate for HTML design work
**Best for:**
- ✅ Quick CSS/HTML tweaks
- ✅ Working with familiar technology
- ✅ No build tools needed
- ✅ Simple, focused approach

**To use:**
```bash
git checkout claude/avery-design-option1-JtI2J
# Edit frontend/index.html
# Preview in browser
```

---

### Option 2: `claude/avery-design-option2-JtI2J`

**Status:** ✅ Created (Session 3)
**Source:** `claude/quiz-design-merge-JtI2J` (includes all Sessions 1-11)
**Primary Directory:** `harmonia-nextjs/`
**Technology:** Next.js 16.1.1 + React 19 + TypeScript + Tailwind v4 + Framer Motion

**Documentation (58 KB):**
- `NEXTJS_INSTRUCTIONS.md` - How to run Next.js (12 KB)
- `COMPONENT_GUIDE.md` - All 17 components (16 KB)
- `DESIGN_TOKENS.md` - Tailwind configuration (12 KB)
- `CHANGELOG_SESSIONS_1-11.md` - Complete build history (18 KB)

**Includes:**
- ✅ All 17 React components
- ✅ Gold particle effects
- ✅ Liquid animations (waves + bubbles)
- ✅ Spring physics
- ✅ Complete design system

**Purpose:** Component-level design with React
**Best for:**
- ✅ Working with React components
- ✅ Advanced animations (particles, springs)
- ✅ Hot reload development
- ✅ TypeScript type safety
- ✅ Modern component architecture

**To use:**
```bash
git checkout claude/avery-design-option2-JtI2J
cd harmonia-nextjs
npm install
npm run dev
# Visit http://localhost:3000
```

---

### Option 3: `claude/avery-design-option3-JtI2J`

**Status:** ✅ Created (Session 4)
**Source:** `origin/main` (same as Option 1)
**Primary File:** `frontend/index.html` (5,820 lines)
**Technology:** Vanilla HTML/CSS/JavaScript

**Documentation (68 KB):**
- `INSTRUCTIONS.md` - Hybrid approach guide (13 KB)
- `docs/NEXTJS_REFERENCE.md` - All 17 components reference (17 KB)
- `docs/BRANCH_COMPARISON.md` - Feature comparison (15 KB)
- `docs/DESIGN_MIGRATION.md` - React → HTML porting guide (14 KB)
- `docs/SESSION_HISTORY.md` - Build history summary (9.6 KB)

**Purpose:** HTML work with comprehensive Next.js reference
**Best for:**
- ✅ Working on HTML (familiar tech)
- ✅ Referencing Next.js implementation
- ✅ Porting features from React to vanilla
- ✅ Understanding full project context
- ✅ Having migration guides

**To use:**
```bash
git checkout claude/avery-design-option3-JtI2J
# Edit frontend/index.html
# Reference docs/ folder when needed
```

---

## Branch Relationships

```
main (production)
│
├── claude/fix-gemini-empty-responses-JtI2J
│   └── Python backend fixes
│
├── claude/quiz-design-merge-JtI2J
│   ├── harmonia-nextjs/ (Sessions 1-11)
│   └── apex-match-preview/
│
└── Avery's Options (All Created!)
    │
    ├── claude/avery-design-option1-JtI2J ⭐ (YOU ARE HERE)
    │   ├── frontend/index.html
    │   └── Simple HTML focus
    │
    ├── claude/avery-design-option2-JtI2J
    │   ├── harmonia-nextjs/ (all 17 components)
    │   └── React/Next.js focus
    │
    └── claude/avery-design-option3-JtI2J
        ├── frontend/index.html
        └── HTML + comprehensive Next.js docs
```

---

## Switching Between Branches

### View Another Branch

```bash
# See all branches
git branch -a

# Switch to a branch
git checkout <branch-name>

# Examples:
git checkout claude/avery-design-option2-JtI2J  # Option 2 (Next.js)
git checkout claude/avery-design-option3-JtI2J  # Option 3 (Hybrid)
git checkout claude/avery-design-option1-JtI2J  # Back to Option 1 (this)
```

### Compare Branches

```bash
# See differences between branches
git diff claude/avery-design-option1-JtI2J claude/avery-design-option2-JtI2J

# See file differences
git diff main frontend/index.html
```

### Pull Latest Changes

```bash
# Make sure you're on the right branch
git checkout claude/avery-design-option1-JtI2J

# Pull latest from remote
git pull origin claude/avery-design-option1-JtI2J
```

---

## Feature Comparison Across Options

| Feature | Option 1 ⭐ | Option 2 | Option 3 |
|---------|-----------|----------|----------|
| **Work on** | HTML | React | HTML |
| **Build required** | ❌ No | ✅ Yes (npm) | ❌ No |
| **Hot reload** | Manual | ✅ Auto | Manual |
| **Next.js reference** | Basic | ✅ Direct | ✅ Docs |
| **Migration guides** | ❌ | N/A | ✅ Yes |
| **Gold particles** | ❌ Not included | ✅ Included | 📚 Guide to port |
| **Liquid animations** | ❌ Not included | ✅ Included | 📚 Guide to port |
| **Spring physics** | ❌ Not included | ✅ Included | 📚 Approx guide |
| **Documentation** | 42 KB | 58 KB | 68 KB |
| **Complexity** | ⭐ Simple | ⭐⭐⭐ Advanced | ⭐⭐ Medium |

---

## Which Branch Should You Use?

### Stay on Option 1 (this branch) if:

✅ You want simple HTML design work
✅ Don't need advanced features (particles, springs)
✅ Prefer no build tools
✅ Want to focus on basics (colors, typography, layout)
✅ Value simplicity over features

### Switch to Option 2 if:

✅ You want to work with React components
✅ Are comfortable with Next.js/TypeScript
✅ Want all advanced features available
✅ Like hot reload development
✅ Plan to build component library

**Command:**
```bash
git checkout claude/avery-design-option2-JtI2J
cd harmonia-nextjs
npm install
npm run dev
```

### Switch to Option 3 if:

✅ You want HTML work (like Option 1)
✅ Want to reference Next.js implementation
✅ Plan to port some features to HTML
✅ Need comprehensive documentation
✅ Want full project context

**Command:**
```bash
git checkout claude/avery-design-option3-JtI2J
# Work on HTML, reference docs/ when needed
```

---

## What Each Branch Contains

### Option 1 (This Branch) ⭐

```
claude/avery-design-option1-JtI2J/
├── frontend/
│   └── index.html (5,820 lines)
│
├── INSTRUCTIONS.md
├── DESIGN_SYSTEM.md
├── OTHER_IMPLEMENTATIONS.md
├── BRANCH_GUIDE.md
│
└── Python backend/ (from main)
```

### Option 2

```
claude/avery-design-option2-JtI2J/
├── harmonia-nextjs/
│   ├── app/ (pages + globals.css)
│   ├── components/ (13 files)
│   ├── package.json
│   └── tsconfig.json
│
├── NEXTJS_INSTRUCTIONS.md
├── COMPONENT_GUIDE.md
├── DESIGN_TOKENS.md
└── CHANGELOG_SESSIONS_1-11.md
```

### Option 3

```
claude/avery-design-option3-JtI2J/
├── frontend/
│   └── index.html (5,820 lines)
│
├── docs/
│   ├── NEXTJS_REFERENCE.md
│   ├── BRANCH_COMPARISON.md
│   ├── DESIGN_MIGRATION.md
│   └── SESSION_HISTORY.md
│
├── INSTRUCTIONS.md
└── Python backend/ (from main)
```

---

## Getting Help

### Documentation on This Branch

1. **INSTRUCTIONS.md** - Getting started guide
2. **DESIGN_SYSTEM.md** - Complete design reference
3. **OTHER_IMPLEMENTATIONS.md** - What's on other branches
4. **BRANCH_GUIDE.md** - This file (branch overview)

### Documentation on Other Branches

**Option 2 (Next.js):**
- NEXTJS_INSTRUCTIONS.md - How to run Next.js
- COMPONENT_GUIDE.md - All 17 components
- DESIGN_TOKENS.md - Tailwind config
- CHANGELOG_SESSIONS_1-11.md - Complete build history

**Option 3 (Hybrid):**
- INSTRUCTIONS.md - Hybrid approach guide
- docs/NEXTJS_REFERENCE.md - Component details
- docs/BRANCH_COMPARISON.md - Feature comparison
- docs/DESIGN_MIGRATION.md - Porting guides
- docs/SESSION_HISTORY.md - Build history

---

## Quick Command Reference

```bash
# Branch operations
git branch -a                              # List all branches
git checkout <branch-name>                 # Switch branch
git checkout -b <new-branch>              # Create new branch

# See what changed
git status                                 # Current status
git diff                                   # Uncommitted changes
git log --oneline -10                     # Recent commits

# Save your work
git add <file>                            # Stage changes
git commit -m "Message"                    # Commit
git push                                   # Push to remote

# Explore branches
git diff option1..option2                  # Compare branches
git log --oneline --graph --all --decorate # Visual branch tree
```

---

## Branch Status Summary

| Branch | Status | Created | Files |
|--------|--------|---------|-------|
| main | ✅ Stable | - | Python + HTML |
| fix-gemini | ✅ Active | - | Python backend |
| quiz-design-merge | ✅ 11 sessions | Sessions 1-11 | Next.js + HTML |
| **avery-option1** ⭐ | ✅ Ready | Session 2 | HTML + docs (42 KB) |
| **avery-option2** | ✅ Ready | Session 3 | Next.js (58 KB) |
| **avery-option3** | ✅ Ready | Session 4 | HTML + docs (68 KB) |

---

## Where to Find Things

### Design Resources

- **This branch:** DESIGN_SYSTEM.md (colors, typography, spacing)
- **Option 2:** DESIGN_TOKENS.md (Tailwind configuration)
- **Option 3:** docs/BRANCH_COMPARISON.md (feature matrix)

### Code Examples

- **This branch:** OTHER_IMPLEMENTATIONS.md (basic porting examples)
- **Option 2:** COMPONENT_GUIDE.md (all 17 components with code)
- **Option 3:** docs/DESIGN_MIGRATION.md (step-by-step porting)

### Build History

- **Option 2:** CHANGELOG_SESSIONS_1-11.md (complete details)
- **Option 3:** docs/SESSION_HISTORY.md (summary)

---

**You're currently on:** `claude/avery-design-option1-JtI2J` (Option 1: Simple HTML) ⭐

**Ready to design!** 🎨
