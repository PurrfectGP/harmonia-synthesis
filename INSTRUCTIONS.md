# Instructions for Avery - Option 3: Hybrid Documentation Hub

**Branch:** `claude/avery-design-option3-JtI2J`
**Purpose:** HTML design work with comprehensive Next.js reference
**Primary Work File:** `frontend/index.html`

---

## Quick Start

### 1. Check Out This Branch

```bash
git checkout claude/avery-design-option3-JtI2J
```

### 2. Open Your Work File

Your primary work file is:
```
frontend/index.html
```

This is a **5,820-line single-page application** (same as Option 1).

### 3. Preview Your Changes

```bash
# Simple: open in browser
open frontend/index.html

# Or use local server (recommended)
cd frontend
python3 -m http.server 8000
# Visit: http://localhost:8000
```

### 4. Explore the Documentation

```
docs/
├── NEXTJS_REFERENCE.md        ← What exists on Next.js branch
├── BRANCH_COMPARISON.md       ← Feature-by-feature comparison
├── DESIGN_MIGRATION.md        ← How to port React → HTML
└── SESSION_HISTORY.md         ← Complete build history (Sessions 1-11)
```

---

## What Makes This Option Different?

### Option 1: Fresh Start
- ✅ Simple HTML work
- ❌ No Next.js context

### Option 2: Next.js Components
- ✅ All advanced features
- ❌ Requires React knowledge

### Option 3: Hybrid Hub (You Are Here) ⭐
- ✅ **Simple HTML work** (like Option 1)
- ✅ **Complete Next.js reference** (can see what was built)
- ✅ **Migration guides** (port features from React to HTML)
- ✅ **Full context** (understand entire project)

**Best for:**
- Working on HTML but wanting to reference advanced implementations
- Understanding the full project scope before choosing approach
- Porting features from Next.js to vanilla HTML
- Having comprehensive documentation access

---

## Your Workflow

### 1. Edit HTML (Primary Work)

```bash
# Open in your editor
code frontend/index.html

# Or vim, emacs, whatever you prefer
```

**Make changes:**
- CSS variables (lines 8-60)
- HTML structure (lines 1500+)
- JavaScript (embedded `<script>` tags)

### 2. Reference Next.js Implementation (When Needed)

Want to see how gold particles work in React?

1. Open `docs/NEXTJS_REFERENCE.md`
2. Find the GoldParticles section
3. See code examples
4. Read `docs/DESIGN_MIGRATION.md` for porting guide
5. Implement in your HTML

### 3. Compare Approaches

Not sure which feature to port?

1. Open `docs/BRANCH_COMPARISON.md`
2. See side-by-side comparison
3. Decide what makes sense for HTML
4. Implement or skip based on complexity

### 4. Understand Build History

Want to know why a decision was made?

1. Open `docs/SESSION_HISTORY.md`
2. Read session-by-session breakdown
3. Understand rationale ("why spring physics?", "why gold particles?")

---

## File Structure

```
claude/avery-design-option3-JtI2J/
├── frontend/
│   └── index.html               ← YOUR PRIMARY WORK FILE
│
├── docs/                        ← REFERENCE DOCUMENTATION
│   ├── NEXTJS_REFERENCE.md      ← What exists on Next.js branch
│   ├── BRANCH_COMPARISON.md     ← Feature comparison
│   ├── DESIGN_MIGRATION.md      ← How to port React → HTML
│   └── SESSION_HISTORY.md       ← Sessions 1-11 history
│
├── INSTRUCTIONS.md              ← This file
│
├── Python backend files/        ← Backend (ignore for design work)
│   ├── main.py
│   ├── config.py
│   └── services/
│
└── deployment/                  ← Deployment guides (ignore)
```

---

## Documentation Guide

### 1. NEXTJS_REFERENCE.md (What Exists on Other Branch)

**Use when:**
- You want to see what was built on the Next.js branch
- You're curious about advanced features (particles, animations)
- You need to understand component structure

**Contains:**
- All 17 React components documented
- Props interfaces
- Features list for each component
- Line number references
- Code examples

**Example use case:**
> "I want to add gold particles when user answers a question. Let me check NEXTJS_REFERENCE.md to see how it was done in React, then read DESIGN_MIGRATION.md to port it to vanilla HTML."

---

### 2. BRANCH_COMPARISON.md (Side-by-Side Features)

**Use when:**
- You want to see what features exist in each implementation
- You're deciding what to port to HTML
- You want to understand technology differences

**Contains:**
- Feature matrix (HTML vs Next.js)
- Complexity ratings
- Implementation status
- Recommended approach for each feature

**Example use case:**
> "I want to know if spring physics makes sense for HTML. Let me check BRANCH_COMPARISON.md to see the complexity and alternatives."

---

### 3. DESIGN_MIGRATION.md (How to Port React → HTML)

**Use when:**
- You want to implement a Next.js feature in HTML
- You need code examples for vanilla JS equivalents
- You want to understand conversion strategies

**Contains:**
- Step-by-step porting guides
- React code → HTML/JS conversion examples
- Framer Motion → CSS/JS alternatives
- Tailwind classes → CSS equivalents
- When to use libraries vs native

**Example use case:**
> "I want to add liquid wave animations from the Next.js version. Let me read DESIGN_MIGRATION.md to see the SVG/CSS implementation."

---

### 4. SESSION_HISTORY.md (Complete Build History)

**Use when:**
- You want to understand what was built and when
- You need to know why decisions were made
- You want complete context on the project

**Contains:**
- Sessions 1-11 detailed breakdown
- Commit hashes for each session
- Design decisions explained
- Technology choices justified
- Visual metaphors documented

**Example use case:**
> "Why were gold particles added? Let me check SESSION_HISTORY.md to understand the 'data capture' visual metaphor."

---

## Common Tasks

### Change a Color Globally

1. Open `frontend/index.html`
2. Find CSS variables (lines 8-60)
3. Update color hex value
4. Save and refresh browser

```css
/* Before */
--gold: #D4A853;

/* After (warmer) */
--gold: #E8C97A;
```

**Affects:** All elements using `var(--gold)`

---

### Add Gold Particles Effect

1. **Research:** Open `docs/NEXTJS_REFERENCE.md`
   - Read GoldParticles component section
   - See how it works in React

2. **Migration:** Open `docs/DESIGN_MIGRATION.md`
   - Find "Gold Particles" section
   - Copy vanilla JavaScript implementation

3. **Implement:** In `frontend/index.html`
   ```javascript
   function createGoldParticles(element) {
     const count = 25;
     for (let i = 0; i < count; i++) {
       const particle = document.createElement('div');
       particle.className = 'gold-particle';
       // ... (see DESIGN_MIGRATION.md for full code)
     }
   }
   ```

4. **Style:** Add CSS
   ```css
   .gold-particle {
     position: absolute;
     width: 4px;
     height: 4px;
     background: var(--gold);
     border-radius: 50%;
     animation: particleFloat 1s ease-out forwards;
   }

   @keyframes particleFloat {
     to {
       transform: translateY(-100px);
       opacity: 0;
     }
   }
   ```

5. **Trigger:** Call function when user answers question
   ```javascript
   questionButton.addEventListener('click', function() {
     createGoldParticles(this);
     // ... handle answer
   });
   ```

---

### Add Liquid Wave Animation

1. **Reference:** Check `docs/NEXTJS_REFERENCE.md`
   - InkWellProgress component
   - VerticalTube component
   - See wave implementations

2. **Migration:** Check `docs/DESIGN_MIGRATION.md`
   - Find "Liquid Wave Animation" section
   - Get SVG path code

3. **Implement:** Add SVG to progress bar
   ```html
   <div class="progress-bar">
     <div class="liquid-fill" style="width: 75%">
       <svg class="wave" viewBox="0 0 100 10">
         <path d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
               fill="var(--gold)"
               opacity="0.6" />
       </svg>
     </div>
   </div>
   ```

4. **Animate:** Add CSS animation
   ```css
   .wave {
     animation: liquidWave 2s ease-in-out infinite;
   }

   @keyframes liquidWave {
     0%, 100% { transform: translateX(0); }
     50% { transform: translateX(-20px); }
   }
   ```

---

### Compare Features Before Implementing

1. Open `docs/BRANCH_COMPARISON.md`
2. Find the feature in the table
3. Check complexity rating
4. See "Recommended for HTML" column
5. Decide whether to implement

**Example:**

| Feature | HTML Complexity | Next.js | Recommended for HTML? |
|---------|----------------|---------|----------------------|
| Color changes | ⭐ Easy | ⭐ Easy | ✅ Yes, use CSS variables |
| Gold particles | ⭐⭐ Medium | ⭐ Easy | ✅ Yes, vanilla JS works well |
| Spring physics | ⭐⭐⭐ Hard | ⭐ Easy | ⚠️ Use CSS cubic-bezier instead |
| Liquid waves | ⭐⭐ Medium | ⭐ Easy | ✅ Yes, SVG + CSS animation |
| Bubbles | ⭐⭐ Medium | ⭐ Easy | ✅ Yes, CSS animation works |

---

## Decision Matrix: When to Use Each Branch

### Use This Branch (Option 3) if you:

✅ Want to work on HTML (familiar technology)
✅ Want to reference advanced Next.js features
✅ Plan to port some (not all) features to HTML
✅ Need full project context before choosing
✅ Like comprehensive documentation

### Switch to Option 1 if you:

✅ Only want HTML work, no Next.js references needed
✅ Prefer simpler documentation (less overwhelming)
✅ Don't plan to port any advanced features

### Switch to Option 2 if you:

✅ Want to work with React components directly
✅ Are comfortable with Next.js/TypeScript
✅ Want all advanced features available
✅ Prefer modern component architecture

---

## Switching Branches

You can switch between options anytime:

```bash
# To Option 1 (HTML only)
git checkout claude/avery-design-option1-JtI2J

# To Option 2 (Next.js)
git checkout claude/avery-design-option2-JtI2J

# Back to Option 3 (Hybrid)
git checkout claude/avery-design-option3-JtI2J
```

**Your uncommitted changes:**
- Will follow you if files don't conflict
- Need to be committed first if files conflict (Git will warn you)

---

## Best Practices

### Reading Order

**First time:**
1. This file (INSTRUCTIONS.md) - 10 min
2. `docs/BRANCH_COMPARISON.md` - 5 min to see what exists
3. Start editing `frontend/index.html`
4. Reference other docs as needed

**When porting a feature:**
1. `docs/NEXTJS_REFERENCE.md` - See how it works in React
2. `docs/DESIGN_MIGRATION.md` - Get vanilla JS equivalent
3. Implement in your HTML
4. Test in browser

**When understanding context:**
1. `docs/SESSION_HISTORY.md` - See what was built and why
2. `docs/BRANCH_COMPARISON.md` - Compare approaches

### Git Workflow

```bash
# Before starting work
git pull origin claude/avery-design-option3-JtI2J

# After making changes
git status
git diff frontend/index.html    # Review your changes
git add frontend/index.html
git commit -m "Add gold particle effect to question cards"
git push
```

### Documentation Workflow

```
Want to add feature
       ↓
Check BRANCH_COMPARISON.md
       ↓
Is it recommended for HTML?
       ↓ Yes
Check NEXTJS_REFERENCE.md (see how it works)
       ↓
Check DESIGN_MIGRATION.md (get vanilla code)
       ↓
Implement in frontend/index.html
       ↓
Test in browser
       ↓
Commit!
```

---

## Getting Help

### Documentation Files

**In this branch:**
- `INSTRUCTIONS.md` - This file (getting started)
- `docs/NEXTJS_REFERENCE.md` - Next.js implementation details
- `docs/BRANCH_COMPARISON.md` - Feature comparison
- `docs/DESIGN_MIGRATION.md` - Porting guide
- `docs/SESSION_HISTORY.md` - Build history

**In Option 1 branch:**
- `DESIGN_SYSTEM.md` - Color tokens, typography
- `OTHER_IMPLEMENTATIONS.md` - Context from other branches

**In Option 2 branch:**
- `NEXTJS_INSTRUCTIONS.md` - How to run Next.js
- `COMPONENT_GUIDE.md` - All 17 components
- `DESIGN_TOKENS.md` - Tailwind configuration

### Ask in Your Chat

If stuck:
1. Describe what you're trying to do
2. Share which documentation you've read
3. Show the code you've tried
4. Ask specific questions

---

## Next Steps

1. ✅ Check out this branch
2. ✅ Read `docs/BRANCH_COMPARISON.md` (5 min)
3. ✅ Open `frontend/index.html` in editor
4. ✅ Make a small change (e.g., color tweak)
5. ✅ Preview in browser
6. ✅ Commit your change
7. ✅ Explore a feature in `docs/NEXTJS_REFERENCE.md`
8. ✅ Try porting a simple feature using `docs/DESIGN_MIGRATION.md`

**Ready to design with full context!** 🎨
