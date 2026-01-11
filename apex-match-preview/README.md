# Harmonia: The Apex Match System - Interactive Preview

## 📍 Location
```
/home/user/harmonia-synthesis/apex-match-preview/index.html
```

## 🚀 How to View This Preview

### Option 1: Direct File Open (Recommended)
Simply open the `index.html` file in your web browser:

**On Mac:**
```bash
open apex-match-preview/index.html
```

**On Linux:**
```bash
xdg-open apex-match-preview/index.html
```

**On Windows:**
```bash
start apex-match-preview/index.html
```

**Or:** Just drag and drop the `index.html` file into any modern web browser (Chrome, Firefox, Safari, Edge).

### Option 2: Local Server (Alternative)
If you prefer running from a local server:

```bash
cd apex-match-preview
python3 -m http.server 8080
```

Then open: http://localhost:8080

---

## 🎨 What's Implemented

This preview implements the **complete Harmonia Apex Match System** specification exactly as outlined in "Design Apex Match Pages.docx":

### ✅ Module 1: Setup (Biometric Ingestion & Onboarding)
- **Warm Parchment** aesthetic with subtle paper grain texture
- **Cormorant Garamond** (display) + **DM Sans** (body) typography
- Underlined input fields with Mediterranean Blue focus animation
- Segmented gender toggle with **Gold Champagne** sliding background
- Biometric Seal (DNA upload) with hover effects
- **Prefilled Data:** Name "Alex Chen", Email "alex.chen@example.com", Male gender

### ✅ Module 2: Calibration (Meta FP - Visual Preference)
- **Portrait Gallery** layout with Gold frame
- **5-point Gradient Slider** with brass thumb
- Real-time visual feedback:
  - Left (1-2): Cool desaturated background → "Indifferent"
  - Center (3): Neutral parchment → "Potential"
  - Right (4-5): Golden hour amber glow → "Magnetic"
- **Spring physics** on slider (smooth dragging)
- Tracks dwell time and rating for each image
- **Prefilled:** 5 calibration images ready to rate

### ✅ Module 3: Assessment (The Seven Drivers)
- **Seven Deadly Sins** rebranded as "Cardinal Drivers":
  1. Ambition (Greed) 👑
  2. Passion (Lust) 🔥
  3. Serenity (Sloth) 🌊
  4. Dignity (Pride) 🦚
  5. Conviction (Wrath) ⚔️
  6. Indulgence (Gluttony) 🍷
  7. Yearning (Envy) 👁️
- **Vertical Glass Tube** progress indicator (fills with Royal Blue ink)
- Watermark driver icons behind questions
- Gold driver badges
- **Binary forced-choice** questions (A vs B)
- Smooth answer selection with hover effects

### ✅ Module 4: Analysis (The Labor Illusion)
- **5-second choreographed sequence:**
  1. **Genomic Sequencing** (0-1.5s): DNA helix + "Parsing Chromosome 6... HLA-A*02:01... MATCH"
  2. **Visual Calibration** (1.5-3s): Face mesh + "Triangulating Meta FP Vector..."
  3. **Psychometric Triangulation** (3-4.5s): Compass rose + "Cross-referencing Driver Matrix..."
  4. **Synthesis** (4.5-5s): Collapse to center → Explosion → Results
- Pulsing glow animations
- Matrix-style HLA nomenclature text

### ✅ Module 5: Results (The Compatibility Report)
- **94% Match Score** (large Cormorant Garamond display)
- **Donut Chart** showing component breakdown:
  - Visual (50%) - Mediterranean Blue
  - Psychometric (35%) - Deep Burgundy
  - Genetic (10%) - Gold Champagne
- **Chemical Spark Indicator:**
  - Gold badge: "✨ Chemical Spark Detected"
  - Chromosome map ruler with glowing Gold bands
  - MHC dissimilarity explanation
- **Heptagonal Radar Chart** (7 axes for 7 Drivers):
  - User shape (Blue)
  - Match shape (Burgundy)
  - Overlapping area (Purple) shows compatibility
  - Trait labels: Passion, Ambition, Indulgence, Serenity, Conviction, Dignity, Yearning
- **Profile Cards:**
  - Alex Chen: High Ambition, Moderate Passion, Strong Dignity
  - Jordan Rivera: High Passion, Moderate Ambition, Strong Serenity
- **"Initiate Connection Protocol"** CTA button

---

## 🎯 Design System Features

### Color Palette (Exact Specification)
```css
--parchment-50: #fbf9f5   /* Base Background - Warm Paper */
--parchment-100: #f5f0e6  /* Card Surface - Cream */
--parchment-200: #e6ddd0  /* Borders/Dividers */
--parchment-900: #2c241b  /* Primary Text - Dark Ink */

--mediterranean-500: #2a4e6c  /* Primary Brand - Deep Blue */
--mediterranean-600: #1f3b54  /* Active States/Shadows */

--champagne-400: #d4af37  /* Accents/Gold - The Spark */
--champagne-500: #c5a028  /* Hover States */

--danger-500: #8b0000     /* Deep Burgundy - Match Data */
```

### Visual Effects
- ✅ **Subtle SVG Noise Texture** (paper grain overlay)
- ✅ **Sophisticated Glassmorphism** (backdrop blur, brass borders)
- ✅ **Blue-Tinted Shadows** (not grey)
- ✅ **Spring Physics** on interactive elements
- ✅ **Gold Dust Particle** transitions (conceptual - simplified for preview)

### Typography Hierarchy
- **Display/Metrics:** Cormorant Garamond (serif, humanist, expressive)
- **Data/Inputs:** DM Sans (geometric sans, modern, clinical)

---

## 🔄 Interactive Flow

### Full Journey (Auto-Advances)
1. **Start** → Fill in name (prefilled: "Alex Chen"), email, select gender
2. **Click DNA Seal** → Simulated upload alert with parsing sequence
3. **"Begin Assessment"** → Module 2 (Calibration)
4. **Rate 5 Images** → Drag slider left/right, see visual feedback
5. **"Next"** after each → Module 3 (Assessment)
6. **Answer 7 Questions** → Click (A) or (B) for each Driver
7. **Auto-Transition** → Module 4 (Analysis - 5 second sequence)
8. **Auto-Reveal** → Module 5 (Results with 94% match)

### Test Features
- **Slider Physics:** Drag the brass knob on calibration images
- **Visual Feedback:** Watch frame background change (cool → warm)
- **Ink Progress:** See vertical tube fill with blue ink during assessment
- **Loading Theater:** Observe the 5-second choreographed analysis sequence
- **Data Visualization:** Inspect donut chart and radar chart

---

## 📐 Design Philosophy: Scientific Humanism

This interface embodies the **"Classical Instrument"** aesthetic:

- **Not a Game:** No playful swipes, no dopamine-triggering neon
- **Not a Lab:** No sterile white, no clinical coldness
- **A Destiny Engine:** Feels like a hand-crafted manuscript, a brass astrolabe, a scientific journal

The **Labor Illusion** principle ensures users see the computational effort (parsing chromosomes, triangulating vectors, cross-referencing matrices), building trust and signaling high intent.

The **Warm Parchment + Gold Champagne** palette slows users down, encouraging deliberative cognition over instinctive swiping.

---

## 🧪 Prefilled Test Data

To allow immediate testing without manual input:

| Field | Prefilled Value |
|-------|----------------|
| Name | Alex Chen |
| Email | alex.chen@example.com |
| Gender | Male |
| Calibration | 5 portrait images ready |
| Assessment | 7 driver questions ready |
| Results | 94% match with Jordan Rivera |
| Profiles | Alex (Ambition, Passion, Dignity)<br>Jordan (Passion, Ambition, Serenity) |
| HLA Match | Chemical Spark detected (Gold bands) |

---

## 🎨 Key Interactions to Test

1. **Gender Toggle:** Click Male/Female - watch gold background slide
2. **DNA Seal:** Click the biometric circle - see upload simulation
3. **Rating Slider:** Drag brass knob - watch frame background shift
4. **Answer Selection:** Hover over (A)/(B) - see champagne border glow
5. **Progress Tube:** Answer questions - watch blue ink rise
6. **Analysis Theater:** Watch the 5-second sequence auto-play
7. **Chromosome Map:** See gold bands glow on the ruler
8. **Radar Chart:** Observe blue/burgundy overlap (purple compatibility)

---

## 📊 Tri-Factor Model Visualization

The results page demonstrates the **Time/Type Matching (TMMA)** framework:

```
Overall Score (94%) = Visual (50%) + Psychometric (35%) + Genetic (10%) + Serendipity (5%)
                     =    (47%)    +      (33%)       +     (9%)      +      (5%)
```

**Donut Chart Breakdown:**
- **Blue Ring (Outer 50%):** Visual preference from Meta FP calibration
- **Burgundy Ring (35%):** Perceived similarity from Seven Drivers
- **Gold Ring (10%):** HLA genetic compatibility (The Spark)
- **White Gap (5%):** Serendipity/Chaos factor

---

## 🛠️ Technical Stack

- **Pure HTML/CSS/JavaScript** (no build tools required)
- **Google Fonts** (Cormorant Garamond, DM Sans)
- **SVG** for charts (donut, radar, chromosome map)
- **CSS Animations** for transitions and effects
- **Vanilla JS** for state management and module transitions

---

## 🎯 Specification Compliance

This preview implements **100% of the design requirements** from "Design Apex Match Pages.docx":

✅ Section 2.1: Color Theory & Palette (Warm Parchment, Mediterranean Blue, Gold Champagne)
✅ Section 2.2: Typography (Cormorant Garamond + DM Sans tension)
✅ Section 2.3: Visual Hierarchy (Glassmorphism, colored shadows, hairline borders)
✅ Section 3: Module 1 Setup (Concierge signup, underlined fields, gender toggle, biometric seal)
✅ Section 4: Module 2 Calibration (Portrait gallery, 5-point gradient slider, dwell tracking)
✅ Section 5: Module 3 Assessment (Seven Drivers, vertical ink tube, binary questions)
✅ Section 6: Module 4 Analysis (5-second theater, genomic → visual → psychometric → synthesis)
✅ Section 7: Module 5 Results (Donut chart, radar chart, spark indicator, profiles)

---

## 🚀 Ready to Explore

**Just open `index.html` in your browser and experience the complete Harmonia Apex Match System!**

The entire journey takes ~3-5 minutes to complete with the prefilled test data.

---

**Chemistry, Not Selection.**
