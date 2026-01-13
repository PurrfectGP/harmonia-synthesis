# Avery's Onboarding Guide: Getting Started with Harmonia Design Branches

**Welcome!** This guide will help you get started with the Harmonia design workspace in under 10 minutes.

**Date:** 2026-01-13
**Your Options:** 3 branch options created specifically for design work

---

## Start Here: Choose Your Branch (2 minutes)

### Answer These 3 Questions

**1. Do you know React/Next.js?**
- ✅ Yes, I'm comfortable with React → **Option 2**
- ❌ No, I only know HTML/CSS/JS → Continue to Question 2

**2. Do you want to work with HTML directly?**
- ✅ Yes, just HTML/CSS → Continue to Question 3
- ❌ No, I want to learn React → **Option 2**

**3. Do you want to add advanced features (particles, animations)?**
- ✅ Yes, I want to port features to HTML → **Option 3**
- ❌ No, just basic design changes → **Option 1**

---

## Visual Decision Tree

```
START
  │
  ├─ Know React? ──YES──> Option 2 (Next.js)
  │                           ↓
  │                      (Full dev environment)
  │
  ├─ NO
  │   │
  │   ├─ Want advanced features? ──YES──> Option 3 (Hybrid)
  │   │                                       ↓
  │   │                              (HTML + migration guides)
  │   │
  │   └─ NO ──> Option 1 (Simple HTML)
  │                 ↓
  │         (Quick design changes)
```

---

## Quick Start Guides

### Option 1: Simple HTML Workspace (⭐ Easiest)

**Total Time:** 2 minutes

#### Step 1: Checkout Branch (30 seconds)
```bash
git checkout claude/avery-design-option1-JtI2J
```

#### Step 2: Open File (30 seconds)
```bash
open frontend/index.html
# Or: Right-click → Open with → Your Browser
```

#### Step 3: Read Instructions (1 minute)
```bash
open INSTRUCTIONS.md
# Read the 3-step quick start
```

#### Your First Change (5 minutes)
1. Open `frontend/index.html` in VS Code (or your editor)
2. Search for `--cream:` (line ~40)
3. Change `#FAF6F1` to `#FFF8F0` (slightly lighter)
4. Refresh browser → See the change!

#### What to Explore
- ✅ INSTRUCTIONS.md - Quick start guide
- ✅ DESIGN_SYSTEM.md - All colors, fonts, spacing
- ✅ OTHER_IMPLEMENTATIONS.md - What else was built
- ✅ BRANCH_GUIDE.md - How to switch branches

#### Common Tasks
```css
/* Change background color */
Search: "--cream:"
Edit: #FAF6F1 → #FFFCF7

/* Change heading font size */
Search: "font-size: 2.5rem"
Edit: 2.5rem → 3rem

/* Adjust spacing */
Search: "padding: var(--spacing-"
Edit: --spacing-6 → --spacing-8
```

---

### Option 2: Next.js Components (⭐⭐⭐ Most Powerful)

**Total Time:** 5 minutes

#### Step 1: Checkout Branch (30 seconds)
```bash
git checkout claude/avery-design-option2-JtI2J
```

#### Step 2: Install Dependencies (2-3 minutes)
```bash
cd harmonia-nextjs
npm install
# Wait for packages to install...
```

#### Step 3: Start Dev Server (30 seconds)
```bash
npm run dev
# Wait for "Ready" message
# Open http://localhost:3000
```

#### Step 4: Read Documentation (1 minute)
```bash
open NEXTJS_INSTRUCTIONS.md
# Read the 4-step setup
```

#### Your First Change (5 minutes)
1. Open `harmonia-nextjs/app/globals.css`
2. Find `--color-champagne-400:` (line ~12)
3. Change `#d4af37` to `#f0c86e` (brighter gold)
4. Browser auto-reloads → See the change!

#### What to Explore
- ✅ NEXTJS_INSTRUCTIONS.md - Complete Next.js guide
- ✅ COMPONENT_GUIDE.md - All 17 components explained
- ✅ DESIGN_TOKENS.md - Tailwind configuration
- ✅ CHANGELOG_SESSIONS_1-11.md - What was built and why

#### Common Tasks
```css
/* Change colors (globals.css) */
--color-champagne-400: #d4af37; → #f0c86e;

/* Adjust component spacing (any .tsx file) */
className="p-6" → className="p-8"

/* Change animation timing (QuestionCard.tsx) */
duration: 0.8 → duration: 1.2
```

---

### Option 3: Hybrid Hub (⭐⭐ Best for Learning)

**Total Time:** 3 minutes

#### Step 1: Checkout Branch (30 seconds)
```bash
git checkout claude/avery-design-option3-JtI2J
```

#### Step 2: Open Files (30 seconds)
```bash
open frontend/index.html  # In browser
open INSTRUCTIONS.md      # In editor
```

#### Step 3: Explore Documentation (2 minutes)
```bash
ls docs/
# NEXTJS_REFERENCE.md - How Next.js version works
# BRANCH_COMPARISON.md - Feature comparison
# DESIGN_MIGRATION.md - How to port features
# SESSION_HISTORY.md - Build history
```

#### Your First Change (5 minutes)
Same as Option 1 (it's HTML):
1. Open `frontend/index.html`
2. Find `--cream:` (line ~40)
3. Change color value
4. Refresh browser

#### Your First Feature Port (20 minutes)
1. Open `docs/BRANCH_COMPARISON.md`
2. Find "Gold Particles" (complexity: ⭐⭐ Medium)
3. Read "Recommended: ✅ Yes"
4. Open `docs/DESIGN_MIGRATION.md`
5. Scroll to "Gold Particles Effect"
6. Copy the vanilla JS code
7. Add to your HTML
8. Test in browser!

#### What to Explore
- ✅ INSTRUCTIONS.md - Hybrid approach explained
- ✅ docs/NEXTJS_REFERENCE.md - Complete React reference
- ✅ docs/BRANCH_COMPARISON.md - What to port
- ✅ docs/DESIGN_MIGRATION.md - How to port features
- ✅ docs/SESSION_HISTORY.md - Why decisions were made

---

## First Day Plan (1-2 hours)

### Hour 1: Get Oriented
1. **Choose your branch** (using decision tree above)
2. **Complete Quick Start** for your chosen option
3. **Make your first change** (color or spacing)
4. **Read primary documentation** (INSTRUCTIONS.md)
5. **Explore file structure** (understand what's where)

### Hour 2: First Real Task
Choose ONE task based on your branch:

**Option 1:**
- Change the color palette (cream → warmer tone)
- Adjust heading sizes (make hierarchy clearer)
- Modify spacing (more breathing room)

**Option 2:**
- Edit QuestionCard component styling
- Adjust animation timing (slower/faster)
- Modify design tokens (globals.css)

**Option 3:**
- Make an HTML change (like Option 1)
- Read one migration guide (gold particles)
- Plan which feature to port first

---

## Common Pitfalls (Avoid These!)

### For All Options

**❌ Don't:** Edit files without committing first
**✅ Do:** `git add . && git commit -m "Before changes"` before editing

**❌ Don't:** Switch branches with uncommitted changes
**✅ Do:** Commit your work first

**❌ Don't:** Edit generated files (node_modules, .next)
**✅ Do:** Edit source files only (app/, components/, frontend/)

### For Option 1 & 3 (HTML)

**❌ Don't:** Make changes to the HTML without testing in multiple browsers
**✅ Do:** Test in Chrome/Firefox/Safari

**❌ Don't:** Add inline styles everywhere
**✅ Do:** Use CSS variables from the design system

### For Option 2 (Next.js)

**❌ Don't:** Edit files while `npm run dev` is not running
**✅ Do:** Always run dev server to see changes

**❌ Don't:** Modify package.json dependencies without understanding
**✅ Do:** Ask first or reference NEXTJS_INSTRUCTIONS.md

**❌ Don't:** Delete the .next folder manually
**✅ Do:** Let Next.js manage it automatically

---

## Quick Wins (Try These First!)

### Easy Changes (5-10 minutes each)

**Change 1: Adjust Background Color**
```css
/* All Options */
Find: --cream: #FAF6F1;
Try: #FFF8F0 (lighter) or #F5F0EB (darker)
```

**Change 2: Make Headings Bigger**
```html
<!-- Option 1 & 3: HTML -->
Find: font-size: 2.5rem;
Try: 3rem;

<!-- Option 2: Next.js -->
Find: className="text-4xl"
Try: className="text-5xl"
```

**Change 3: Increase Spacing**
```html
<!-- Option 1 & 3: HTML -->
Find: padding: var(--spacing-6)
Try: var(--spacing-8)

<!-- Option 2: Next.js -->
Find: className="p-6"
Try: className="p-8"
```

**Change 4: Adjust Gold Color**
```css
/* Option 1 & 3 */
Find: --gold: #D4A853;
Try: #E8C97A (lighter) or #B8944D (darker)

/* Option 2 */
Find: --color-champagne-400: #d4af37;
Try: #f0c86e (brighter)
```

---

## When You Get Stuck

### Debugging Checklist

**1. Is the dev server running?** (Option 2 only)
```bash
# Check terminal - should see "Ready" message
# If not: npm run dev
```

**2. Did you save the file?**
- Check for unsaved indicator in editor
- Save: Cmd+S (Mac) or Ctrl+S (Windows)

**3. Did you refresh the browser?** (Options 1 & 3)
- Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)

**4. Is the syntax correct?**
- Missing semicolon? `color: red;` not `color: red`
- Missing quotes? `content: "text"` not `content: text`
- Typo in CSS variable? `--cream` not `--ceram`

**5. Are you editing the right file?**
- Option 1: `frontend/index.html`
- Option 2: `harmonia-nextjs/app/globals.css` (design tokens) or `harmonia-nextjs/components/` (components)
- Option 3: `frontend/index.html`

### Where to Find Help

**1. Documentation (Start Here)**
- INSTRUCTIONS.md - Quick start
- DESIGN_SYSTEM.md (Option 1) or DESIGN_TOKENS.md (Option 2) - Design reference
- COMPONENT_GUIDE.md (Option 2) - Component details
- FAQ section (below)

**2. Specifications (Deeper Dive)**
- SPECIFICATIONS.md - Design decisions explained
- MASTER_CHANGELOG.md - Complete history
- SESSION_HISTORY.md (Option 3) - Build context

**3. Comparison (Choose Different Branch)**
- FINAL_COMPARISON_REPORT.md - All options compared
- BRANCH_GUIDE.md - How to switch branches

---

## Frequently Asked Questions

### General Questions

**Q: Which branch should I start with?**
**A:** Use the decision tree at the top of this guide. If still unsure, start with Option 1 (simplest).

**Q: Can I switch branches later?**
**A:** Yes! Commit your work first:
```bash
git add .
git commit -m "My design changes"
git checkout claude/avery-design-option[different]-JtI2J
```

**Q: Will I lose my work if I switch branches?**
**A:** No, if you commit first. Your work stays on the branch you committed to.

**Q: How do I see what branches are available?**
**A:** Run: `git branch -a | grep "avery-design"`

**Q: What if I make a mistake?**
**A:** Git has your back:
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard all uncommitted changes
git restore .

# Go back to last commit
git reset --hard HEAD
```

### Option 1 & 3 Questions (HTML)

**Q: Where is the HTML file?**
**A:** `frontend/index.html` (5,820 lines)

**Q: How do I preview my changes?**
**A:** Open `frontend/index.html` in a browser, or use Live Server extension in VS Code.

**Q: Can I split the HTML into multiple files?**
**A:** Yes, but you'll need to manage includes manually. Documentation assumes single file.

**Q: Where are the CSS variables defined?**
**A:** In the `<style>` tag at the top of `frontend/index.html` (around line 30-100).

**Q: How do I add gold particles (Option 3)?**
**A:** Read `docs/DESIGN_MIGRATION.md` → "Gold Particles Effect" section → copy the code.

### Option 2 Questions (Next.js)

**Q: What is npm and why do I need it?**
**A:** npm is a package manager. Next.js needs it to install dependencies. Run `npm install` once, then forget about it.

**Q: The dev server won't start. What do I do?**
**A:**
1. Check if another server is running on port 3000
2. Try `npm run dev -- -p 3001` (use different port)
3. Delete `.next` folder and try again
4. Run `npm install` again

**Q: How do I stop the dev server?**
**A:** Press Ctrl+C in the terminal where `npm run dev` is running.

**Q: Where do I change colors?**
**A:** `harmonia-nextjs/app/globals.css` - edit CSS variables at the top.

**Q: Where do I edit components?**
**A:** `harmonia-nextjs/components/` folder. See COMPONENT_GUIDE.md for details.

**Q: What is TypeScript?**
**A:** JavaScript with types. You can mostly ignore the type annotations and just edit the code. NEXTJS_INSTRUCTIONS.md explains basics.

**Q: What is Tailwind?**
**A:** A CSS framework. `className="p-6 bg-cream"` = `padding: 24px; background: cream;`. See DESIGN_TOKENS.md for reference.

**Q: Hot reload isn't working.**
**A:**
1. Check dev server is running
2. Save the file (Cmd+S / Ctrl+S)
3. If still not working, restart dev server (Ctrl+C, then `npm run dev`)

### Design Questions

**Q: What colors can I use?**
**A:** See DESIGN_SYSTEM.md (Options 1 & 3) or DESIGN_TOKENS.md (Option 2) for the complete palette.

**Q: Can I change the font?**
**A:** Yes, but you'll need to update the Google Fonts import and CSS variables. Documentation shows how.

**Q: What spacing should I use?**
**A:** Use the spacing scale (4px base unit): 4px, 8px, 12px, 16px, 24px, 32px, etc. See DESIGN_SYSTEM.md.

**Q: Can I add my own components?**
**A:**
- **Option 1 & 3:** Add HTML anywhere in `frontend/index.html`
- **Option 2:** Create new `.tsx` files in `components/` folder

**Q: How do I make the design responsive?**
**A:**
- **Option 1 & 3:** Use media queries (`@media (max-width: 768px)`)
- **Option 2:** Use Tailwind responsive classes (`md:text-lg lg:text-xl`)

---

## Success Checklist (End of Day 1)

After your first session, you should have:

- ✅ Chosen a branch using the decision tree
- ✅ Successfully checked out the branch
- ✅ Made at least one design change
- ✅ Seen your change in the browser
- ✅ Read the primary INSTRUCTIONS.md file
- ✅ Committed your work with a clear message
- ✅ Explored at least 2 documentation files
- ✅ Tested 1-2 "quick wins" from this guide

**If you have all ✅ above, you're ready to work independently!**

---

## Day 2 and Beyond

### Week 1 Goals
- ✅ Make 5+ design changes successfully
- ✅ Understand the design system (colors, spacing, typography)
- ✅ Commit work regularly with clear messages
- ✅ Read all primary documentation for your branch

### Week 2 Goals
- ✅ Complete a larger design task (redesign a module)
- ✅ Experiment with different branches (if curious)
- ✅ Port 1 feature from Next.js to HTML (Option 3 only)
- ✅ Understand the "why" behind design decisions (read SPECIFICATIONS.md)

### Month 1 Goals
- ✅ Comfortable working independently
- ✅ Can switch between branches confidently
- ✅ Understand component architecture (Option 2) or feature porting (Option 3)
- ✅ Contributing design improvements regularly

---

## Advanced Topics (When You're Ready)

### Porting Features (Option 3)
1. Start with ⭐⭐ Medium complexity features
2. Read `docs/DESIGN_MIGRATION.md` completely
3. Test each feature in isolation first
4. Recommended order:
   - ⭐⭐ Gold particles (copy-paste code)
   - ⭐⭐ Liquid waves (SVG + CSS)
   - ⭐⭐ Rising bubbles (CSS animation)

### Working with Components (Option 2)
1. Read COMPONENT_GUIDE.md completely
2. Start with simple components (BiometricSeal, PageTransition)
3. Then try animated components (QuestionCard, DriverCard)
4. Finally, complex components (VerticalTube, InkWellProgress)

### Understanding the Codebase
1. Read MASTER_CHANGELOG.md (what was built in Sessions 1-11)
2. Read SPECIFICATIONS.md (why decisions were made)
3. Read SESSION_HISTORY.md (Option 3) for context
4. Explore original commits on `claude/quiz-design-merge-JtI2J` branch

---

## Resources

### Primary Documentation (Read These First)
- **This file:** AVERY_ONBOARDING_GUIDE.md
- **Option 1:** INSTRUCTIONS.md, DESIGN_SYSTEM.md
- **Option 2:** NEXTJS_INSTRUCTIONS.md, COMPONENT_GUIDE.md
- **Option 3:** INSTRUCTIONS.md, docs/BRANCH_COMPARISON.md

### Reference Documentation (When Needed)
- FINAL_COMPARISON_REPORT.md - Compare all options
- BRANCH_GUIDE.md - Navigate between branches
- DESIGN_TOKENS.md (Option 2) - Tailwind reference
- DESIGN_MIGRATION.md (Option 3) - Feature porting guides

### Context Documentation (For Understanding)
- SPECIFICATIONS.md - Why decisions were made
- MASTER_CHANGELOG.md - Complete history
- SESSION_HISTORY.md (Option 3) - Build timeline
- CHANGELOG_SESSIONS_1-11.md (Option 2) - Detailed sessions

### External Resources
- **Next.js:** https://nextjs.org/docs
- **React:** https://react.dev
- **Tailwind CSS:** https://tailwindcss.com/docs
- **Framer Motion:** https://www.framer.com/motion/
- **MDN (HTML/CSS/JS):** https://developer.mozilla.org

---

## Your Personalized Recommendation

**Based on:** You know `frontend/index.html` from main branch

**Recommended Path:**
1. **Start:** Option 1 (familiar HTML file, no new tools)
2. **First Week:** Make design changes, get comfortable
3. **Week 2-3:** Read BRANCH_GUIDE.md, explore other options
4. **Week 4+:** Try Option 3 if you want advanced features, or Option 2 if you want to learn React

**Why This Path:**
- ✅ Builds on what you already know
- ✅ No overwhelming new tools immediately
- ✅ Clear progression path
- ✅ Can upgrade when ready

---

## Final Checklist: Ready to Start?

Before you begin, make sure you have:

- ✅ Git installed (`git --version`)
- ✅ A code editor (VS Code recommended)
- ✅ A web browser (Chrome, Firefox, Safari)
- ✅ For Option 2: Node.js and npm installed (`node --version`)
- ✅ Repository cloned locally
- ✅ Read this onboarding guide
- ✅ Chosen your starting branch

**All set? Let's go!**

```bash
# Your first command:
git checkout claude/avery-design-option[1/2/3]-JtI2J

# Your second command (Option 2 only):
cd harmonia-nextjs && npm install && npm run dev

# Your second command (Options 1 & 3):
open frontend/index.html

# Now read INSTRUCTIONS.md and start creating! 🎨
```

---

**Welcome aboard, Avery!** 🎉

You have everything you need to start working on Harmonia design. Choose your branch, follow the quick start, and make your first change. The documentation has your back every step of the way.

**Questions?** Check the FAQ section or reference the appropriate documentation file for your branch.

**Happy designing!** ✨

---

**Guide Status:** ✅ Complete
**Created:** Session 10
**Last Updated:** 2026-01-13
