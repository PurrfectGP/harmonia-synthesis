
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ReportService:
    """Generate comprehensive Word document reports."""

    SIN_ORDER = ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]

    def generate_full_report(self, p1: dict, p2: dict, analysis: dict,
                             visual_data: dict, hla_data: dict,
                             similarity_result: dict, weights: dict,
                             filename: str) -> str:
        """
        Generate a comprehensive compatibility report.

        Includes:
        - Executive summary with overall score
        - Visual analysis results
        - Personality analysis with evidence
        - HLA genetic compatibility
        - Connection themes and deep analysis
        """
        doc = Document()

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

        summary_table = doc.add_table(rows=5, cols=3)
        summary_table.style = 'Table Grid'

        headers = summary_table.rows[0].cells
        headers[0].text = "Component"
        headers[1].text = "Score"
        headers[2].text = "Weight"

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

        doc.add_paragraph()

        # Vibe check
        vibe = analysis.get('ui_cards', {}).get('vibe_check', 'A unique connection.')
        vibe_para = doc.add_paragraph()
        vibe_para.add_run("The Vibe: ").bold = True
        vibe_para.add_run(vibe).italic = True

        # ═══════════════════════════════════════════════════════════════════
        # CONNECTION THEMES
        # ═══════════════════════════════════════════════════════════════════
        doc.add_heading('Connection Themes', level=1)

        themes = analysis.get('themes', ['Analysis in progress'])
        theme_descs = analysis.get('ui_cards', {}).get('theme_descriptions', {})

        for theme in themes:
            theme_para = doc.add_paragraph(style='Intense Quote')
            theme_para.add_run(theme)

            desc = theme_descs.get(theme, '')
            if desc:
                doc.add_paragraph(desc)

        # ═══════════════════════════════════════════════════════════════════
        # VISUAL ANALYSIS
        # ═══════════════════════════════════════════════════════════════════
        doc.add_heading('Visual Compatibility Analysis', level=1)

        visual_insight = analysis.get('visual_insight', 'Visual analysis provides baseline attraction assessment.')
        doc.add_paragraph(visual_insight)

        if visual_data.get('note'):
            note_para = doc.add_paragraph()
            note_para.add_run(f"Note: {visual_data['note']}").italic = True

        # ═══════════════════════════════════════════════════════════════════
        # PERSONALITY DEEP ANALYSIS
        # ═══════════════════════════════════════════════════════════════════
        doc.add_heading('Personality Compatibility Analysis', level=1)

        doc.add_heading('Deep Analysis', level=2)
        doc.add_paragraph(analysis.get('deep_analysis', 'Analysis in progress.'))

        doc.add_heading('Mutual Perception', level=2)
        doc.add_paragraph(analysis.get('perceived_similarity', 'Perception analysis in progress.'))

        # ═══════════════════════════════════════════════════════════════════
        # PSYCHOMETRIC EVIDENCE
        # ═══════════════════════════════════════════════════════════════════
        doc.add_heading('Detailed Psychometric Evidence', level=1)

        for sin in self.SIN_ORDER:
            doc.add_heading(sin.capitalize(), level=2)

            # Person 1
            try:
                p1_score = round(p1['sins'][sin]['score'], 2)
                p1_conf = int(p1['sins'][sin].get('confidence', 0.8) * 100)
                p1_evidence = p1['sins'][sin].get('evidence_list', [])
            except (KeyError, TypeError):
                p1_score, p1_conf, p1_evidence = 0, 50, []

            p1_para = doc.add_paragraph()
            run = p1_para.add_run(f"{p1['name']} (Score: {p1_score} | Confidence: {p1_conf}%)")
            run.bold = True
            run.font.color.rgb = RGBColor(0, 51, 204)  # Blue

            for ev in p1_evidence:
                doc.add_paragraph(ev, style='List Bullet')

            # Person 2
            try:
                p2_score = round(p2['sins'][sin]['score'], 2)
                p2_conf = int(p2['sins'][sin].get('confidence', 0.8) * 100)
                p2_evidence = p2['sins'][sin].get('evidence_list', [])
            except (KeyError, TypeError):
                p2_score, p2_conf, p2_evidence = 0, 50, []

            p2_para = doc.add_paragraph()
            run = p2_para.add_run(f"{p2['name']} (Score: {p2_score} | Confidence: {p2_conf}%)")
            run.bold = True
            run.font.color.rgb = RGBColor(204, 0, 102)  # Pink

            for ev in p2_evidence:
                doc.add_paragraph(ev, style='List Bullet')

        # ═══════════════════════════════════════════════════════════════════
        # HLA GENETIC ANALYSIS
        # ═══════════════════════════════════════════════════════════════════
        doc.add_heading('HLA Genetic Compatibility Analysis', level=1)

        hla_insight = analysis.get('hla_insight', 'Genetic compatibility assessment based on HLA diversity.')
        doc.add_paragraph(hla_insight)

        interp = hla_data.get('interpretation', 'No genetic data analyzed.')
        interp_para = doc.add_paragraph()
        interp_para.add_run("Interpretation: ").bold = True
        interp_para.add_run(interp)

        # Breakdown table if available
        breakdown = hla_data.get('breakdown', {})
        if breakdown:
            doc.add_paragraph()  # Spacer
            for locus, data in breakdown.items():
                if isinstance(data, dict) and data.get('status') != 'no_data':
                    locus_para = doc.add_paragraph()
                    locus_para.add_run(f"{locus}: ").bold = True
                    dissim = data.get('dissimilarity', 'N/A')
                    locus_para.add_run(f"Dissimilarity = {dissim}")

        # ═══════════════════════════════════════════════════════════════════
        # FLAGS
        # ═══════════════════════════════════════════════════════════════════
        doc.add_heading('Compatibility Flags', level=1)

        ui_cards = analysis.get('ui_cards', {})

        green = doc.add_paragraph()
        green.add_run("🟢 Green Flag: ").bold = True
        green.add_run(ui_cards.get('green_flag', 'Shared values and interests'))

        red = doc.add_paragraph()
        red.add_run("🔴 Red Flag: ").bold = True
        red.add_run(ui_cards.get('red_flag', 'Potential communication challenges'))

        # ═══════════════════════════════════════════════════════════════════
        # FOOTER
        # ═══════════════════════════════════════════════════════════════════
        doc.add_paragraph()  # Spacer
        footer = doc.add_paragraph()
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = footer.add_run("Generated by Harmonia Synthesis")
        run.italic = True
        run.font.size = Pt(10)

        # Save
        doc.save(filename)
        logger.info(f"Report saved: {filename}")
        return filename
