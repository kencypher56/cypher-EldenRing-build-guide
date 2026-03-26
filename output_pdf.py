"""
output_pdf.py - Generates a beautifully formatted Elden Ring Build Guide PDF using ReportLab
"""

import os
from typing import Any
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

OUTPUT_FILE = "elden_ring_build.pdf"

# ── Color Palette ─────────────────────────────────────────────────────────────
GOLD_DARK    = colors.HexColor("#B8860B")
GOLD_BRIGHT  = colors.HexColor("#DAA520")
GOLD_LIGHT   = colors.HexColor("#FFD700")
AMBER        = colors.HexColor("#FFBF00")
PARCHMENT    = colors.HexColor("#F5E6C8")
PARCHMENT_DK = colors.HexColor("#E8D5A3")
DARK_BG      = colors.HexColor("#1A1208")
DARK_PANEL   = colors.HexColor("#2A1F0E")
MID_BROWN    = colors.HexColor("#3D2B0F")
CRIMSON      = colors.HexColor("#8B0000")
TEAL         = colors.HexColor("#1A6B6B")
WHITE        = colors.white
OFF_WHITE    = colors.HexColor("#F0E8D0")
SHADOW_GREY  = colors.HexColor("#444444")


# ── Page Layout ───────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN_L = 2.2 * cm
MARGIN_R = 2.2 * cm
MARGIN_T = 2.5 * cm
MARGIN_B = 2.5 * cm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R


def _styles() -> dict:
    """Return all custom paragraph styles."""
    base = getSampleStyleSheet()

    def make(name, parent="Normal", **kw):
        return ParagraphStyle(name, parent=base[parent], **kw)

    return {
        "title": make("BuildTitle",
            fontSize=28, leading=34, alignment=TA_CENTER,
            textColor=GOLD_LIGHT, fontName="Helvetica-Bold",
            spaceAfter=4),
        "subtitle": make("BuildSubtitle",
            fontSize=13, leading=17, alignment=TA_CENTER,
            textColor=AMBER, fontName="Helvetica",
            spaceAfter=6),
        "section_header": make("SectionHeader",
            fontSize=16, leading=20, alignment=TA_LEFT,
            textColor=GOLD_BRIGHT, fontName="Helvetica-Bold",
            spaceBefore=14, spaceAfter=4),
        "sub_header": make("SubHeader",
            fontSize=12, leading=15, alignment=TA_LEFT,
            textColor=AMBER, fontName="Helvetica-Bold",
            spaceBefore=8, spaceAfter=3),
        "item_title": make("ItemTitle",
            fontSize=11, leading=14,
            textColor=GOLD_LIGHT, fontName="Helvetica-Bold",
            spaceBefore=4, spaceAfter=2),
        "body": make("Body",
            fontSize=9.5, leading=14, alignment=TA_JUSTIFY,
            textColor=OFF_WHITE, fontName="Helvetica",
            spaceAfter=3),
        "body_center": make("BodyCenter",
            fontSize=9.5, leading=14, alignment=TA_CENTER,
            textColor=OFF_WHITE, fontName="Helvetica"),
        "label": make("Label",
            fontSize=8.5, leading=12,
            textColor=AMBER, fontName="Helvetica-Bold"),
        "label_value": make("LabelValue",
            fontSize=8.5, leading=12,
            textColor=OFF_WHITE, fontName="Helvetica"),
        "pro": make("Pro",
            fontSize=9, leading=13,
            textColor=colors.HexColor("#6BCB77"), fontName="Helvetica"),
        "con": make("Con",
            fontSize=9, leading=13,
            textColor=colors.HexColor("#FF6B6B"), fontName="Helvetica"),
        "location": make("Location",
            fontSize=8.5, leading=12,
            textColor=colors.HexColor("#87CEEB"), fontName="Helvetica-Oblique"),
        "tip": make("Tip",
            fontSize=9.5, leading=14,
            textColor=PARCHMENT, fontName="Helvetica-Oblique",
            leftIndent=10, spaceAfter=4),
        "footer": make("Footer",
            fontSize=8, leading=10, alignment=TA_CENTER,
            textColor=SHADOW_GREY, fontName="Helvetica"),
        "note": make("Note",
            fontSize=8.5, leading=12, alignment=TA_CENTER,
            textColor=SHADOW_GREY, fontName="Helvetica-Oblique"),
    }


def _divider(color=GOLD_DARK, width=1):
    return HRFlowable(
        width="100%", thickness=width, color=color,
        spaceBefore=4, spaceAfter=4,
    )


def _spacer(h=6):
    return Spacer(1, h)


class PageDecorator:
    """Draws the dark background and golden border on every page."""

    def __init__(self, build_name: str):
        self.build_name = build_name

    def __call__(self, canvas: rl_canvas.Canvas, doc):
        canvas.saveState()
        # Full dark background
        canvas.setFillColor(DARK_BG)
        canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

        # Outer golden border
        canvas.setStrokeColor(GOLD_DARK)
        canvas.setLineWidth(2.5)
        pad = 10
        canvas.rect(pad, pad, PAGE_W - 2*pad, PAGE_H - 2*pad, fill=0, stroke=1)

        # Inner thin border
        canvas.setStrokeColor(AMBER)
        canvas.setLineWidth(0.5)
        pad2 = 14
        canvas.rect(pad2, pad2, PAGE_W - 2*pad2, PAGE_H - 2*pad2, fill=0, stroke=1)

        # Corner ornaments
        canvas.setFillColor(GOLD_BRIGHT)
        canvas.setFont("Helvetica-Bold", 14)
        for x, y in [(18, PAGE_H - 24), (PAGE_W - 24, PAGE_H - 24),
                     (18, 16), (PAGE_W - 24, 16)]:
            canvas.drawCentredString(x, y, "✦")

        # Footer: page number and build name
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(SHADOW_GREY)
        footer_y = 20
        canvas.drawCentredString(PAGE_W / 2, footer_y,
            f"{self.build_name}  ·  Cypher Elden Ring Build Guide  ·  Page {doc.page}")

        canvas.restoreState()


def _item_table(rows: list[tuple], col_widths=None) -> Table:
    """Create a styled 2-column label/value table."""
    if col_widths is None:
        col_widths = [3.5 * cm, CONTENT_W - 3.5 * cm]
    t = Table(rows, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), DARK_PANEL),
        ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#0F0A05")),
        ("TEXTCOLOR", (0, 0), (0, -1), AMBER),
        ("TEXTCOLOR", (1, 0), (1, -1), OFF_WHITE),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("LEADING", (0, 0), (-1, -1), 13),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (0, -1), 8),
        ("LEFTPADDING", (1, 0), (1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.3, GOLD_DARK),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [DARK_PANEL, colors.HexColor("#150E03")]),
    ]))
    return t


def _section_banner(text: str, S: dict) -> list:
    """Return a visually distinct section banner."""
    elems = []
    elems.append(_spacer(10))
    elems.append(_divider(GOLD_BRIGHT, 1.5))
    elems.append(Paragraph(f"⚜  {text.upper()}  ⚜", S["section_header"]))
    elems.append(_divider(GOLD_DARK, 0.5))
    elems.append(_spacer(4))
    return elems


def _pros_cons_location(pros: list, cons: list, location: str, S: dict) -> list:
    """Render pros, cons, and location paragraph list."""
    elems = []
    if pros:
        for p in pros:
            elems.append(Paragraph(f"✓  {p}", S["pro"]))
    if cons:
        for c in cons:
            elems.append(Paragraph(f"✗  {c}", S["con"]))
    if location:
        elems.append(Paragraph(f"📍  {location}", S["location"]))
    return elems


# ── Cover Page ────────────────────────────────────────────────────────────────
def _build_cover(build: dict, S: dict) -> list:
    elems = []
    elems.append(_spacer(60))

    # Title
    elems.append(Paragraph("⚔  ELDEN RING  ⚔", S["title"]))
    elems.append(Paragraph("BUILD GUIDE", S["title"]))
    elems.append(_spacer(12))
    elems.append(_divider(GOLD_BRIGHT, 2))
    elems.append(_spacer(8))

    build_name = build.get("build_name", "Tarnished's Path")
    elems.append(Paragraph(build_name, S["subtitle"]))
    elems.append(_spacer(6))

    desc = build.get("build_description", "")
    elems.append(Paragraph(desc, S["body_center"]))
    elems.append(_spacer(20))

    meta = build.get("_meta", {})
    info_data = [
        ["Class", meta.get("class", "Unknown")],
        ["Primary Stat", build.get("primary_attribute", "—")],
        ["Secondary Stat", build.get("secondary_attribute", "—")],
        ["Model", build.get("_meta", {}).get("model", "deepseek-r1:8b")],
    ]
    rows = [(Paragraph(k, S["label"]), Paragraph(v, S["label_value"])) for k, v in info_data]
    t = _item_table(rows, [4 * cm, CONTENT_W - 4 * cm])
    elems.append(t)

    elems.append(_spacer(30))
    elems.append(Paragraph(
        "Generated by Cypher Elden Ring Build Guide · deepseek-r1:8b · Ollama",
        S["note"]
    ))
    elems.append(PageBreak())
    return elems


# ── Stats Section ─────────────────────────────────────────────────────────────
STAT_ICONS = {
    "Vigor": "❤", "Mind": "💧", "Endurance": "⚡",
    "Strength": "💪", "Dexterity": "🗡", "Intelligence": "✨",
    "Faith": "☀", "Arcane": "🔮",
}

PRIORITY_COLORS = {"High": "#FF6B6B", "Medium": "#FFBF00", "Low": "#6BCB77"}


def _build_stats_section(build: dict, S: dict) -> list:
    elems = []
    elems += _section_banner("Stat Recommendations & Rune Allocation", S)

    strategy = build.get("rune_allocation_strategy", "")
    if strategy:
        elems.append(Paragraph(f"Strategy: {strategy}", S["body"]))
        elems.append(_spacer(6))

    recs = build.get("stat_recommendations", [])
    if recs:
        header = [
            Paragraph("Attribute", S["label"]),
            Paragraph("Current", S["label"]),
            Paragraph("Target", S["label"]),
            Paragraph("Priority", S["label"]),
            Paragraph("Reason", S["label"]),
        ]
        col_w = [3.2*cm, 1.8*cm, 1.8*cm, 2.2*cm, CONTENT_W - 9*cm]
        data = [header]
        for rec in recs:
            stat = rec.get("stat", "")
            icon = STAT_ICONS.get(stat, "•")
            pri = rec.get("priority", "Medium")
            pri_color = PRIORITY_COLORS.get(pri, "#FFBF00")
            data.append([
                Paragraph(f"{icon}  {stat}", S["label_value"]),
                Paragraph(str(rec.get("current", "?")), S["body_center"]),
                Paragraph(str(rec.get("recommended", "?")), S["body_center"]),
                Paragraph(f'<font color="{pri_color}">{pri}</font>', S["label_value"]),
                Paragraph(rec.get("reason", ""), S["body"]),
            ])

        t = Table(data, colWidths=col_w)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), MID_BROWN),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [DARK_PANEL, colors.HexColor("#150E03")]),
            ("TEXTCOLOR", (0, 0), (-1, 0), GOLD_LIGHT),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8.5),
            ("LEADING", (0, 0), (-1, -1), 12),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("GRID", (0, 0), (-1, -1), 0.3, GOLD_DARK),
            ("ALIGN", (1, 0), (2, -1), "CENTER"),
            ("ALIGN", (3, 0), (3, -1), "CENTER"),
        ]))
        elems.append(t)

    level_prog = build.get("level_progression", "")
    if level_prog:
        elems.append(_spacer(8))
        elems.append(Paragraph(f"Level Progression:  {level_prog}", S["tip"]))

    return elems


# ── Weapons Section ───────────────────────────────────────────────────────────
def _build_weapons_section(build: dict, S: dict) -> list:
    elems = []
    elems += _section_banner("Recommended Weapons", S)

    weapons = build.get("weapons", [])
    for i, w in enumerate(weapons[:3], 1):
        elems.append(KeepTogether([
            Paragraph(f"⚔  {i}. {w.get('name', 'Unknown Weapon')}", S["sub_header"]),
            _item_table([
                (Paragraph("Type", S["label"]), Paragraph(w.get("type", "—"), S["label_value"])),
                (Paragraph("Scaling", S["label"]), Paragraph(w.get("scaling", "—"), S["label_value"])),
                (Paragraph("Requires", S["label"]), Paragraph(w.get("requirement", "—"), S["label_value"])),
                (Paragraph("Ash of War", S["label"]), Paragraph(w.get("ash_of_war", "—"), S["label_value"])),
            ]),
        ]))
        elems += _pros_cons_location(
            w.get("pros", []), w.get("cons", []), w.get("location", ""), S
        )
        if i < len(weapons):
            elems.append(_spacer(8))

    return elems


# ── Armor Section ─────────────────────────────────────────────────────────────
def _build_armor_section(build: dict, S: dict) -> list:
    elems = []
    elems += _section_banner("Recommended Armor Sets", S)

    armor_sets = build.get("armor_sets", [])
    for i, a in enumerate(armor_sets[:3], 1):
        elems.append(KeepTogether([
            Paragraph(f"🛡  {i}. {a.get('name', 'Unknown Armor')}", S["sub_header"]),
            _item_table([
                (Paragraph("Type", S["label"]), Paragraph(a.get("type", "—"), S["label_value"])),
                (Paragraph("Poise", S["label"]), Paragraph(str(a.get("poise", "—")), S["label_value"])),
                (Paragraph("Weight", S["label"]), Paragraph(str(a.get("weight", "—")), S["label_value"])),
            ]),
        ]))
        elems += _pros_cons_location(
            a.get("pros", []), a.get("cons", []), a.get("location", ""), S
        )
        if i < len(armor_sets):
            elems.append(_spacer(8))

    return elems


# ── Talismans Section ─────────────────────────────────────────────────────────
def _build_talismans_section(build: dict, S: dict) -> list:
    elems = []
    elems += _section_banner("Recommended Talismans", S)

    talismans = build.get("talismans", [])
    for i, t in enumerate(talismans[:8], 1):
        elems.append(KeepTogether([
            Paragraph(f"✦  {i}. {t.get('name', 'Unknown Talisman')}", S["sub_header"]),
            Paragraph(t.get("effect", ""), S["body"]),
        ] + _pros_cons_location(
            t.get("pros", []), t.get("cons", []), t.get("location", ""), S
        )))
        if i < len(talismans):
            elems.append(_spacer(4))

    return elems


# ── Great Runes Section ───────────────────────────────────────────────────────
def _build_great_runes_section(build: dict, S: dict) -> list:
    elems = []
    elems += _section_banner("Great Rune Recommendations", S)

    great_runes = build.get("great_runes", [])
    for i, gr in enumerate(great_runes[:2], 1):
        elems.append(KeepTogether([
            Paragraph(f"★  {i}. {gr.get('name', 'Unknown Great Rune')}", S["sub_header"]),
            _item_table([
                (Paragraph("Holder", S["label"]), Paragraph(gr.get("holder", "—"), S["label_value"])),
                (Paragraph("Effect", S["label"]), Paragraph(gr.get("effect", "—"), S["label_value"])),
            ]),
        ]))
        elems += _pros_cons_location(
            gr.get("pros", []), gr.get("cons", []), gr.get("location", ""), S
        )
        if i < len(great_runes):
            elems.append(_spacer(8))

    return elems


# ── Gameplay Tips ─────────────────────────────────────────────────────────────
def _build_tips_section(build: dict, S: dict) -> list:
    elems = []
    tips = build.get("gameplay_tips", [])
    if not tips:
        return elems

    elems += _section_banner("Gameplay Tips & Strategies", S)
    for tip in tips:
        elems.append(Paragraph(f"➤  {tip}", S["tip"]))

    return elems


# ── Master Build Function ─────────────────────────────────────────────────────
def generate_pdf(build: dict, output_path: str = OUTPUT_FILE) -> str:
    """Generate the complete Elden Ring Build Guide PDF."""
    S = _styles()
    build_name = build.get("build_name", "Tarnished's Path")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T,
        bottomMargin=MARGIN_B,
        title=f"Elden Ring Build Guide — {build_name}",
        author="Cypher Build Guide (deepseek-r1:8b)",
        subject="Elden Ring Character Build",
    )

    story = []

    # Cover
    story += _build_cover(build, S)

    # Stats
    story += _build_stats_section(build, S)
    story.append(_spacer(10))

    # Weapons
    story += _build_weapons_section(build, S)
    story.append(_spacer(10))

    # Armor
    story += _build_armor_section(build, S)
    story.append(_spacer(10))

    # Talismans
    story += _build_talismans_section(build, S)
    story.append(_spacer(10))

    # Great Runes
    story += _build_great_runes_section(build, S)
    story.append(_spacer(10))

    # Tips
    story += _build_tips_section(build, S)

    # Final rule
    story.append(_spacer(20))
    story.append(_divider(GOLD_BRIGHT, 1.5))
    story.append(Paragraph(
        "May your runes guide thee, and may the grace of gold ever shine upon your path.",
        S["footer"]
    ))

    # Build PDF
    decorator = PageDecorator(build_name)
    doc.build(story, onFirstPage=decorator, onLaterPages=decorator)

    return output_path