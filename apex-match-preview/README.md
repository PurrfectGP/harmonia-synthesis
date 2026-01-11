
# Harmonia: Architectural Specification and Design Strategy for the Apex Match System

## 1. Executive Vision: The Paradigm of Scientific Humanism {#executive-vision-the-paradigm-of-scientific-humanism}

The contemporary landscape of digital courtship is defined by a crisis
of \"search friction\" and the commodification of human connection. The
dominant algorithmic paradigms---collaborative filtering and
high-frequency swipe mechanics---have created a marketplace
characterized by \"decision fatigue,\" superficial filtering, and a
paradox of choice that paradoxically lowers the probability of
meaningful pair-bonding.^1^ Users are reduced to static data points, and
the complex, multi-modal nature of attraction is flattened into binary
vectors of \"Like\" or \"Pass.\"

The proposed solution, **Harmonia** (internally referenced as the Apex
Match System), represents a radical departure from this gamified model.
It posits that attraction is a cumulative probability function of three
distinct variables: **Visual Preference (Meta FP)**, **Psychological
Resonance (Perceived Similarity)**, and **Biological Compatibility
(MHC/HLA Synergy)**.^1^ Unlike traditional platforms that obscure their
mechanisms behind \"black box\" algorithms, Harmonia is built on the
philosophy of **\"Quantified Romance.\"** It utilizes the \"Labor
Illusion\"---a psychological principle suggesting that users ascribe
greater value to results when they witness the computational effort
behind them ^1^---to build trust and signal high intent.

However, the defining characteristic of Harmonia is not merely its
algorithmic rigor, but its aesthetic and interaction philosophy:
**Scientific Humanism**. The interface does not mimic the sterile,
clinical look of a laboratory, nor the neon-soaked, dopamine-triggering
visuals of a casino-style game. Instead, it adopts the visual language
of the **Classical Instrument**. Drawing from the provided design index
(index.html), the platform utilizes a palette of **Warm Parchment**,
**Mediterranean Blue**, and **Gold Champagne**.^1^ The typography pairs
**Cormorant Garamond** (a humanist serif evoking literary tradition)
with **DM Sans** (a geometric modern sans), creating a tension between
the romantic ideal and the data-driven reality.

This comprehensive design report serves as the definitive architectural
blueprint for the Harmonia platform. It translates the validation logic
from the \"Harmonia Engine Pilot Study\" ^1^ and the specific
operational requirements discussed in technical meetings ^1^ into a
granular UX/UI specification. It is designed to guide the development of
a React-based frontend that is not only functional but emotionally
resonant, guiding the user through the five critical modules: **Setup**,
**Calibration**, **Assessment**, **Analysis**, and **Results**.

### 1.1 The Theoretical Framework: The Tri-Factor Model {#the-theoretical-framework-the-tri-factor-model}

The Harmonia architecture is predicated on the sequential integration of
three data streams, a methodology known as **Time/Type Matching
(TMMA)**. This approach introduces variables in staggered phases to
prevent \"cross-contamination\" (e.g., the Halo Effect of a photo
biasing the perception of personality).^1^ The design must reflect this
phased disclosure, treating each module as a distinct stage in a
scientific journey.

| **Variable**                             | **Weight** | **Scientific Basis & Validation Protocol**                                                                                                                                                                           | **UX/UI Design Implication**                                                                                                                                                               |
|------------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Visual Preference (Meta FP)**          | **50%**    | **The Halo Effect & Transfer Learning:** Attraction is the primary gatekeeper. The system creates a baseline \"Face Preference\" vector using stock imagery before introducing real profiles.^1^                     | Requires a \"Calibration\" module (Stage 1) that feels like a curated gallery. The UI must capture implicit signals like \"dwell time\" and \"decision velocity\" to refine the vector.^1^ |
| **Psychometrics (Perceived Similarity)** | **35%**    | **Identity Malleability & The \"Sins\":** Users are attracted to those they *perceive* as similar. The validation study actively manipulates this perception to test if users can be influenced by the algorithm.^1^ | Utilizes a mandatory \"Five-Question Inquiry\" and a \"Seven Drivers\" (Sins) assessment. Visualized as a \"Compass Rose\" (Radar Chart) to show alignment rather than raw scores.^1^      |
| **Genetics (HLA / Chemical Spark)**      | **10%**    | **MHC Dissimilarity:** Biological compatibility based on immune system genes. Validated via a \"Placebo vs. Incentive\" protocol where some users are told they match even if they don\'t.^1^                        | Requires a \"Biometric Ingestion\" interface that treats DNA data with reverence. Visualized as \"The Spark\" or \"Gold Thread\"---a high-value indicator of \"destiny\".^1^               |
| **Serendipity**                          | **5%**     | **Stochastic Variation:** Accounts for the \"Chaos\" factor and logistical noise.                                                                                                                                    | Represented as the \"Void\" or \"White Segment\" in visualizations, acknowledging the limits of computation.^1^                                                                            |

The interaction design for each of these variables must balance the
**Science** (accurate data collection) with the **Suggestion** (the
psychological priming that makes the user *believe* in the match).^1^

## 2. Design System Architecture: The \"Harmonia\" Aesthetic {#design-system-architecture-the-harmonia-aesthetic}

The visual identity of Harmonia is critical to its function. In a market
saturated with \"Dark Mode\" cyber-aesthetics and \"Clean White\"
corporate minimalism, Harmonia's **\"Warm Parchment\"** theme signals a
return to something tangible, permanent, and valuable. It is an
interface that feels like it has been written, not just rendered.

### 2.1 Color Theory and Palette Application {#color-theory-and-palette-application}

The color palette is derived directly from the provided index.html style
guide, utilizing CSS variables to ensure consistency across the
application.^1^

- **Primary Background: Warm Parchment (#fbf9f5 to \#f5f0e6)**

  - *Psychology:* Evokes the feeling of high-quality paper, manuscripts,
    > or archival documents. It reduces eye strain compared to pure
    > white and creates a sense of intimacy and warmth.

  - *Application:* Used for the main application background and card
    > surfaces. A subtle grain texture (noise) is applied to prevent the
    > \"flatness\" typical of digital screens, giving the UI a tactile
    > quality.

- **Primary Action & Depth: Mediterranean Blue (#2a4e6c to \#1f3b54)**

  - *Psychology:* Represents depth, intellect, stability, and trust. It
    > anchors the ethereal parchment tones and provides a \"serious\"
    > counterweight to the romance.

  - *Application:* Used for primary buttons, active states, toggle
    > switches, and deep shadows. It replaces standard black for text,
    > softening the contrast while maintaining readability.

- **Accent & Value: Gold Champagne (#d4af37 to \#c5a028)**

  - *Psychology:* Represents scarcity, value, and \"The Spark.\" It
    > triggers a sense of luxury and importance.

  - *Application:* Used sparingly for high-value interactions: the
    > \"Spark\" indicator, successful match notifications, slider
    > \"thumbs,\" and border highlights on active inputs.

- **Functional Alert: Deep Burgundy (#8b0000)**

  - *Psychology:* Represents passion, biology (blood/heart), and error
    > states.

  - *Application:* Used for the \"Match\" polygon in radar charts (to
    > contrast with the user\'s Blue) and for critical system alerts.

### 2.2 Typography: The Tension of Old and New {#typography-the-tension-of-old-and-new}

The typographic system creates a deliberate tension between the \"Old
World\" of romantic idealism and the \"New World\" of data science.^1^

- **Display / Headings: Cormorant Garamond**

  - *Characteristics:* A distinct display serif with flowing curves and
    > sharp serifs. It feels human, historical, and expressive.

  - *Usage:* All module titles (e.g., \"The Calibration\"), major
    > questions, and the final \"Match Score\" percentage. It frames the
    > experience as a narrative.

- **Data / Body: DM Sans**

  - *Characteristics:* A geometric sans-serif with excellent legibility
    > at small sizes. It is objective, modern, and clinical.

  - *Usage:* Input fields, data labels, button text, and instructional
    > copy. It frames the inputs as scientific data points.

### 2.3 Visual Hierarchy and Materiality {#visual-hierarchy-and-materiality}

The interface utilizes **\"Sophisticated Glassmorphism\"** to create
depth.^1^ Unlike the \"frosted glass\" of iOS, Harmonia's glass effect
looks like **Lens Optical Glass** or **Vellum**.

- **The Card Metaphor:** Content is not floating in a void; it rests on
  > \"cards\" styled as thick, cream-colored stationery
  > (bg-parchment-100).

- **Shadows:** Shadows are not grey. They are tinted with
  > **Mediterranean Blue** (shadow-mediterranean-500/10), creating a
  > rich, atmospheric depth that feels like natural light interacting
  > with ink.

- **Borders:** Borders are hairline thin (1px), often colored in **Gold
  > Champagne** at low opacity (border-champagne-400/30), mimicking the
  > edge of a gilded page or a brass instrument casing.

## 3. Module 1: The Setup (Biometric Ingestion & Onboarding) {#module-1-the-setup-biometric-ingestion-onboarding}

The onboarding phase is the user\'s initiation into the Harmonia
protocol. It must immediately differentiate itself from the
low-friction, gamified signup flows of Tinder or Hinge. The goal is to
establish **High Intent**.^1^

### 3.1 The \"Concierge\" Signup Flow {#the-concierge-signup-flow}

The initial data collection is streamlined but formal. The meeting notes
clarify that while the study requires a gender equilibrium (1:1 ratio),
this complexity should not block the initial signup.^1^

- **Layout:** A centered, single-column layout max-width 480px
  > (mobile-first), resembling a formal invitation or a digital dossier.

- **Input Design:**

  - Inputs are styled as **\"Underlined Fields\"** (border-bottom only)
    > rather than boxed containers. This mimics filling out a paper
    > form.

  - *Interaction:* When focused, the bottom border animates from
    > center-out in **Mediterranean Blue**. The label (DM Sans) floats
    > upward, transitioning to a smaller scale.

- **Data Points:** Name, Email, Password.

- **Gender & Orientation Logic:**

  - The user selects gender via a **Segmented Control** (Sliding
    > Toggle).

  - *Design:* A pill-shaped container with a sliding **Gold** background
    > that moves behind the active text (Male/Female).

  - *Waitlist Logic:* As per Felix\'s correction ^1^, the \"Waitlist\"
    > is **not** for the app account itself, but for the **DNA Testing
    > Kit**. The signup proceeds regardless of gender balance, but the
    > \"Kit Request\" later in the flow may be gated if the gender quota
    > is full.

### 3.2 The \"Mandatory Five\" Inquiry {#the-mandatory-five-inquiry}

To establish a valid psychometric baseline before any \"Sins\" or
\"DNA\" data is processed, every user must answer the same **Five
Mandatory Questions**.^1^

- **Selection Logic:** These questions are drawn from five distinct
  > \"blocks\" of personality traits (e.g., Social Battery, Conflict
  > Style, Ambition).

- **Presentation: The Card Stack.**

  - Each question appears on a solitary card in the center of the
    > screen.

  - *Typography:* The question text is large, set in **Cormorant
    > Garamond**.

  - *Interaction:* The user selects an answer (A or B/C). The card does
    > not \"swipe\" away playfully. It **dissolves** into gold particles
    > that flow into a progress bar at the bottom, symbolizing the data
    > being \"ingested\" by the system.

- **Progress Indicator:** A \"Fountain Pen\" or \"Ink Well\" progress
  > bar. As the user advances, a line of **Royal Blue Ink** extends
  > across the bottom of the screen.

### 3.3 The Biometric Ingestion Port (HLA Integration) {#the-biometric-ingestion-port-hla-integration}

This is the \"Wow\" moment of the setup. It bridges the digital and
biological worlds. The system must handle two scenarios: users with
existing data (23andMe) and users needing a kit.^1^

- **Visual Metaphor: The Seal.**

  - Instead of a standard \"File Upload\" box, the component is designed
    > as a circular **\"Biometric Seal.\"**

  - *Resting State:* A dashed circle in **Mediterranean Blue**. Inside,
    > a stylized **Double Helix** icon drawn in a sketch-like style (Da
    > Vinci-esque).

  - *Hover State:* The border becomes solid **Gold Champagne** and
    > pulses gently (\"Breathing\" animation). The cursor becomes a
    > \"DNA\" icon.

- **Interaction Physics (The \"Labor Illusion\"):**

  - When a file (e.g., genome.txt) is dropped onto the Seal:

    - **Phase 1 (Ingestion):** The circle fills with a liquid gold
      > effect (SVG clip-path animation), moving from bottom to top.

    - **Phase 2 (Sequencing):** The UI transitions to a \"Processing\"
      > state. The text does not say \"Uploading\...\" but uses the
      > specific language from the **HLA Parser Pipeline** ^1^:

      - *\"Detecting File Format (23andMe/Ancestry)\...\"*

      - *\"Parsing Chromosome 6 Region\...\"*

      - *\"Validating 1,000+ SNP Markers\...\"*

      - *\"Imputing HLA-A, B, DRB1 Alleles\...\"*

    - *Timing:* This sequence is artificially delayed (approx. 3-4
      > seconds) to ensure the user perceives the complexity of the
      > analysis.^1^

- **The Waitlist Gate:** If the user selects \"Request Kit,\" the system
  > checks the gender equilibrium backend.

  - *If Quota Full:* A polite, formal modal appears: *\"Due to strict
    > scientific equilibrium protocols, the Pilot Pool for male testing
    > kits is currently at capacity. You have been placed on the
    > Priority Access List. Please proceed with Visual and Psychometric
    > calibration.\"*.^1^

## 4. Module 2: Calibration (The Meta FP Engine) {#module-2-calibration-the-meta-fp-engine}

Once onboarding is complete, the user enters the **Calibration Phase**.
This module is designed to train the **Visual Preference (Meta FP)**
algorithm, which accounts for 50% of the match score.^1^

### 4.1 The Theory: Transfer Learning & Dwell Time {#the-theory-transfer-learning-dwell-time}

The system uses \"Transfer Learning\".^1^ By analyzing the user\'s
reaction to a standardized set of **Stock Images** (The Meta FP
Dataset), it builds a preference vector that can be applied to the real
testing pool.

- **Implicit Signals:** The system must track not just the explicit
  > rating, but the **Dwell Time** (milliseconds spent looking) and
  > **Decision Velocity** (speed of the swipe/click). Fast, high-rating
  > decisions indicate \"Visceral/Instinctive\" attraction; slow,
  > high-rating decisions indicate \"Cognitive/Deliberative\"
  > attraction.^1^

### 4.2 UI Pattern: The \"Portrait Gallery\" {#ui-pattern-the-portrait-gallery}

We reject the \"Stack of Cards\" (Tinder) model, which encourages
disposability. Harmonia uses a **\"Portrait Gallery\"** or **\"Easel\"**
metaphor.

- **The Frame:** The user is presented with a single portrait, framed by
  > a subtle **Gold Leaf** border (border-champagne-400).

- **The Stimuli:** The first 14-50 images are from the **Meta FP
  > Dataset** (StockX/Chicago Face Database).^1^ The user is unaware
  > these are stock; they are presented as \"Calibration Profiles.\"

  - *Context:* No names, no bios. Pure visual phenotype. This isolates
    > the \"Halo Effect\" variable.^1^

- **The Rating Mechanism: The 1-5 Likert Scale.**

  - Binary \"Like/Pass\" is insufficient for granular data. We use a
    > **5-point Gradient Slider**.

  - *Visual:* A horizontal track beneath the portrait.

    - **Track:** A thin line of **Mediterranean Blue**.

    - **Thumb:** A Brass/Gold knob with a subtle shadow.

  - *Feedback (Color Theory):*

    - **1-2 (Left):** The background behind the portrait cools
      > (Desaturated Blue/Grey). The feedback text reads
      > *\"Indifferent.\"*

    - **3 (Center):** The background is neutral Parchment. Feedback:
      > *\"Potential.\"*

    - **4-5 (Right):** The background glows with a **\"Golden Hour\"**
      > light (Warm Amber). Feedback: *\"Magnetic.\"*

- **Interaction Physics:**

  - The slider uses **Spring Physics** (via Framer Motion). It has
    > \"weight.\" It doesn\'t snap instantly; it drags slightly, forcing
    > the user to \"feel\" the rating.

  - *Dwell Capture:* The timer starts the moment the image renders. The
    > vector of slider movement is recorded.

### 4.3 The \"Trickle\" Strategy {#the-trickle-strategy}

As per Felix\'s notes, the profiles are \"trickled\" out.^1^

- **Mix of Fake & Real:** The stream seamlessly mixes the Stock Images
  > (Meta FP) with Real Profiles (Testing Pool).

- **The \"Real\" Flag:** For the backend/admin view (and potentially for
  > the \"Perceived Similarity\" stage), there is a mechanism to signal
  > if a profile is \"Real\" or \"Fake\" ^1^, but this is hidden from
  > the user during Calibration to maintain the immersion.

## 5. Module 3: Assessment (The Sins & Perceived Similarity) {#module-3-assessment-the-sins-perceived-similarity}

With the visual baseline established, the user moves to the
**Psychometric Profiling** phase. This module measures the 35%
\"Personality\" variable.^1^

### 5.1 Rebranding the \"Seven Deadly Sins\" {#rebranding-the-seven-deadly-sins}

To fit the \"Sophisticated Humanism\" of Harmonia, the raw theological
terms (Lust, Gluttony, etc.) are rebranded as **\"Cardinal Drivers.\"**
This reduces defensiveness while maintaining the archetypal power of the
model.^1^

| **Theological Sin** | **Harmonia Driver** | **Visual Iconography (Sketch Style)** |
|---------------------|---------------------|---------------------------------------|
| **Lust**            | **Passion**         | A Burning Heart or Flame              |
| **Gluttony**        | **Indulgence**      | A Wine Chalice or Cornucopia          |
| **Greed**           | **Ambition**        | A Crown or Mountain Peak              |
| **Sloth**           | **Serenity**        | A Sleeping Lion or Still Water        |
| **Wrath**           | **Conviction**      | A Sword or Lightning Bolt             |
| **Envy**            | **Yearning**        | An Eye or Mirror                      |
| **Pride**           | **Dignity**         | A Peacock Feather or Pillar           |

### 5.2 The \"Inquiry Deck\" Interface {#the-inquiry-deck-interface}

This module uses a **Single-Card Stack** layout, distinct from the
Portrait Gallery.

- **The Card:** A large, vertical card centered on the screen.

  - *Background:* A slightly lighter cream (bg-parchment-50) to pop
    > against the darker background.

  - *Watermark:* A faint, sketch-style watermark of the Driver\'s icon
    > (e.g., a Crown for Ambition) sits behind the text.

- **The Question Logic (Forced Choice):**

  - Questions are binary (A vs. B) to force a decision and prevent
    > \"neutral\" hedging.^1^

  - *Example:* \"For **Serenity** (Sloth): Do you find regeneration in
    > **(A) Motion and Activity** or **(B) Stillness and Silence**?\"

- **Liquid Progress Indicator:**

  - Instead of a digital bar, the right edge of the screen features a
    > thin, vertical glass tube.

  - As the user answers, the tube fills with **Royal Blue Fluid** (Ink).
    > This reinforces the metaphor of \"writing one\'s profile.\"

- **Transition Animation:**

  - When an option is selected, the text doesn\'t just fade. It
    > transforms into **Gold Dust** particles that flow upward into a
    > \"Profile Icon\" in the header.

  - This animation visually confirms data capture, satisfying the
    > \"Labor Illusion.\"

### 5.3 The \"Perceived Similarity\" Experiment {#the-perceived-similarity-experiment}

In the backend, this module captures the user\'s \"Actual Personality.\"
However, during the matching phase (Module 5), this data will be
manipulated to test **\"Identity Malleability\"**.^1^ The UI must be
capable of displaying \"highlighted traits\" that may or may not be
statistically significant, effectively \"telling\" the user they are
similar to a match to see if they believe it.

## 6. Module 4: The Analysis Engine (The \"Labor Illusion\" Loading Screen) {#module-4-the-analysis-engine-the-labor-illusion-loading-screen}

This module is the psychological pivot point of the application. The
user has invested effort (Setup, Calibration, Assessment). Now, the
system must demonstrate the \"Labor\" of finding a match.^1^ A simple
spinner is insufficient; the user must *see* the synthesis of the three
data streams.

### 6.1 The \"Theater of Computation\" {#the-theater-of-computation}

The screen dims, creating a spotlight effect. The animation sequence
lasts exactly **5 seconds** ^1^, choreographed to frame the \"Scientific
Humanism\" narrative.

- **Stage 1: Genomic Sequencing (0s - 1.5s)**

  - *Visual:* A **Vitruvian Man** or anatomical sketch appears in the
    > center. Overlaid is a **Double Helix** drawn in Gold Ink.

  - *Animation:* The helix rotates. Specific \"bands\" (HLA markers)
    > light up in **Mediterranean Blue**.

  - *Text:* Vertical streams of \"Matrix-style\" text, but utilizing the
    > specific HLA nomenclature ^1^: *\"HLA-A*02:01\... MATCH\"\*,
    > *\"Parsing Chromosome 6\...\"*, *\"MHC Synergy Detected.\"*

- **Stage 2: Visual Calibration (1.5s - 3s)**

  - *Visual:* The helix fades. A **Wireframe Face Mesh** appears. It
    > morphs rapidly, cycling through the specific phenotypes the user
    > rated highly in the Calibration phase (e.g., specific eye shapes,
    > jawlines).^1^

  - *Text:* *\"Triangulating Meta FP Vector\...\"*, *\"Calibrating
    > Symmetry Preference\...\"*.

- **Stage 3: Psychometric Triangulation (3s - 4.5s)**

  - *Visual:* A **Compass Rose** (Radar Chart) appears. It spins and
    > shifts shape, expanding and contracting as if \"seeking\" a lock.

  - *Text:* *\"Cross-referencing Driver Matrix\...\"*, *\"Seeking
    > Complementary Serenity/Ambition Dynamics\...\"*.

- **Stage 4: Synthesis (4.5s - 5s)**

  - *Visual:* All three layers---The Helix, The Face, The
    > Compass---collapse into a single **Golden Point** of light in the
    > center.

  - *Climax:* The point explodes outward in a shockwave of gold dust and
    > light, revealing the **Results Page**.

## 7. Module 5: The Results (Synthesis & Profile) {#module-5-the-results-synthesis-profile}

The Results Page is the dossier. It must present the match not as a
\"Profile\" but as a **\"Compatibility Report.\"**

### 7.1 The Match Score Breakdown (The Donut) {#the-match-score-breakdown-the-donut}

- **Central Metric:** A large, elegant number (e.g., **\"94%\"**) set in
  > **Cormorant Garamond**. It sits in the center of a concentric
  > **Donut Chart**.

- **The Rings (Data Visualization):**

  - **Visual (50%):** A thick ring of **Mediterranean Blue**.

  - **Psychometric (35%):** A ring of **Deep Burgundy**.

  - **Genetic (10%):** A ring of **Gold Champagne** (representing the
    > \"Spark\").

  - **Serendipity (5%):** A segment of **White/Void** (representing the
    > unknown).

- **Interaction:** Tapping a segment isolates that score and displays a
  > detailed breakdown below.

### 7.2 The Psychometric Compass (Radar Chart) {#the-psychometric-compass-radar-chart}

- **Visual:** A **Heptagonal Radar Chart** (7 Axes for the 7
  > Drivers).^1^

- **Styling:**

  - *Grid:* Faint gold lines (stroke-champagne-400), resembling a map
    > grid.

  - *User Shape:* Filled with **Blue Ink** (Multiply blending mode).

  - *Match Shape:* Filled with **Red/Burgundy Ink** (Multiply blending
    > mode).

  - *Overlap:* The intersection creates a deep **Purple/Indigo**. Large
    > overlap visually signifies high compatibility.

- **Insight Tooltip:** Hovering over an axis (e.g., \"Ambition\")
  > expands a text box: *\"Your high Ambition complements their moderate
  > Serenity, creating a dynamic of \'Drive and Support\'.\"*

### 7.3 The \"Chemical Spark\" Indicator (The Placebo) {#the-chemical-spark-indicator-the-placebo}

This section handles the 10% Biological variable.

- **Visual:** A horizontal **\"Chromosome Map\"** styled like a ruler or
  > scale below the charts.

- **Logic:**

  - *True Positive / Placebo Groups:* If the user is in Group A (True
    > Match) or Group B (Placebo) ^1^, specific bands on the ruler glow
    > **Gold**. A badge appears: **\"Chemical Spark Detected.\"**

  - *Copy:* *\"MHC Dissimilarity indicates robust biological
    > chemistry.\"*.^1^

  - *Negative Control:* The ruler remains dim. No badge.

- **Strategic Note:** The UI effectively \"blinds\" the user to the
  > reality of the DNA match, serving the validation protocol by
  > delivering the *suggestion* of compatibility perfectly.

### 7.4 The \"Perceived Similarity\" Narrative {#the-perceived-similarity-narrative}

Below the data, an AI-generated text summary appears.

- **Content:** This text is dynamically generated to emphasize shared
  > traits (High Similarity Condition) or complementary differences (Low
  > Similarity Condition).^1^

- **Tone:** The copy must be authoritative and insightful, reinforcing
  > the \"Scientific\" validity of the match.

### 7.5 The Connection Protocol (Meeting) {#the-connection-protocol-meeting}

- **The Call to Action:** Instead of \"Message,\" the button reads
  > **\"Initiate Protocol\"** or **\"Open Channel.\"**

- **Chat Logic:** As per the meeting notes ^1^, the system may gate the
  > full reveal or meeting capability until a certain threshold of
  > interaction (messages exchanged) is met, ensuring data is collected
  > on the *process* of connection.

## 8. Technical Architecture & Implementation Strategy {#technical-architecture-implementation-strategy}

To execute this \"Best Ever\" design within the constraints of an AI
coding agent, the technology stack is selected for performance,
animation fidelity, and aesthetic control.

### 8.1 Core Stack {#core-stack}

- **Framework:** **React (Next.js App Router)**. Ensures fast initial
  > load and SEO (for the web version).

- **Styling:** **Tailwind CSS**. Configured with the specific parchment,
  > mediterranean, and champagne color tokens.

- **State Management:** **Zustand**. A lightweight store to manage the
  > complex, multi-stage state (Setup -\> Calibration -\> Quiz -\>
  > Results) without the boilerplate of Redux.

- **Animation:** **Framer Motion**. Essential for the \"Labor Illusion\"
  > sequences (sequencing, morphing, layout transitions) and the
  > spring-physics of the rating slider.^1^

- **Data Visualization:** **Recharts**. Chosen for its composability and
  > ability to render SVG-based Radar/Donut charts that can be styled
  > with custom distinct colors and strokes (e.g., the \"Gold
  > Grid\").^1^

- **Icons:** **Lucide-React**. Styled with thin stroke widths to match
  > the elegant typography.

### 8.2 The HLA Processing Pipeline (Backend Logic) {#the-hla-processing-pipeline-backend-logic}

While the frontend handles the \"Theater,\" the backend (mocked or real)
follows a strict pipeline ^1^:

1.  **Parser:** Detects format (23andMe/Ancestry), extracts Chromosome 6
    > data (Positions 29M-34M).

2.  **Imputation (HIBAG):** Uses R-based HIBAG to infer HLA alleles.

3.  **Standardization:** Converts to 2-field format (e.g., A\*02:01).

4.  **Compatibility:** Calculates the **Allele Sharing Score** (0-6). 0
    > Shared = High Compatibility (The Spark).

## 9. Master Prompts for Code Generation {#master-prompts-for-code-generation}

The following section aggregates the architectural, visual, and logical
requirements into a set of \"Master Prompts\" designed to be fed
directly into an AI coding agent (e.g., Claude 3.5 Sonnet or GPT-4o).
These prompts enforce the \"Harmonia\" style and the specific logic of
the validation study.

### 9.1 Prompt 1: Design System & Foundation {#prompt-1-design-system-foundation}

# Role: Lead Frontend Architect & Design Systems Lead {#role-lead-frontend-architect-design-systems-lead}

# Objective: Initialize the \"Harmonia\" Design System in Tailwind CSS and React. {#objective-initialize-the-harmonia-design-system-in-tailwind-css-and-react.}

Context:

We are building \"Harmonia,\" a high-end algorithmic dating platform.
The aesthetic is \"Scientific Humanism\"---a fusion of classical
instruments (astrolabes, manuscripts) and modern data science. It must
feel like a \"destiny engine,\" not a game.

1\. Color Palette (Tailwind Configuration):

Extend tailwind.config.js with these specific tokens:

- parchment:

  - 50: \'#fbf9f5\' (Base Background - Warm Paper)

  - 100: \'#f5f0e6\' (Card Surface - Cream)

  - 200: \'#e6ddd0\' (Borders/Dividers)

  - 900: \'#2c241b\' (Primary Text - Dark Ink)

- mediterranean:

  - 500: \'#2a4e6c\' (Primary Brand - Deep Blue)

  - 600: \'#1f3b54\' (Active States/Shadows)

- champagne:

  - 400: \'#d4af37\' (Accents/Gold - The Spark)

  - 500: \'#c5a028\' (Hover States)

- danger:

  - 500: \'#8b0000\' (Deep Burgundy - For \"Sins\" Match Data)

**2. Typography:**

- **Headers:** \"Cormorant Garamond\" (Google Font). Use for H1-H6,
  > \"Spark\" badges, and major metrics.

- **Body:** \"DM Sans\" (Google Font). Use for inputs, data labels, and
  > button text.

**3. Visual Effects (Glassmorphism & Texture):**

- Create a custom utility .bg-parchment-texture that applies a subtle
  > SVG noise overlay to the parchment-50 background to simulate paper
  > grain.

- Create .glass-panel: bg-parchment-100/90 backdrop-blur-md border
  > border-champagne-400/30 shadow-lg shadow-mediterranean-500/10.

- Shadows must be colored (Blue-tinted), not grey.

**4. Component Primitives:**

- **Buttons:** Not rounded pills. Slight border-radius (rounded-md).
  > Primary buttons use bg-mediterranean-500 with font-dm-sans.

- **Inputs:** \"Underlined\" style. No background. Border-bottom
  > border-parchment-200. On focus, animate border to mediterranean-500.

Output:

Generate the tailwind.config.js and a layout.tsx wrapper that applies
the font and texture globally.

### 9.2 Prompt 2: Core Logic & Modules (State Machine) {#prompt-2-core-logic-modules-state-machine}

# Role: Senior React Developer

# Objective: Build the Core Logic and Modules for Harmonia. {#objective-build-the-core-logic-and-modules-for-harmonia.}

**Stack:** React, Framer Motion, Zustand.

1\. State Management (Zustand Store):

Create useHarmoniaStore with:

- currentPhase: Enum

- gender: \'MALE\' \| \'FEMALE\'

- dnaKitStatus: \'NONE\' \| \'REQUESTED\' \| \'WAITLISTED\'

- metaFPScores: Array of objects { imageId, score (1-5), dwellTimeMs }

- quizAnswers: Object { openness: \'A\', ambition: \'B\',\... }

- hlaMatch: Boolean (True/False - The \"Spark\")

**2. Module 1: Setup (Onboarding):**

- **Inputs:** Name, Email.

- **Gender Toggle:** Segmented Control (Sliding Gold Background).

- **DNA Logic:**

  - Create a \"Biometric Seal\" component. Circular, Double Border
    > (Blue/Gold).

  - Inside: Stylized DNA Icon.

  - On Drag/Drop: Animate circle filling with \"Gold Ink\" (SVG
    > clip-path).

  - Text Feedback: Cycle through \"Parsing Chromosome 6\...\",
    > \"Imputing HLA Alleles\...\" (3s delay).

  - **Waitlist Logic:** If user selects \"Request Kit\" and gender ===
    > \'MALE\', show Modal: \"Pilot Pool at Capacity. Added to Priority
    > List.\"

**3. Module 2: Calibration (Meta FP):**

- **Layout:** \"Portrait Gallery\" (Single Card, Gold Frame).

- **Stimuli:** Iterate through 5 stock images (placeholders).

- **Input:** 5-Point Slider.

  - Track: Blue Line.

  - Thumb: Gold Knob.

  - Feedback: Left = \"Indifferent\" (Cool BG), Right = \"Magnetic\"
    > (Warm Amber BG).

  - **Metric:** Capture time from render to rating.

**4. Module 3: Assessment (The Drivers):**

- **Content:** 7 Questions mapping to \"Sins\" (Passion, Ambition,
  > Serenity, etc.).

- **UI:** Single Card Stack.

- **Progress:** Vertical \"Glass Tube\" on the right filling with Blue
  > Ink.

- **Animation:** On answer, text dissolves into Gold Particles and flies
  > to header.

**5. Module 4: Analysis (The Labor Illusion):**

- **Duration:** 5 Seconds.

- **Sequence:**

  1.  **Genomic:** Rotating DNA Helix (Gold). Text: \"Sequencing
      > HLA\...\"

  2.  **Visual:** Morphing Face Mesh. Text: \"Triangulating Meta
      > FP\...\"

  3.  **Psychometric:** Radar Chart scanning. Text: \"Cross-referencing
      > Drivers\...\"

  4.  **Synthesis:** Collapse to center point -\> Explosion -\> Results.

**6. Module 5: Results:**

- **Charts:**

  - Donut Chart (Recharts): 50% Visual (Blue), 35% Psych (Burgundy), 10%
    > Genetic (Gold). Center: \"94%\".

  - Radar Chart (Recharts): 7 Axes. User (Blue), Match (Burgundy).
    > Overlap = Purple.

- **Spark Indicator:**

  - If hlaMatch === true, show \"Chromosome Map\" (Ruler) with Gold
    > Bands glowing. Badge: \"Chemical Spark Detected.\"

Output:

Generate the React components for these modules, ensuring Framer Motion
handles the page transitions (Fade/Slide).

## 10. Conclusion and Strategic Implication {#conclusion-and-strategic-implication}

The Harmonia architecture represents a comprehensive synthesis of
**Scientific Rigor** and **Humanist Design**. By creating an interface
that respects the user\'s desire for depth and narrative---leveraging
the \"Labor Illusion\" of the Analysis Engine and the \"Classical\"
aesthetic of the Design System---Harmonia addresses the core market
failure of dating app fatigue.

The specific integration of the **Tri-Factor Model** (Visual,
Psychometric, Genetic) within a rigorous **Time/Type Matching**
framework ensures that the platform is not just a matchmaking tool, but
a validatable scientific instrument. The **Warm Parchment** and **Gold
Champagne** aesthetic serves a functional purpose: it slows the user
down, encouraging the \"deliberative\" cognition required for meaningful
choice, rather than the \"instinctive\" speed of the swipe economy. This
is the future of Quantified Romance: precise, beautiful, and deeply
human.

#### Works cited

1.  Dating Algorithm Validation Methodology Design.pdf
