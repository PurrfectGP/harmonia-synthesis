# MASTER FIX INSTRUCTIONS - Complete Specification Implementation

**CRITICAL:** This document lists EVERY fix needed to match the specifications EXACTLY.
**Status:** AWAITING USER APPROVAL TO PROCEED

---

## 📋 **EXECUTION STRATEGY**

### Phase 1: Foundation (Design System)
### Phase 2: Content Population (All Text/Questions/Images)
### Phase 3: Advanced Animations (Framer Motion/Particles)
### Phase 4: Data Visualization (Recharts Charts)
### Phase 5: Polish & Validation

---

## **PHASE 1: DESIGN SYSTEM FOUNDATION** (Sessions 1-3)

### SESSION 1: Paper Grain Texture & Glassmorphism

**Research Required:**
- [CSS-Tricks - Grainy Gradients](https://css-tricks.com/grainy-gradients/)
- [freeCodeCamp - SVG Filters for Grainy Backgrounds](https://www.freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters/)
- [Codrops - feTurbulence Texture](https://tympanus.net/codrops/2019/02/19/svg-filter-effects-creating-texture-with-feturbulence/)

**Actions:**
1. Create SVG filter in assets/svg/paper-grain.svg with feTurbulence
   - baseFrequency="0.9"
   - numOctaves="4"
   - opacity="0.035"
2. Apply filter to body background in CSS
3. Create `.bg-parchment-texture` utility class
4. Create `.glass-panel` utility:
   ```css
   .glass-panel {
     background: rgba(245, 240, 230, 0.9);
     backdrop-filter: blur(12px);
     border: 1px solid rgba(212, 175, 55, 0.3);
     box-shadow: 0 10px 15px -3px rgba(42, 78, 108, 0.1);
   }
   ```

**Expected Outcome:** Pages have tactile paper feel, cards have depth

---

### SESSION 2: Blue-Tinted Shadows & Gold Borders

**Research Required:**
- [MDN - box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)
- Custom shadow color techniques

**Actions:**
1. Update ALL shadow declarations in CSS to use Mediterranean Blue tint:
   - Find all `box-shadow` instances
   - Replace grey shadows with `rgba(42, 78, 108, 0.1)`
2. Add gold borders to all cards:
   ```css
   border: 1px solid rgba(212, 175, 55, 0.3);
   ```
3. Update setup-card, calibration-card, assessment-card, results containers

**Expected Outcome:** Atmospheric depth with blue shadows, gilded page aesthetic

---

### SESSION 3: Typography & Color Validation

**Actions:**
1. Verify Google Fonts loading correctly (already done ✓)
2. Audit ALL color usage - ensure using CSS variables correctly:
   - --parchment-* for backgrounds
   - --mediterranean-* for actions/text
   - --champagne-* for accents
   - --danger-500 for match data (burgundy)
3. Check font-family application:
   - Cormorant Garamond for headings
   - DM Sans for body/data

**Expected Outcome:** Color system matches spec exactly

---

## **PHASE 2: CONTENT POPULATION** (Sessions 4-8)

### SESSION 4: Module 1 - Mandatory Five Questions

**Actions:**
1. Create question data array in js/modules/1-setup.js:
   ```javascript
   const MANDATORY_FIVE = [
     {
       id: 'social-battery',
       text: 'When facing a social gathering, do you typically feel:',
       choiceA: 'Energized by the prospect of meeting new people',
       choiceB: 'Drained and prefer quiet reflection'
     },
     // ... 4 more questions
   ];
   ```
2. Update question card rendering to iterate through array
3. Add proper question text for all 5 blocks (social, conflict, ambition, decision, philosophy)

**Expected Outcome:** All 5 questions display with proper text

---

### SESSION 5: Module 1 - HLA Processing Text Sequence

**Actions:**
1. Create status text array in js/components/biometric-seal.js:
   ```javascript
   const HLA_PROCESSING_STEPS = [
     'Detecting File Format (23andMe/Ancestry)...',
     'Parsing Chromosome 6 Region...',
     'Validating 1,000+ SNP Markers...',
     'Imputing HLA-A, B, DRB1 Alleles...'
   ];
   ```
2. Add sequential animation (500ms per step, total 3-4 seconds)
3. Update biometric seal component to show these messages

**Expected Outcome:** Labor illusion during DNA upload

---

### SESSION 6: Module 1 - Waitlist Modal Text

**Actions:**
1. Create formal waitlist modal in 1-setup.js
2. Add exact spec text: "Due to strict scientific equilibrium protocols, the Pilot Pool for male testing kits is currently at capacity. You have been placed on the Priority Access List. Please proceed with Visual and Psychometric calibration."
3. Style modal with glass-panel class
4. Trigger when gender quota full

**Expected Outcome:** Professional, exclusive waitlist messaging

---

### SESSION 7: Module 2 - Portrait Gallery Content

**Actions:**
1. Create stock image array (14-50 placeholder URLs):
   ```javascript
   const META_FP_DATASET = [
     { id: 'stock_001', url: 'https://placeholder.com/portrait1.jpg', type: 'stock' },
     // ... 13-49 more
   ];
   ```
2. Add gold leaf border to portrait frame:
   ```css
   .calibration-portrait-frame {
     border: 4px solid var(--champagne-400);
     padding: 1rem;
   }
   ```
3. Implement image loading logic in 2-calibration.js

**Expected Outcome:** Portrait gallery with proper framing

---

### SESSION 8: Module 3 - Seven Cardinal Drivers Questions

**Actions:**
1. Create complete question set for all 7 drivers:
   ```javascript
   const CARDINAL_DRIVERS = [
     {
       driver: 'Passion',
       icon: 'icon-passion',
       question: 'In intimate connection, do you prioritize:',
       choiceA: 'Intense emotional vulnerability and passion',
       choiceB: 'Steady companionship and mutual respect'
     },
     // ... 6 more (Indulgence, Ambition, Serenity, Conviction, Yearning, Dignity)
   ];
   ```
2. Add driver icon watermark injection
3. Update 3-assessment.js to render all questions

**Expected Outcome:** Complete psychometric assessment

---

## **PHASE 3: ADVANCED ANIMATIONS** (Sessions 9-14)

### SESSION 9: Install & Configure Framer Motion

**Research Required:**
- [Motion.dev - React Animation](https://motion.dev/docs/react-animation)
- [Motion - Transitions](https://www.framer.com/motion/transition/)
- [Framer Motion Spring Generator](https://rapidtoolset.com/en/tool/framer-motion-spring-generator)

**Actions:**
1. Since this is vanilla JS (not React), research alternatives:
   - Option A: Use native Web Animations API
   - Option B: Use GSAP (GreenSock)
   - Option C: Enhance current animation library
2. Create spring physics easing for slider
3. Test spring feel on calibration slider

**Expected Outcome:** Slider has "weight" and drag

---

### SESSION 10: Gold Particle Dissolution (Module 1 & 3)

**Actions:**
1. Enhance js/lib/particles.js:
   - Add "dissolve" animation mode
   - Particles flow from card → progress bar (Module 1)
   - Particles flow upward → profile icon (Module 3)
2. Implement in 1-setup.js on question answer
3. Implement in 3-assessment.js on answer selection
4. Use HarmoniaEasing luxury curves

**Expected Outcome:** Visual data "ingestion" feedback

---

### SESSION 11: Liquid Fill Animations

**Actions:**
1. Enhance js/lib/liquid-fill.js for two modes:
   - Horizontal ink well (Module 1 progress)
   - Vertical glass tube (Module 3 progress)
2. Implement biometric seal liquid fill (bottom → top)
3. Add Royal Blue ink color
4. Smooth bezier wave animation

**Expected Outcome:** Ink well and tube fill smoothly

---

### SESSION 12: Calibration Slider Enhancements

**Actions:**
1. Add spring physics to calibration slider in 2-calibration.js
2. Implement background color shift based on value:
   - 1-2: Cool blue-grey (#e0e5e8)
   - 3: Neutral parchment
   - 4-5: Warm amber (#f5e6d3 with golden glow)
3. Update feedback text dynamically:
   - "Indifferent" / "Potential" / "Magnetic"
4. Add dwell time tracking (timestamp on render)
5. Record slider movement vector

**Expected Outcome:** Immersive rating experience

---

### SESSION 13: Module 4 - Theater of Computation (Part 1)

**Research Required:**
- SVG animation techniques
- Morphing animations
- Sequence choreography

**Actions:**
1. Create 4-stage animation sequence in 4-analysis.js
2. **Stage 1 (0-1.5s):** Genomic
   - Display rotating DNA helix (use existing SVG, animate rotation)
   - HLA marker highlighting effect
   - Text overlay: "HLA-A*02:01... MATCH", "Parsing Chromosome 6...", "MHC Synergy Detected"
3. **Stage 2 (1.5-3s):** Visual
   - Wireframe face mesh (create SVG)
   - Morphing animation
   - Text: "Triangulating Meta FP Vector...", "Calibrating Symmetry Preference..."

**Expected Outcome:** First 2 stages of labor illusion

---

### SESSION 14: Module 4 - Theater of Computation (Part 2)

**Actions:**
1. **Stage 3 (3-4.5s):** Psychometric
   - Spinning compass rose (radar chart)
   - Rotation + scale animation
   - Text: "Cross-referencing Driver Matrix...", "Seeking Complementary Dynamics..."
2. **Stage 4 (4.5-5s):** Synthesis
   - Collapse all layers to center golden point
   - Explosion effect using HarmoniaParticles
   - Reveal results page

**Expected Outcome:** Complete 5-second choreographed sequence

---

## **PHASE 4: DATA VISUALIZATION** (Sessions 15-17)

### SESSION 15: Migrate from Chart.js to Recharts

**Research Required:**
- [Recharts Official Docs](https://recharts.org/)
- [Recharts Radar Chart](https://recharts.github.io/en-US/api/Radar/)
- [React Donut Chart Tutorial](https://gozukara-mert.medium.com/react-customizable-donut-chart-715bb847f971)

**Actions:**
1. PROBLEM: Current implementation is vanilla JS, Recharts requires React
2. **Decision Point:**
   - Option A: Keep Chart.js, customize heavily
   - Option B: Migrate to React framework (major refactor)
   - Option C: Use D3.js (vanilla JS compatible)

**USER INPUT REQUIRED:** Which approach to take?

---

### SESSION 16: Donut Chart Implementation

**Actions:**
1. Create tri-factor donut chart in 5-results.js
2. Layers:
   - Outer ring: Visual 50% (Mediterranean Blue)
   - Middle ring: Psychometric 35% (Deep Burgundy)
   - Inner ring: Genetic 10% (Gold Champagne)
   - Small segment: Serendipity 5% (White/Void)
3. Center: Large percentage number (Cormorant Garamond)
4. Interactive: Click segment to see breakdown

**Expected Outcome:** Visual match score composition

---

### SESSION 17: Radar Chart Styling

**Actions:**
1. Create heptagonal (7-axis) radar chart
2. Custom styling:
   - Grid lines: Gold (stroke-champagne-400)
   - User profile: Blue fill with Multiply blend
   - Match profile: Burgundy fill with Multiply blend
   - Overlap: Purple/Indigo
3. Add hover tooltips for each axis
4. Axes labels: Passion, Indulgence, Ambition, Serenity, Conviction, Yearning, Dignity

**Expected Outcome:** Visual personality alignment proof

---

## **PHASE 5: POLISH & VALIDATION** (Sessions 18-20)

### SESSION 18: Chemical Spark Indicator

**Actions:**
1. Create horizontal chromosome map SVG (ruler visualization)
2. Add conditional Gold band glow when hlaMatch === true
3. Display badge: "Chemical Spark Detected"
4. Add explanatory text: "MHC Dissimilarity indicates robust biological chemistry"
5. Implement placebo logic (show even if no match for validation)

**Expected Outcome:** Biological compatibility indicator

---

### SESSION 19: Dynamic Personality Narrative

**Actions:**
1. Create narrative generation function in 5-results.js
2. Templates for:
   - High Similarity: "Both of you share exceptional Ambition and Conviction..."
   - Complementary: "Your high Ambition complements their Serenity, creating a 'Drive and Support' dynamic..."
3. Inject real personality scores into templates
4. Display below radar chart

**Expected Outcome:** AI-like personality summary

---

### SESSION 20: Final Text & CTA Updates

**Actions:**
1. Update all button text to match spec:
   - "Send Like" → "Initiate Protocol"
   - "Skip" → appropriate scientific language
2. Review ALL copy for "Scientific Humanism" tone
3. Remove any casual/gamified language
4. Add formal, precise terminology

**Expected Outcome:** Consistent tone throughout

---

## **VERIFICATION CHECKLIST**

After all sessions complete, verify:

- [ ] Paper grain texture visible on all pages
- [ ] All shadows are blue-tinted
- [ ] All borders are gold
- [ ] 5 Mandatory Five questions present
- [ ] HLA processing text sequence works
- [ ] Waitlist modal has exact spec text
- [ ] Portrait gallery has 14-50 images
- [ ] Gold frame on portraits
- [ ] Slider has spring physics
- [ ] Background color shifts with slider
- [ ] Dwell time tracking functional
- [ ] 7 Cardinal Driver questions present
- [ ] Driver icon watermarks display
- [ ] Vertical liquid tube fills
- [ ] Gold particle dissolution works
- [ ] 5-second Theater of Computation plays
- [ ] Donut chart shows tri-factor breakdown
- [ ] Radar chart has 7 axes with gold grid
- [ ] Overlap shows purple blend
- [ ] Chemical Spark indicator works
- [ ] Dynamic personality narrative generates
- [ ] All CTAs use formal language

---

## **ESTIMATED TIME**

- **Phase 1 (Foundation):** 3 sessions
- **Phase 2 (Content):** 5 sessions
- **Phase 3 (Animations):** 6 sessions
- **Phase 4 (Data Viz):** 3 sessions
- **Phase 5 (Polish):** 3 sessions

**Total:** 20 focused sessions

**Current vs Spec:** ~15% → 100%

---

## **DEPENDENCIES**

```
Foundation (1-3)
    ↓
Content (4-8)
    ↓
Animations (9-14) ← depends on content being in place
    ↓
Data Viz (15-17) ← depends on framework decision
    ↓
Polish (18-20)
```

---

## **AWAITING USER APPROVAL**

**User must review:**
1. CRITICAL-GAPS-AUDIT.md (understanding the problems)
2. This document (understanding the solutions)

**User must decide:**
1. Approve proceeding with all fixes?
2. Framework decision: Keep vanilla JS or migrate to React?
3. Session-by-session or batch execution?

**DO NOT BEGIN FIXES UNTIL USER APPROVES**
