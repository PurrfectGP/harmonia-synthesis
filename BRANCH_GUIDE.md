# Branch Guide - Harmonia Synthesis Repository

**Repository:** `PurrfectGP/harmonia-synthesis`
**Purpose:** Complete map of all branches and what they contain

---

## Current Branch: `claude/avery-design-option1-JtI2J`

**You are here!** ⭐

**Purpose:** Clean design workspace for Avery (Option 1)
**Source:** `origin/main`
**Primary File:** `frontend/index.html`
**Technology:** Vanilla HTML/CSS/JavaScript

---

## All Branches

### 1. `main` (Production Branch)

**Status:** Stable
**Contains:**
- Python backend (Flask/FastAPI)
  - `main.py` - Main application
  - `services/gemini_service.py` - Gemini AI integration
  - `services/visual_service.py` - Image processing
- Frontend: `frontend/index.html` (5,820 lines)
- Deployment configurations (Railway, Render, Cloudflare)
- Documentation (DEPLOYMENT.md, README.md)

**Last Updated:** January 11, 2026
**Use for:** Production deployments, stable features

---

### 2. `claude/quiz-design-merge-JtI2J` (Next.js Implementation)

**Status:** Active development (11 sessions complete)
**Contains:**
- **`harmonia-nextjs/`** - Complete Next.js app
  - Next.js 16.1.1 + React 19
  - TypeScript components (17 files)
  - Tailwind CSS v4 design system
  - Framer Motion animations
  - Gold particle effects
  - Liquid fill animations with bubbles

- **`apex-match-preview/`** - Modular HTML implementation
  - Session 1-10: HTML integration work
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
**Use for:** Advanced React components, animation reference

---

### 3. `claude/fix-gemini-empty-responses-JtI2J`

**Status:** Backend fixes
**Contains:**
- Python backend improvements
- Gemini API error handling
- Visual service enhancements

**Use for:** Backend development, API fixes

---

### 4. `claude/avery-design-option1-JtI2J` ⭐ (You Are Here)

**Status:** Just created for Avery
**Contains:**
- `frontend/index.html` (clean from main)
- Comprehensive documentation:
  - INSTRUCTIONS.md - How to get started
  - DESIGN_SYSTEM.md - Colors, typography, spacing
  - OTHER_IMPLEMENTATIONS.md - What exists on other branches
  - BRANCH_GUIDE.md - This file

**Purpose:** Avery's design workspace (Option 1: Fresh start)
**Use for:** Design changes to HTML without complexity

---

### 5. `claude/avery-design-option2-JtI2J` (Coming in Session 3)

**Status:** To be created
**Will contain:**
- Full `harmonia-nextjs/` directory
- All 17 React components
- Advanced features (particles, animations)
- Next.js development environment

**Purpose:** Avery's design workspace (Option 2: Next.js components)
**Use for:** React component-level design work

---

### 6. `claude/avery-design-option3-JtI2J` (Coming in Session 4)

**Status:** To be created
**Will contain:**
- `frontend/index.html` (primary work file)
- `docs/` folder with extensive cross-references
- Migration guides for porting features
- Visual references and comparisons

**Purpose:** Avery's design workspace (Option 3: Hybrid with docs)
**Use for:** HTML design with comprehensive context

---

## Branch Relationships

```
main (stable production)
│
├── claude/fix-gemini-empty-responses-JtI2J (backend fixes)
│
├── claude/quiz-design-merge-JtI2J (Next.js + advanced features)
│   │
│   └── Sessions 1-11 complete:
│       ├── harmonia-nextjs/ (Next.js app)
│       └── apex-match-preview/ (HTML implementation)
│
└── Avery's Branches (design work):
    │
    ├── claude/avery-design-option1-JtI2J ⭐ (YOU ARE HERE)
    │   └── Clean HTML from main + documentation
    │
    ├── claude/avery-design-option2-JtI2J (coming soon)
    │   └── Next.js components from merge-design
    │
    └── claude/avery-design-option3-JtI2J (coming soon)
        └── HTML + extensive documentation
```

---

## Switching Between Branches

### Check Out Another Branch

```bash
# See all branches
git branch -a

# Switch to a branch
git checkout <branch-name>

# Example: View Next.js implementation
git checkout claude/quiz-design-merge-JtI2J

# Return to your design branch
git checkout claude/avery-design-option1-JtI2J
```

### View Changes Between Branches

```bash
# Compare your branch to main
git diff main

# Compare to Next.js implementation
git diff claude/quiz-design-merge-JtI2J

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

## What Each Branch is For

| Branch | Primary Purpose | Technology | Best For |
|--------|----------------|------------|----------|
| **main** | Production | Python + HTML | Stable deployments |
| **fix-gemini** | Backend fixes | Python | API improvements |
| **quiz-design-merge** | Advanced UI | Next.js + React | Component library |
| **avery-option1** ⭐ | Design (HTML) | Vanilla HTML/CSS | Quick design changes |
| **avery-option2** | Design (React) | Next.js | Component design |
| **avery-option3** | Design (Hybrid) | HTML + Docs | Comprehensive reference |

---

## Important Notes

### Your Branch is Safe

- Your changes on `claude/avery-design-option1-JtI2J` **will not** affect other branches
- You can experiment freely
- Other collaborators' work is preserved elsewhere

### Non-Destructive Exploration

You can switch branches to explore:

```bash
# Explore Next.js implementation
git checkout claude/quiz-design-merge-JtI2J
cd harmonia-nextjs
npm install
npm run dev

# Return to your work (your changes are preserved)
git checkout claude/avery-design-option1-JtI2J
```

Your uncommitted changes will either:
- Come with you (if files don't conflict)
- Need to be committed first (Git will warn you)

### Git Best Practices

```bash
# Before switching branches
git status                    # Check for uncommitted changes
git add frontend/index.html   # Stage your changes
git commit -m "Message"       # Commit before switching

# Now safe to switch
git checkout other-branch
```

---

## Where to Find Things

### Design Resources

- **Design System:** `DESIGN_SYSTEM.md` (on this branch)
- **Color Tokens:** `frontend/index.html` lines 8-60
- **Typography:** `DESIGN_SYSTEM.md` Typography section
- **Component Patterns:** `DESIGN_SYSTEM.md` Component Patterns

### Code References

- **HTML Structure:** `frontend/index.html` lines 1500+
- **CSS Styles:** `frontend/index.html` lines 60-1500
- **JavaScript:** `frontend/index.html` embedded `<script>` tags

### Advanced Features

- **Next.js Components:** Switch to `claude/quiz-design-merge-JtI2J`, then `harmonia-nextjs/components/`
- **Animation Examples:** `OTHER_IMPLEMENTATIONS.md` on this branch
- **Migration Guides:** `OTHER_IMPLEMENTATIONS.md` → "How to Port Features"

---

## Getting Help

### Documentation Files on This Branch

1. **INSTRUCTIONS.md** - Getting started guide
2. **DESIGN_SYSTEM.md** - Complete design reference
3. **OTHER_IMPLEMENTATIONS.md** - What's on other branches
4. **BRANCH_GUIDE.md** - This file (branch overview)

### Other Resources

- **Main README:** `git checkout main` then read `README.md`
- **Deployment Docs:** `deployment/` directory on main branch
- **Session History:** `git log` on any branch

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
git diff main..claude/quiz-design-merge-JtI2J  # Compare branches
git log --oneline --graph --all --decorate     # Visual branch tree
```

---

## Branch Status Summary

| Branch | Status | Last Updated | Files |
|--------|--------|--------------|-------|
| main | ✅ Stable | Jan 11 | Python + HTML |
| fix-gemini | ✅ Active | Recent | Python backend |
| quiz-design-merge | ✅ 11 sessions | Jan 12 | Next.js + HTML |
| avery-option1 ⭐ | 🆕 Just created | Now | HTML + docs |
| avery-option2 | 📅 Planned | Session 3 | Next.js |
| avery-option3 | 📅 Planned | Session 4 | HTML + docs |

---

**You're currently working on:** `claude/avery-design-option1-JtI2J`

**Primary file:** `frontend/index.html`

**Ready to start designing!** 🎨
