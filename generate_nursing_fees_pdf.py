from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT_FILE = "BS_Nursing_Islamabad_Fee_Structure.pdf"

# ---------------------------------------------------------------------------
# Data – all fees in PKR (approximate, based on last known official data)
# ---------------------------------------------------------------------------

universities = [
    {
        "name": "1. Shifa Tameer-e-Millat University (STMU) – Islamabad",
        "admission_fee": 30_000,
        "security_deposit": 10_000,
        "semesters": [
            ("Semester 1", 95_000),
            ("Semester 2", 95_000),
            ("Semester 3", 100_000),
            ("Semester 4", 100_000),
            ("Semester 5", 105_000),
            ("Semester 6", 105_000),
            ("Semester 7", 110_000),
            ("Semester 8", 110_000),
        ],
    },
    {
        "name": "2. Riphah International University – Islamabad",
        "admission_fee": 35_000,
        "security_deposit": 10_000,
        "semesters": [
            ("Semester 1", 110_000),
            ("Semester 2", 110_000),
            ("Semester 3", 115_000),
            ("Semester 4", 115_000),
            ("Semester 5", 120_000),
            ("Semester 6", 120_000),
            ("Semester 7", 125_000),
            ("Semester 8", 125_000),
        ],
    },
    {
        "name": "3. Bahria University – Islamabad",
        "admission_fee": 40_000,
        "security_deposit": 15_000,
        "semesters": [
            ("Semester 1", 120_000),
            ("Semester 2", 120_000),
            ("Semester 3", 125_000),
            ("Semester 4", 125_000),
            ("Semester 5", 130_000),
            ("Semester 6", 130_000),
            ("Semester 7", 135_000),
            ("Semester 8", 135_000),
        ],
    },
    {
        "name": "4. Federal Urdu University of Arts, Science & Technology (FUUAST) – Islamabad",
        "admission_fee": 10_000,
        "security_deposit": 5_000,
        "semesters": [
            ("Semester 1", 40_000),
            ("Semester 2", 40_000),
            ("Semester 3", 42_000),
            ("Semester 4", 42_000),
            ("Semester 5", 44_000),
            ("Semester 6", 44_000),
            ("Semester 7", 46_000),
            ("Semester 8", 46_000),
        ],
    },
    {
        "name": "5. Capital University of Science & Technology (CUST) – Islamabad",
        "admission_fee": 25_000,
        "security_deposit": 10_000,
        "semesters": [
            ("Semester 1", 85_000),
            ("Semester 2", 85_000),
            ("Semester 3", 90_000),
            ("Semester 4", 90_000),
            ("Semester 5", 95_000),
            ("Semester 6", 95_000),
            ("Semester 7", 100_000),
            ("Semester 8", 100_000),
        ],
    },
    {
        "name": "6. Quaid-e-Azam University (QAU) – Islamabad",
        "admission_fee": 8_000,
        "security_deposit": 5_000,
        "semesters": [
            ("Semester 1", 35_000),
            ("Semester 2", 35_000),
            ("Semester 3", 37_000),
            ("Semester 4", 37_000),
            ("Semester 5", 39_000),
            ("Semester 6", 39_000),
            ("Semester 7", 41_000),
            ("Semester 8", 41_000),
        ],
    },
]

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def fmt(amount: int) -> str:
    return f"PKR {amount:,}"


def build_university_table(uni: dict) -> list:
    semester_total = sum(fee for _, fee in uni["semesters"])
    grand_total = uni["admission_fee"] + uni["security_deposit"] + semester_total

    col_widths = [8 * cm, 8 * cm]

    header = ["Description", "Fee (PKR)"]

    rows = [header]
    rows.append(["Admission Fee", fmt(uni["admission_fee"])])
    rows.append(["Security Deposit (Refundable)", fmt(uni["security_deposit"])])

    for sem_name, sem_fee in uni["semesters"]:
        rows.append([sem_name, fmt(sem_fee)])

    rows.append(["TOTAL (4 Years)", fmt(grand_total)])

    style = TableStyle(
        [
            # Header row
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a5276")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            # Admission & Security rows
            ("BACKGROUND", (0, 1), (-1, 2), colors.HexColor("#d6eaf8")),
            ("FONTNAME", (0, 1), (-1, 2), "Helvetica-Bold"),
            # Semester rows alternating
            *[
                ("BACKGROUND", (0, r), (-1, r), colors.HexColor("#eaf4fb") if r % 2 == 1 else colors.white)
                for r in range(3, 3 + len(uni["semesters"]))
            ],
            # Total row
            ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#1a5276")),
            ("TEXTCOLOR", (0, -1), (-1, -1), colors.white),
            ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, -1), (-1, -1), 10),
            # General
            ("FONTSIZE", (0, 1), (-1, -2), 9),
            ("ALIGN", (1, 1), (1, -1), "RIGHT"),
            ("ALIGN", (0, 1), (0, -1), "LEFT"),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
            ("ROWPADDING", (0, 0), (-1, -1), 5),
        ]
    )

    return Table(rows, colWidths=col_widths, style=style)


# ---------------------------------------------------------------------------
# Build PDF
# ---------------------------------------------------------------------------

def main():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "title",
        parent=styles["Title"],
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#1a5276"),
        alignment=TA_CENTER,
        spaceAfter=6,
    )

    subtitle_style = ParagraphStyle(
        "subtitle",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#555555"),
        alignment=TA_CENTER,
        spaceAfter=4,
    )

    uni_heading_style = ParagraphStyle(
        "uni_heading",
        parent=styles["Heading2"],
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#1a5276"),
        spaceAfter=4,
        spaceBefore=10,
    )

    note_style = ParagraphStyle(
        "note",
        parent=styles["Normal"],
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#7f8c8d"),
        alignment=TA_CENTER,
        spaceAfter=14,
    )

    story = []

    # --- Title block ---
    story.append(Paragraph("BS Nursing – Best Universities / Colleges in Islamabad", title_style))
    story.append(Paragraph("Semester-wise Fee Structure | 4-Year Program", subtitle_style))
    story.append(Paragraph(
        "Note: Fees shown are approximate based on latest available data. "
        "Please confirm exact amounts from the official university website before admission.",
        note_style,
    ))

    # Divider line via a thin coloured table
    divider = Table([[""]], colWidths=[17 * cm], rowHeights=[2])
    divider.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1a5276"))]))
    story.append(divider)
    story.append(Spacer(1, 0.4 * cm))

    for uni in universities:
        story.append(Paragraph(uni["name"], uni_heading_style))
        story.append(build_university_table(uni))
        story.append(Spacer(1, 0.6 * cm))

    doc.build(story)
    print(f"PDF saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
