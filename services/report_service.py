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
        """Generate comprehensive compatibility report with in-depth analysis."""
        doc = Document()
        
        # Title Page
        title = doc.add_heading('Harmonia Compatibility Report', 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER

        subtitle = doc.add_paragraph()
        subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = subtitle.add_run(f"{p1['name']} & {p2['name']}")
        run.bold = True
        run.font.size = Pt(18)

        date_para = doc.add_paragraph()
        date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        date_para.add_run(f"Generated: {datetime.now().strftime('%B %d, %Y at %H:%M')}").italic = True
        doc.add_paragraph()

        # Executive Summary
        doc.add_heading('Executive Summary', level=1)
        visual_score = visual_data.get('mutual_attraction_score', 50)
        personality_score = similarity_result.get('percentage', 50)
        hla_score = hla_data.get('compatibility_score', 50)
        overall = (visual_score * weights['visual'] / 100 + personality_score * weights['personality'] / 100 + hla_score * weights['hla'] / 100)

        summary_table = doc.add_table(rows=5, cols=3)
        summary_table.style = 'Table Grid'
        headers = summary_table.rows[0].cells
        headers[0].text = "Component"
        headers[1].text = "Score"
        headers[2].text = "Weight"

        data_rows = [
            ("Visual Attraction", f"{visual_score:.1f}%", f"{weights['visual']}%"),
            ("Personality Match", f"{personality_score:.1f}%", f"{weights['personality']}%"),
            ("Genetic Chemistry", f"{hla_score:.1f}%", f"{weights['hla']}%"),
            ("OVERALL", f"{overall:.1f}%", "100%")
        ]

        for i, (comp, score, weight) in enumerate(data_rows, 1):
            row = summary_table.rows[i].cells
            row[0].text = comp
            row[1].text = score
            row[2].text = weight

        doc.add_paragraph()
        vibe = analysis.get('ui_cards', {}).get('vibe_check', 'A unique connection.')
        vibe_para = doc.add_paragraph()
        vibe_para.add_run("The Vibe: ").bold = True
        vibe_para.add_run(vibe).italic = True

        # Connection Themes
        doc.add_page_break()
        doc.add_heading('Connection Themes', level=1)
        themes = analysis.get('themes', ['Analysis in progress'])
        theme_descs = analysis.get('ui_cards', {}).get('theme_descriptions', {})
        for theme in themes:
            theme_para = doc.add_paragraph()
            theme_para.add_run(theme).bold = True
            desc = theme_descs.get(theme, '')
            if desc:
                doc.add_paragraph(desc)

        # Deep Analysis
        doc.add_page_break()
        doc.add_heading('Deep Compatibility Analysis', level=1)
        doc.add_heading('Overall Dynamics', level=2)
        doc.add_paragraph(analysis.get('deep_analysis', 'Analysis in progress.'))
        doc.add_heading('Mutual Perception', level=2)
        doc.add_paragraph(analysis.get('perceived_similarity', 'Perception analysis in progress.'))

        # Visual Analysis
        doc.add_page_break()
        doc.add_heading('Visual Compatibility Analysis', level=1)
        doc.add_paragraph(analysis.get('visual_insight', 'Visual analysis provides baseline attraction assessment.'))
        if visual_data.get('note'):
            note_para = doc.add_paragraph()
            note_para.add_run(f"Note: {visual_data['note']}").italic = True

        # HLA Analysis
        doc.add_page_break()
        doc.add_heading('HLA Genetic Compatibility Analysis', level=1)
        doc.add_paragraph(analysis.get('hla_insight', 'Genetic compatibility assessment based on HLA diversity.'))
        interp = hla_data.get('interpretation', 'No genetic data analyzed.')
        interp_para = doc.add_paragraph()
        interp_para.add_run("Interpretation: ").bold = True
        interp_para.add_run(interp)

        # Personality Trait Analysis
        doc.add_page_break()
        doc.add_heading('Detailed Personality Trait Analysis', level=1)
        for sin in self.SIN_ORDER:
            doc.add_heading(sin.capitalize(), level=2)
            try:
                p1_score = round(p1['sins'][sin]['score'], 2)
                p1_conf = int(p1['sins'][sin].get('confidence', 0.8) * 100)
                p1_evidence = p1['sins'][sin].get('evidence', '')
                
                p1_para = doc.add_paragraph()
                p1_run = p1_para.add_run(f"{p1['name']} (Score: {p1_score} | Confidence: {p1_conf}%)")
                p1_run.bold = True
                
                if p1_evidence:
                    ev_para = doc.add_paragraph()
                    ev_para.add_run("Evidence: ").italic = True
                    ev_para.add_run(f'"{p1_evidence}"')
            except (KeyError, TypeError):
                doc.add_paragraph(f"No data for {p1['name']}")

            try:
                p2_score = round(p2['sins'][sin]['score'], 2)
                p2_conf = int(p2['sins'][sin].get('confidence', 0.8) * 100)
                p2_evidence = p2['sins'][sin].get('evidence', '')
                
                p2_para = doc.add_paragraph()
                p2_run = p2_para.add_run(f"{p2['name']} (Score: {p2_score} | Confidence: {p2_conf}%)")
                p2_run.bold = True
                
                if p2_evidence:
                    ev_para = doc.add_paragraph()
                    ev_para.add_run("Evidence: ").italic = True
                    ev_para.add_run(f'"{p2_evidence}"')
            except (KeyError, TypeError):
                doc.add_paragraph(f"No data for {p2['name']}")

        # Questionnaire Responses
        doc.add_page_break()
        doc.add_heading('Complete Questionnaire Responses', level=1)
        doc.add_heading(f"{p1['name']}'s Responses", level=2)
        p1_responses = p1.get('raw_responses', [])
        if p1_responses:
            for i, resp in enumerate(p1_responses, 1):
                q_para = doc.add_paragraph()
                q_para.add_run(f"Q{i}: {resp.get('question', 'No question')}").bold = True
                doc.add_paragraph(f"A: {resp.get('answer', 'No answer')}")
                doc.add_paragraph()
        else:
            doc.add_paragraph("No response data available.")

        doc.add_page_break()
        doc.add_heading(f"{p2['name']}'s Responses", level=2)
        p2_responses = p2.get('raw_responses', [])
        if p2_responses:
            for i, resp in enumerate(p2_responses, 1):
                q_para = doc.add_paragraph()
                q_para.add_run(f"Q{i}: {resp.get('question', 'No question')}").bold = True
                doc.add_paragraph(f"A: {resp.get('answer', 'No answer')}")
                doc.add_paragraph()
        else:
            doc.add_paragraph("No response data available.")

        # Final Verdict
        doc.add_page_break()
        doc.add_heading('Final Compatibility Verdict', level=1)
        verdict = analysis.get('compatibility_verdict', 'This pairing shows promise across multiple dimensions of compatibility.')
        doc.add_paragraph(verdict)

        # Footer
        doc.add_paragraph()
        footer = doc.add_paragraph()
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = footer.add_run("Generated by Harmonia Synthesis")
        run.italic = True
        run.font.size = Pt(10)

        doc.save(filename)
        logger.info(f"Enhanced report saved: {filename}")
        return filename
