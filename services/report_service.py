# Enhanced Report Service for Harmonia Synthesis
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)

class ReportService:
    """Generate comprehensive Word document reports with detailed analysis."""

    SIN_ORDER = ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]
    
    SIN_DESCRIPTIONS = {
        "greed": "Material possessions, resources, control over outcomes",
        "pride": "Self-image, status, being right, perfectionism",
        "lust": "Passion, intensity, immediate gratification, sensory experiences",
        "wrath": "Conflict response, boundaries, justice, emotional reactivity",
        "gluttony": "Indulgence, pleasure-seeking, moderation challenges",
        "envy": "Comparison with others, competition, validation needs",
        "sloth": "Energy management, effort avoidance, procrastination"
    }

    def generate_full_report(self, p1: dict, p2: dict, analysis: dict,
                             visual_data: dict, hla_data: dict,
                             similarity_result: dict, weights: dict,
                             filename: str) -> str:
        """
        Generate a comprehensive compatibility report with in-depth analysis.
        
        Includes:
        - Executive summary with overall score
        - Connection themes and star sign pairing
        - Individual character portraits
        - Full questionnaire responses with evidence
        - Detailed personality trait analysis with calculations
        - Visual analysis with features and confidence
        - HLA genetic compatibility with breakdown
        - Compatibility flags and final verdict
        """
        doc = Document()
        
        # Add helper method for tables
        def set_cell_border(cell, **kwargs):
            """Set cell border."""
            tc = cell._element
            tcPr = tc.get_or_add_tcPr()
            for edge in ('top', 'left', 'bottom', 'right'):
                if edge in kwargs:
                    edge_element = OxmlElement(f'w:{edge}')
                    edge_element.set(qn('w:val'), 'single')
                    edge_element.set(qn('w:sz'), '4')
                    edge_element.set(qn('w:color'), kwargs[edge])
                    tcPr.append(edge_element)

        # ═══════════════════════════════════════════════════════════════════
        # TITLE PAGE
        # ═══════════════════════════════════════════════════════════════════
        title = doc.add_heading('Harmonia Compatibility Report', 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER

        subtitle = doc.add_paragraph()
        subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = subtitle.add_run(f"{p1['name']} & {p2['name']}")
        run.bold = True
        run.font.size = Pt(18)
        run.font.color.rgb = RGBColor(138, 43, 226)  # Purple

        # Star sign title if available
        star_title = analysis.get('star_sign_title', '')
        if star_title:
            star_para = doc.add_paragraph()
            star_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = star_para.add_run(f'"{star_title}"')
            run.italic = True
            run.font.size = Pt(14)
            run.font.color.rgb = RGBColor(255, 105, 180)  # Hot pink

        date_para = doc.add_paragraph()
        date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        date_para.add_run(f"Generated: {datetime.now().strftime('%B %d, %Y at %H:%M')}").italic = True

        doc.add_paragraph()  # Spacer

        # ═══════════════════════════════════════════════════════════════════
        # EXECUTIVE SUMMARY
        # ═══════════════════════════════════════════════════════════════════
        doc.add_heading('Executive Summary', level=1)

        # Calculate weighted overall score
        visual_score = visual_data.get('mutual_attraction_score', 50)
        personality_score = similarity_result.get('percentage', 50)
        hla_score = hla_data.get('compatibility_score', 50)

        overall = (
            visual_score * weights['visual'] / 100 +
            personality_score * weights['personality'] / 100 +
            hla_score * weights['hla'] / 100
        )

        # Score table
        summary_table = doc.add_table(rows=5, cols=3)
        summary_table.style = 'Table Grid'

        headers = summary_table.rows[0].cells
        headers[0].text = "Component"
        headers[1].text = "Score"
        headers[2].text = "Weight"
        for cell in headers:
            cell.paragraphs[0].runs[0].bold = True

        data_rows = [
            ("🖼️ Visual Attraction", f"{visual_score:.1f}%", f"{weights['visual']}%"),
            ("🧠 Personality Match", f"{personality_score:.1f}%", f"{weights['personality']}%"),
            ("🧬 Genetic Chemistry", f"{hla_score:.1f}%", f"{weights['hla']}%"),
            ("⭐ OVERALL", f"{overall:.1f}%", "100%")
        ]

        for i, (comp, score, weight) in enumerate(data_rows, 1):
            row = summary_table.rows[i].cells
            row[0].text = comp
            row[1].text = score
            row[2].text = weight
            if "OVERALL" in comp:
                for cell in row:
                    cell.paragraphs[0].runs[0].bold = True

        doc.add_paragraph()

        # Vibe check
        vibe = analysis.get('ui_cards', {}).get('vibe_check', 'A unique connection.')
        vibe_para = doc.add_paragraph()
        vibe_para.add_run("💜 The Vibe: ").bold = True
        vibe_para.add_run(vibe).italic = True

        # Star sign description if available
        star_desc = analysis.get('star_sign_description', '')
        if star_desc:
            doc.add_paragraph()
            star_heading = doc.add_heading('✨ The Cosmic Connection', level=2)
            doc.add_paragraph(star_desc)

        # ═══════════════════════════════════════════════════════════════════
        # INDIVIDUAL PORTRAITS
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('👤 Individual Character Portraits', level=1)

        portraits = analysis.get('individual_portraits', {})
        
        # Person 1
        p1_heading = doc.add_heading(p1['name'], level=2)
        p1_heading.runs[0].font.color.rgb = RGBColor(0, 102, 204)  # Blue
        doc.add_paragraph(portraits.get(p1['name'], f"{p1['name']}'s personality profile."))
        
        # Person 1 sin scores summary
        p1_table = doc.add_table(rows=1, cols=4)
        p1_table.style = 'Light Grid Accent 1'
        hdr = p1_table.rows[0].cells
        hdr[0].text = "Trait"
        hdr[1].text = "Score"
        hdr[2].text = "Confidence"
        hdr[3].text = "Interpretation"
        
        for sin in self.SIN_ORDER:
            try:
                score = round(p1['sins'][sin]['score'], 2)
                conf = int(p1['sins'][sin].get('confidence', 0.8) * 100)
                interp = "Strong" if abs(score) > 3 else "Moderate" if abs(score) > 1 else "Neutral"
                row = p1_table.add_row().cells
                row[0].text = sin.capitalize()
                row[1].text = str(score)
                row[2].text = f"{conf}%"
                row[3].text = interp
            except (KeyError, TypeError):
                pass
        
        doc.add_paragraph()
        
        # Person 2
        p2_heading = doc.add_heading(p2['name'], level=2)
        p2_heading.runs[0].font.color.rgb = RGBColor(204, 0, 102)  # Pink
        doc.add_paragraph(portraits.get(p2['name'], f"{p2['name']}'s personality profile."))
        
        # Person 2 sin scores summary
        p2_table = doc.add_table(rows=1, cols=4)
        p2_table.style = 'Light Grid Accent 1'
        hdr = p2_table.rows[0].cells
        hdr[0].text = "Trait"
        hdr[1].text = "Score"
        hdr[2].text = "Confidence"
        hdr[3].text = "Interpretation"
        
        for sin in self.SIN_ORDER:
            try:
                score = round(p2['sins'][sin]['score'], 2)
                conf = int(p2['sins'][sin].get('confidence', 0.8) * 100)
                interp = "Strong" if abs(score) > 3 else "Moderate" if abs(score) > 1 else "Neutral"
                row = p2_table.add_row().cells
                row[0].text = sin.capitalize()
                row[1].text = str(score)
                row[2].text = f"{conf}%"
                row[3].text = interp
            except (KeyError, TypeError):
                pass

        # ═══════════════════════════════════════════════════════════════════
        # CONNECTION THEMES
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('🌟 Connection Themes', level=1)

        themes = analysis.get('themes', ['Analysis in progress'])
        theme_descs = analysis.get('ui_cards', {}).get('theme_descriptions', {})

        for i, theme in enumerate(themes, 1):
            theme_para = doc.add_paragraph()
            run = theme_para.add_run(f"{i}. {theme}")
            run.bold = True
            run.font.size = Pt(13)

            desc = theme_descs.get(theme, '')
            if desc:
                doc.add_paragraph(desc)

        # ═══════════════════════════════════════════════════════════════════
        # DEEP COMPATIBILITY ANALYSIS
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('🔮 Deep Compatibility Analysis', level=1)

        doc.add_heading('Overall Dynamics', level=2)
        doc.add_paragraph(analysis.get('deep_analysis', 'Analysis in progress.'))

        doc.add_heading('How They Perceive Each Other', level=2)
        doc.add_paragraph(analysis.get('perceived_similarity', 'Perception analysis in progress.'))

        # UI Cards
        ui_cards = analysis.get('ui_cards', {})
        if ui_cards:
            doc.add_paragraph()
            flags_table = doc.add_table(rows=5, cols=2)
            flags_table.style = 'Table Grid'
            
            flags_data = [
                ("🟢 Green Flag", ui_cards.get('green_flag', 'Shared values')),
                ("🔴 Red Flag", ui_cards.get('red_flag', 'Potential challenges')),
                ("💎 Secret Strength", ui_cards.get('secret_strength', 'Hidden potential')),
                ("📈 Growth Edge", ui_cards.get('growth_edge', 'Areas for development'))
            ]
            
            for i, (label, value) in enumerate(flags_data):
                row = flags_table.rows[i].cells
                row[0].text = label
                row[0].paragraphs[0].runs[0].bold = True
                row[1].text = value

        # ═══════════════════════════════════════════════════════════════════
        # VISUAL ANALYSIS (DETAILED)
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('🖼️ Visual Compatibility Analysis (Detailed)', level=1)

        doc.add_heading('Overview', level=2)
        visual_insight = analysis.get('visual_insight', 'Visual analysis provides baseline attraction assessment.')
        doc.add_paragraph(visual_insight)
        
        # Deep visual analysis
        visual_deep = analysis.get('visual_deep_analysis', '')
        if visual_deep:
            doc.add_heading('In-Depth Visual Analysis', level=2)
            doc.add_paragraph(visual_deep)

        # Visual scores breakdown
        doc.add_heading('Visual Metrics', level=2)
        visual_metrics_table = doc.add_table(rows=1, cols=2)
        visual_metrics_table.style = 'Light List Accent 1'
        hdr = visual_metrics_table.rows[0].cells
        hdr[0].text = "Metric"
        hdr[1].text = "Value"
        hdr[0].paragraphs[0].runs[0].bold = True
        hdr[1].paragraphs[0].runs[0].bold = True
        
        visual_metrics = [
            ("Mutual Attraction Score", f"{visual_score:.1f}%"),
            ("Analysis Method", visual_data.get('method', 'Meta-learning adaptation')),
            ("Confidence Level", f"{visual_data.get('confidence', 0.85) * 100:.0f}%")
        ]
        
        # Add image ratings if available
        if 'a_rates_b' in visual_data:
            visual_metrics.append((f"{p1['name']} rates {p2['name']}", f"{visual_data['a_rates_b']:.1f}%"))
        if 'b_rates_a' in visual_data:
            visual_metrics.append((f"{p2['name']} rates {p1['name']}", f"{visual_data['b_rates_a']:.1f}%"))
        
        for metric, value in visual_metrics:
            row = visual_metrics_table.add_row().cells
            row[0].text = metric
            row[1].text = str(value)

        # Add note about visual analysis
        if visual_data.get('note'):
            doc.add_paragraph()
            note_para = doc.add_paragraph()
            note_para.add_run("Note: ").bold = True
            note_para.add_run(visual_data['note']).italic = True
        
        # Calculation methodology
        doc.add_heading('Calculation Methodology', level=2)
        doc.add_paragraph(
            "Visual compatibility uses a three-stage approach: "
            "(1) Universal feature extraction from images using EfficientNet-B4, "
            "(2) Multi-task learning to predict attractiveness and quality scores, "
            "(3) Meta-learning adaptation based on user preferences. "
            f"The final mutual attraction score of {visual_score:.1f}% represents "
            "the geometric mean of bidirectional attraction, weighted at "
            f"{weights['visual']}% in the overall compatibility calculation."
        )

        # ═══════════════════════════════════════════════════════════════════
        # HLA GENETIC ANALYSIS (DETAILED)
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('🧬 HLA Genetic Compatibility Analysis (Detailed)', level=1)

        doc.add_heading('Overview', level=2)
        hla_insight = analysis.get('hla_insight', 'Genetic compatibility assessment based on HLA diversity.')
        doc.add_paragraph(hla_insight)
        
        # Deep HLA analysis
        hla_deep = analysis.get('hla_deep_analysis', '')
        if hla_deep:
            doc.add_heading('In-Depth Genetic Analysis', level=2)
            doc.add_paragraph(hla_deep)

        # HLA interpretation
        interp = hla_data.get('interpretation', 'No genetic data analyzed.')
        interp_para = doc.add_paragraph()
        interp_para.add_run("Biological Interpretation: ").bold = True
        interp_para.add_run(interp)

        # HLA locus breakdown table
        doc.add_heading('Locus-by-Locus Breakdown', level=2)
        breakdown = hla_data.get('breakdown', {})
        if breakdown:
            hla_table = doc.add_table(rows=1, cols=4)
            hla_table.style = 'Light Grid Accent 1'
            hdr = hla_table.rows[0].cells
            hdr[0].text = "Locus"
            hdr[1].text = "Dissimilarity"
            hdr[2].text = "Contribution"
            hdr[3].text = "Status"
            for cell in hdr:
                cell.paragraphs[0].runs[0].bold = True
            
            for locus, data in breakdown.items():
                if isinstance(data, dict):
                    row = hla_table.add_row().cells
                    row[0].text = locus
                    
                    if data.get('status') == 'no_data':
                        row[1].text = "N/A"
                        row[2].text = "N/A"
                        row[3].text = "No data"
                    else:
                        dissim = data.get('dissimilarity', 'N/A')
                        row[1].text = f"{dissim:.2f}" if isinstance(dissim, (int, float)) else str(dissim)
                        contrib = data.get('contribution', 'N/A')
                        row[2].text = f"{contrib:.1f}%" if isinstance(contrib, (int, float)) else str(contrib)
                        row[3].text = data.get('status', 'Analyzed')
            
            doc.add_paragraph()
        
        # HLA Calculation Methodology
        doc.add_heading('Calculation Methodology', level=2)
        doc.add_paragraph(
            "HLA compatibility is assessed by analyzing genetic markers on chromosome 6 "
            "(HLA-A, HLA-B, HLA-C, HLA-DRB1, HLA-DQB1). Optimal compatibility occurs at "
            "~55% dissimilarity (Wedekind et al., 1995), balancing immune diversity with "
            "genetic compatibility. The algorithm: "
            "(1) Parses genetic data to extract HLA alleles, "
            "(2) Calculates locus-specific dissimilarity scores, "
            "(3) Weights each locus contribution (Class I: 30% each, Class II: 20% each), "
            f"(4) Applies optimal dissimilarity curve to generate {hla_score:.1f}% compatibility score, "
            f"weighted at {weights['hla']}% in overall calculation."
        )
        
        # Birth control factor if present
        if 'adjusted_for_bc' in hla_data and hla_data['adjusted_for_bc']:
            bc_para = doc.add_paragraph()
            bc_para.add_run("⚠️ Adjustment Factor: ").bold = True
            bc_para.add_run(
                "Birth control use was indicated. Research suggests hormonal contraception "
                "may alter MHC preference perception. This score assumes natural (non-BC) conditions."
            )

        # ═══════════════════════════════════════════════════════════════════
        # PERSONALITY ANALYSIS (DETAILED)
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('🧠 Personality Compatibility Analysis (Detailed)', level=1)

        doc.add_heading('Similarity Calculation', level=2)
        doc.add_paragraph(
            f"Overall personality similarity: {personality_score:.1f}%"
        )
        doc.add_paragraph(
            "Personality compatibility uses the Seven Deadly Sins framework as a psychometric lens. "
            "Each person's responses to open-ended questions are analyzed by Gemini AI to extract "
            "trait scores (-5 to +5) with confidence levels. Similarity is calculated using: "
            "(1) Euclidean distance between trait vectors, "
            "(2) Cosine similarity for directional alignment, "
            "(3) Weighted average based on confidence scores. "
            f"The resulting {personality_score:.1f}% match score is weighted at "
            f"{weights['personality']}% in the overall compatibility calculation."
        )

        # ═══════════════════════════════════════════════════════════════════
        # DETAILED TRAIT ANALYSIS WITH Q&A EVIDENCE
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('📋 Detailed Trait Analysis with Evidence', level=1)
        
        doc.add_paragraph(
            "Below is a comprehensive breakdown of each personality trait (Seven Deadly Sins framework), "
            "showing how each person scored, the confidence level, and direct evidence from their questionnaire responses."
        )

        for sin in self.SIN_ORDER:
            doc.add_page_break()
            doc.add_heading(f"{sin.capitalize()}: {self.SIN_DESCRIPTIONS[sin]}", level=2)
            
            # Person 1 Analysis
            try:
                p1_score = round(p1['sins'][sin]['score'], 2)
                p1_conf = int(p1['sins'][sin].get('confidence', 0.8) * 100)
                p1_evidence = p1['sins'][sin].get('evidence', '')
                
                p1_heading = doc.add_paragraph()
                p1_run = p1_heading.add_run(f"👤 {p1['name']} — Score: {p1_score} | Confidence: {p1_conf}%")
                p1_run.bold = True
                p1_run.font.size = Pt(12)
                p1_run.font.color.rgb = RGBColor(0, 102, 204)
                
                # Interpretation
                if p1_score > 3:
                    interp = f"Strong tendency toward {sin}"
                elif p1_score > 1:
                    interp = f"Moderate tendency toward {sin}"
                elif p1_score < -3:
                    interp = f"Strong tendency toward opposite virtue"
                elif p1_score < -1:
                    interp = f"Moderate tendency toward opposite virtue"
                else:
                    interp = "Neutral - balanced approach"
                
                doc.add_paragraph(f"Interpretation: {interp}")
                
                # Evidence
                if p1_evidence:
                    ev_para = doc.add_paragraph()
                    ev_para.add_run("Evidence from responses: ").italic = True
                    ev_para.add_run(f'"{p1_evidence}"')
                    
            except (KeyError, TypeError) as e:
                logger.warning(f"Could not extract {sin} data for {p1['name']}: {e}")
                doc.add_paragraph(f"No data available for {p1['name']}")

            doc.add_paragraph()  # Spacer

            # Person 2 Analysis
            try:
                p2_score = round(p2['sins'][sin]['score'], 2)
                p2_conf = int(p2['sins'][sin].get('confidence', 0.8) * 100)
                p2_evidence = p2['sins'][sin].get('evidence', '')
                
                p2_heading = doc.add_paragraph()
                p2_run = p2_heading.add_run(f"👤 {p2['name']} — Score: {p2_score} | Confidence: {p2_conf}%")
                p2_run.bold = True
                p2_run.font.size = Pt(12)
                p2_run.font.color.rgb = RGBColor(204, 0, 102)
                
                # Interpretation
                if p2_score > 3:
                    interp = f"Strong tendency toward {sin}"
                elif p2_score > 1:
                    interp = f"Moderate tendency toward {sin}"
                elif p2_score < -3:
                    interp = f"Strong tendency toward opposite virtue"
                elif p2_score < -1:
                    interp = f"Moderate tendency toward opposite virtue"
                else:
                    interp = "Neutral - balanced approach"
                
                doc.add_paragraph(f"Interpretation: {interp}")
                
                # Evidence
                if p2_evidence:
                    ev_para = doc.add_paragraph()
                    ev_para.add_run("Evidence from responses: ").italic = True
                    ev_para.add_run(f'"{p2_evidence}"')
                    
            except (KeyError, TypeError) as e:
                logger.warning(f"Could not extract {sin} data for {p2['name']}: {e}")
                doc.add_paragraph(f"No data available for {p2['name']}")

            # Compatibility insight for this trait
            try:
                difference = abs(p1_score - p2_score)
                doc.add_paragraph()
                compat_para = doc.add_paragraph()
                compat_para.add_run("💡 Compatibility Insight: ").bold = True
                
                if difference < 1:
                    compat_para.add_run(
                        f"Very similar on {sin} (difference: {difference:.2f}). "
                        "Strong alignment in this area."
                    )
                elif difference < 2.5:
                    compat_para.add_run(
                        f"Moderate difference on {sin} (difference: {difference:.2f}). "
                        "Some variation that could be complementary."
                    )
                else:
                    compat_para.add_run(
                        f"Significant difference on {sin} (difference: {difference:.2f}). "
                        "Different approaches that may require understanding and compromise."
                    )
            except:
                pass

        # ═══════════════════════════════════════════════════════════════════
        # FULL QUESTIONNAIRE RESPONSES
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('📝 Complete Questionnaire Responses', level=1)
        
        doc.add_paragraph(
            "Below are the full question-and-answer pairs from both participants. "
            "These responses were analyzed to generate the personality profiles above."
        )

        # Person 1 Responses
        doc.add_heading(f"{p1['name']}'s Responses", level=2)
        p1_responses = p1.get('raw_responses', [])
        if p1_responses:
            for i, resp in enumerate(p1_responses, 1):
                q_para = doc.add_paragraph()
                q_run = q_para.add_run(f"Q{i}: {resp.get('question', 'No question')}")
                q_run.bold = True
                
                a_para = doc.add_paragraph(f"A: {resp.get('answer', 'No answer')}")
                a_para.style = 'Intense Quote'
                doc.add_paragraph()  # Spacer
        else:
            doc.add_paragraph("No response data available.")

        doc.add_page_break()

        # Person 2 Responses
        doc.add_heading(f"{p2['name']}'s Responses", level=2)
        p2_responses = p2.get('raw_responses', [])
        if p2_responses:
            for i, resp in enumerate(p2_responses, 1):
                q_para = doc.add_paragraph()
                q_run = q_para.add_run(f"Q{i}: {resp.get('question', 'No question')}")
                q_run.bold = True
                
                a_para = doc.add_paragraph(f"A: {resp.get('answer', 'No answer')}")
                a_para.style = 'Intense Quote'
                doc.add_paragraph()  # Spacer
        else:
            doc.add_paragraph("No response data available.")

        # ═══════════════════════════════════════════════════════════════════
        # FINAL VERDICT
        # ═══════════════════════════════════════════════════════════════════
        doc.add_page_break()
        doc.add_heading('💜 Final Compatibility Verdict', level=1)

        verdict = analysis.get('compatibility_verdict', 
                               'This pairing shows promise across multiple dimensions of compatibility.')
        verdict_para = doc.add_paragraph(verdict)
        verdict_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        # Final score reminder
        doc.add_paragraph()
        final_para = doc.add_paragraph()
        final_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        final_run = final_para.add_run(f"Overall Compatibility: {overall:.1f}%")
        final_run.bold = True
        final_run.font.size = Pt(16)
        final_run.font.color.rgb = RGBColor(138, 43, 226)

        # ═══════════════════════════════════════════════════════════════════
        # FOOTER
        # ═══════════════════════════════════════════════════════════════════
        doc.add_paragraph()
        doc.add_paragraph()
        footer = doc.add_paragraph()
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = footer.add_run("Generated by Harmonia Synthesis")
        run.italic = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(128, 128, 128)

        # Save
        doc.save(filename)
        logger.info(f"✅ Enhanced report saved: {filename}")
        return filename
'''

print("="*60)
print("✅ ENHANCED REPORT SERVICE CREATED")
print("="*60)
print()
print("New Features Added:")
print("  📋 Complete questionnaire Q&A pairs")
print("  🔬 Detailed HLA locus-by-locus breakdown")
print("  🖼️ Visual analysis with confidence & features")
print("  🧮 Calculation methodology for all components")
print("  💡 Per-trait compatibility insights")
print("  ⭐ Star sign titles and descriptions")
print("  👤 Individual character portraits")
print("  📊 Scoring interpretation for each trait")
print("  🎯 Evidence quotes linked to traits")
print("  💜 Final compatibility verdict")
print()
print("=" * 60)
