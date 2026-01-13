# SPECIFICATIONS - Branch Creation Project

**Project:** Avery Design Workspace Branches
**Repository:** PurrfectGP/harmonia-synthesis
**Date:** 2026-01-13

---

## Project Objectives

### Primary Goal
Create independent workspace branches for collaborator "Avery" to make design changes without losing the complete history and context from the original Next.js implementation (Sessions 1-11).

### Success Criteria
1. ✅ Avery can work independently on design
2. ✅ Complete history preserved in documentation
3. ✅ Multiple branch options for different skill levels
4. ✅ Migration guides for porting advanced features
5. ✅ No loss of context from original work

---

## Architecture Decisions

### Decision 1: Create 3 Separate Branches (Not 1)

**Rationale:**
- Different designers have different skill levels
- Some comfortable with HTML, others with React
- Some want simplicity, others want all features
- One-size-fits-all would compromise for everyone

**Options Created:**
1. **Option 1:** Simple HTML workspace (minimal complexity)
2. **Option 2:** Full Next.js environment (maximum features)
3. **Option 3:** Hybrid approach (HTML + comprehensive reference)

**Trade-offs:**
- **Pro:** Covers all use cases
- **Pro:** Avery can choose based on comfort level
- **Con:** More maintenance (3 branches vs 1)
- **Con:** More documentation needed

**Decision:** Worth the trade-off for flexibility

---

### Decision 2: Branch from `main` vs `quiz-design-merge`

**Option 1 & 3:** Branch from `origin/main`
- **Rationale:** Clean starting point, no Next.js complexity
- **Trade-off:** Don't include Next.js files (but Avery doesn't need them)

**Option 2:** Branch from `claude/quiz-design-merge-JtI2J`
- **Rationale:** Include all 17 React components
- **Trade-off:** Larger repo (but necessary for React work)

**Decision:** Different sources for different needs

---

### Decision 3: Preserve History via Documentation (Not Git History)

**Alternative considered:** Keep full git history
- **Pro:** Complete commit-by-commit record
- **Con:** Cluttered git log for Avery
- **Con:** Harder to navigate

**Chosen approach:** Comprehensive documentation files
- **Pro:** Clear, organized, searchable
- **Pro:** Session-by-session breakdown
- **Pro:** "Why" explained, not just "what"
- **Con:** Requires writing extensive docs

**Decision:** Documentation is clearer than raw git history

---

### Decision 4: Include Migration Guides

**Rationale:**
- Avery knows HTML but might want advanced features
- React → HTML porting is non-obvious
- Code examples reduce friction

**Implementation:**
- Step-by-step guides for each feature
- Copy-paste ready vanilla JS code
- Performance tips included
- Common pitfalls documented

**Trade-offs:**
- **Pro:** Enables feature porting without React knowledge
- **Pro:** Reduces "how do I...?" questions
- **Con:** Substantial documentation effort

**Decision:** Essential for Option 3's value proposition

---

## Technology Stack Decisions

### For Option 1 & 3: Vanilla HTML/CSS/JS

**Why:**
- ✅ No build tools required
- ✅ Familiar to most designers
- ✅ Instant preview (open in browser)
- ✅ Lightweight and fast

**Why not:**
- ❌ No component reusability
- ❌ Manual DOM updates
- ❌ No TypeScript type safety

**Decision:** Right choice for simple HTML work

---

### For Option 2: Next.js + React + TypeScript + Tailwind + Framer Motion

**Why:**
- ✅ Modern component architecture
- ✅ Hot reload (fast iteration)
- ✅ All advanced features available
- ✅ Type safety (fewer bugs)
- ✅ Already implemented (Sessions 1-11)

**Why not:**
- ❌ Build tools required (npm install)
- ❌ React learning curve
- ❌ More complex setup

**Decision:** Right choice for component-level design

---

### For Documentation: Markdown

**Why:**
- ✅ Readable as plain text
- ✅ Renders nicely on GitHub
- ✅ Supports code blocks with syntax highlighting
- ✅ Easy to search (Cmd+F)

**Why not:**
- ❌ No interactive elements
- ❌ No images (but links work)

**Decision:** Best format for technical documentation

---

## Design System Specifications

### Color Palette (Scientific Humanism Aesthetic)

**Parchment Base:**
- `--cream: #FAF6F1` - Main background
- `--blush: #F5EDE6` - Light surface
- `--rose: #EFE5DC` - Medium surface
- `--card-bg: #F0E8DF` - Card background

**Gold Accents:**
- `--gold: #D4A853` - Primary accent
- `--gold-champagne: #E8C97A` - Light gold
- `--gold-rose: #D4A574` - Rose-tinted gold

**Mediterranean Blues:**
- `--navy: #1E293B` - Primary text
- `--slate: #475569` - Secondary text
- `--blue-med: #3B5998` - Links, accents

**Rationale:**
- Warm parchment = approachable, human-centered
- Mediterranean blues = depth, intelligence
- Champagne gold = sophistication, "the spark"

---

### Typography

**Serif (Headers):** Cormorant Garamond
- **Why:** Humanist serif, warm and elegant
- **Weights:** 400, 500, 600, 700

**Sans-serif (Body):** DM Sans
- **Why:** Geometric sans, modern and clear
- **Weights:** 400, 500, 600, 700

**Rationale:**
- Contrast creates visual hierarchy
- Serif = warmth, Sans = clarity
- Both humanist in feel (not cold/mechanical)

---

### Spacing Scale

**Base unit:** 0.25rem (4px)
- **Why:** Divisible by 4 (design systems standard)
- **Range:** 1 (4px) to 24 (96px)

**Usage:**
- `spacing-4` (16px) - Default padding
- `spacing-6` (24px) - Card padding
- `spacing-8` (32px) - Section spacing

---

## Feature Implementation Specifications

### Gold Particles Effect

**Visual Metaphor:** "Data Capture"
- Particles represent data being collected
- Floating upward = data ingestion
- Dissolution = processing complete

**Technical Specs:**
- **Count:** 25-30 particles
- **Size:** 2-6px (random)
- **Duration:** 0.8-1.2s
- **Target:** Float upward 100-120px
- **Stagger:** 0-300ms delay

**Implementation:**
- **Option 1:** Not included (too complex)
- **Option 2:** Framer Motion (GoldParticles.tsx)
- **Option 3:** Vanilla JS guide provided

---

### Liquid Fill Animations

**Visual Metaphor:** "Progress in Motion"
- Static bars = boring
- Liquid = active, alive, in process

**Technical Specs:**
- **Wave:** SVG path, 2s loop
- **Bubbles:** 8 per tube, 3-5s rise time
- **Trigger:** Shows when progress > 0%

**Implementation:**
- **Option 1:** Not included
- **Option 2:** InkWellProgress, VerticalTube components
- **Option 3:** SVG + CSS guide provided

---

### Spring Physics

**Why:** More natural than linear animations
- Real-world objects don't move linearly
- Spring = responsive, alive feeling
- Users notice the difference

**Technical Specs:**
- **Stiffness:** 300 (medium, balanced)
- **Damping:** 30 (some bounce)
- **Mass:** 1 (standard weight)

**Implementation:**
- **Option 1:** Not included
- **Option 2:** Framer Motion (native support)
- **Option 3:** Cubic-bezier approximation (`cubic-bezier(0.68, -0.55, 0.27, 1.55)`)

---

## Documentation Architecture

### Principle: Layered Information

**Layer 1: Quick Start**
- INSTRUCTIONS.md - Get started in 3 steps
- Assume zero context
- Copy-paste ready commands

**Layer 2: Reference**
- DESIGN_SYSTEM.md / DESIGN_TOKENS.md - Look up colors, spacing
- COMPONENT_GUIDE.md - Component details
- Organized for scanning

**Layer 3: Context**
- CHANGELOG.md - What was built and when
- SESSION_HISTORY.md - Why decisions were made
- For understanding, not doing

**Layer 4: Migration**
- DESIGN_MIGRATION.md - How to port features
- Step-by-step with code
- Bridges React → HTML knowledge gap

---

### Principle: Progressive Disclosure

**Don't overwhelm:**
- Start simple (INSTRUCTIONS.md)
- Reference when needed (DESIGN_SYSTEM.md)
- Deep dive optional (CHANGELOG.md)

**Implementation:**
- Files named by purpose
- Clear "when to use" sections
- Cross-references minimal but present

---

### Principle: Code Over Prose

**Show, don't tell:**
```javascript
// ✅ Good
function createParticle() { /* code */ }

// ❌ Bad
"To create a particle, you write a function that..."
```

**Implementation:**
- Every feature has code example
- Copy-paste ready
- Commented for understanding

---

## Quality Standards

### Documentation Must Be:

1. **Accurate**
   - Line numbers must match
   - Commands must work
   - Code must be copy-paste ready

2. **Comprehensive**
   - Answer all likely questions
   - Provide context for decisions
   - Include troubleshooting

3. **Scannable**
   - Clear headings
   - Tables for comparison
   - Code blocks syntax highlighted

4. **Cross-referenced**
   - Link related documents
   - No dead ends
   - Clear navigation

---

### Code Examples Must Be:

1. **Complete**
   - Include all necessary parts (HTML + CSS + JS)
   - No missing dependencies
   - Ready to use

2. **Tested**
   - Actually works
   - Verified before documenting

3. **Performant**
   - Follow best practices
   - Include performance tips
   - Warn about pitfalls

---

## Branch Naming Convention

**Pattern:** `claude/[description]-JtI2J`

**Why "claude/":**
- Indicates created by Claude Code
- Separates from user branches

**Why "-JtI2J":**
- Session identifier
- Enables push permissions
- Required by git hook configuration

**Examples:**
- `claude/avery-design-option1-JtI2J`
- `claude/avery-design-option2-JtI2J`
- `claude/avery-design-option3-JtI2J`

---

## Session-Based Development

**Principle:** One major task per session
- Makes progress trackable
- Enables clear commits
- Easy to verify completion

**Session Structure:**
1. Todo update (mark in_progress)
2. Complete work
3. Create verification file
4. Commit with detailed message
5. Todo update (mark completed)

**Benefits:**
- Clear progress tracking
- Verification at each step
- Easy to resume if interrupted

---

## Verification Standards

**Each session must have:**
- Verification markdown file
- Complete checklist
- File size/line counts
- Commit hash reference
- Success criteria

**Why:**
- Proves work was done
- Documents what was created
- Enables quality review
- Helps user trust output

---

## Git Workflow Specifications

### Commits Must Include:

1. **Clear session number**
   - "Session 2: ..."
   - Easy to map to work

2. **What was created**
   - Files added
   - Lines of documentation

3. **Purpose**
   - Why this work matters
   - What it enables

**Example:**
```
Session 3: Option 2 - Next.js Components Branch

Created branch for React component design work.

Documentation (58 KB):
- NEXTJS_INSTRUCTIONS.md (12 KB)
- COMPONENT_GUIDE.md (16 KB)
- DESIGN_TOKENS.md (12 KB)
- CHANGELOG_SESSIONS_1-11.md (18 KB)

Enables Avery to work with all 17 React components.
```

---

## Success Metrics

### Quantitative:
- ✅ 3 branches created
- ✅ 168 KB documentation
- ✅ ~7,375 lines written
- ✅ 13 files across 3 branches
- ✅ All branches pushed to GitHub

### Qualitative:
- ✅ Avery can work independently
- ✅ Complete context preserved
- ✅ All skill levels accommodated
- ✅ Migration paths clear
- ✅ Design decisions documented

---

## Future Considerations

### If Expanding This Work:

1. **Add Visual Documentation**
   - Screenshots of components
   - Animated GIFs of effects
   - Before/after comparisons

2. **Interactive Elements**
   - Decision tree for branch selection
   - Interactive code playground
   - Live component previews

3. **Automated Tools**
   - Branch comparison script
   - Documentation generator
   - Validation tests

4. **Video Walkthroughs**
   - "Getting started with Option 1"
   - "Porting gold particles to HTML"
   - "Understanding the Next.js structure"

---

## Constraints & Limitations

### What We Didn't Include:

1. **Dark Mode Implementation**
   - Designed but not implemented
   - Wine black theme ready in CSS
   - Future enhancement

2. **Actual Portrait Images**
   - Using placeholders
   - Need real photos for production

3. **Backend Integration**
   - Branches focus on frontend design
   - Backend on different branch

4. **Testing**
   - No automated tests for documentation
   - Manual verification only

---

## Maintenance Strategy

### To Keep Branches Updated:

1. **If main branch changes:**
   - Cherry-pick relevant commits to Options 1 & 3
   - Update documentation if structure changes

2. **If quiz-design-merge advances:**
   - Merge to Option 2
   - Update Session 12+ documentation

3. **If Avery has questions:**
   - Add FAQ section to INSTRUCTIONS.md
   - Improve unclear documentation

---

**End of SPECIFICATIONS**

This document codifies all major decisions made during the branch creation project.
