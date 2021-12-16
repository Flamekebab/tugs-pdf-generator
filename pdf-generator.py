# We'll be using ReportLab to generate PDFs as that's currently what I've got
# If something else is a better fit then I definitely want to hear about it!
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.lib import utils
from reportlab.lib.units import mm
from reportlab.platypus import Frame, Image
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os


def main(output_filename: str ="test.pdf"):
    ''' (TODO: description

    :param output_filename: The path the finished PDF will be written to.

    '''

    canvas = Canvas(output_filename)

    # Ridgeline for the titles
    # Source Sans Pro for the body text
    fonts = (
        ("Ridgeline", "./fonts/Ridgeline.ttf"),
        ("SSP", "./fonts/SourceSansPro-Regular.ttf"),
        ("SSP Italic", "./fonts/SourceSansPro-It.ttf"),
        ("SSP Bold", "./fonts/SourceSansPro-Bold.ttf"),
        ("SSP Bold Italic", "./fonts/SourceSansPro-BoldIt.ttf")
    )

    for font in fonts:
        add_font(font[0], font[1])

    # addMapping amends SSP to have multiple styles - rather than switching font when the style changes.
    # addMapping(face, bold, italic, psname)
    addMapping('SSP', 0, 0, 'SSP')  # normal
    addMapping('SSP', 0, 1, 'SSP Italic')  # italic
    addMapping('SSP', 1, 0, 'SSP Bold')  # bold
    addMapping('SSP', 1, 1, 'SSP Bold Italic')  # italic and bold

    # From now on we can use the syntax "canvas.setFont("Ridgeline", 32)" to set the font and size
    canvas.setFont("Ridgeline", 18)
    #canvas.drawString(72, 72, "Hello, World")


    # Building a stylesheet from scratch is a hassle, instead we use the sample stylsheet as a base
    styles = getSampleStyleSheet()
    # To see the various options use
    #print(styles.list())

    # Needed things - H1, H2, body text
    h1 = ParagraphStyle(
        'document_title',
        parent=styles['Heading1'],
        fontName="Ridgeline",
        fontSize=50,
        alignment=1,
        spaceAfter=50,
        )
    h2 = ParagraphStyle(
        'subheading',
        parent=styles['Heading3'],
        fontName="Ridgeline",
        fontSize=20,
        alignment=0,
        spaceAfter=20,
        )
    body_paragraph = ParagraphStyle(
        'body_text',
        parent=styles['BodyText'],
        fontName="SSP",
        fontSize=14,
        alignment=4, # page 77 of the Reference PDF (4 = justify)
        spaceAfter=14,
        bulletFontName="SSP"
        )
    styles.add(h1)
    styles.add(h2)
    styles.add(body_paragraph)


    # These dimensions worked out from existing PDFs
    doc = BaseDocTemplate('test.pdf', showBoundary=1, leftMargin=14.5 * mm, rightMargin=14.5 * mm, bottomMargin=35 * mm, topMargin=30 * mm)

    # As yet undecided on whether to allow header paragraphs (all bold SSP, centre aligned)
    # If so push the paragraphs down.
    header_paragraph = False
    if header_paragraph:
        body_text_height = doc.height * 0.9
    else:
        body_text_height = doc.height

    frame1 = Frame(doc.leftMargin, doc.bottomMargin, doc.width / 2 - 6, body_text_height, id='col1')
    frame2 = Frame(doc.leftMargin + doc.width / 2 + 6, doc.bottomMargin, doc.width / 2 - 6, body_text_height, id='col2')

    paragraphs = []

    bacon_ipsum = """Pork belly ut enim aliquip andouille irure. Ground round velit brisket shoulder, eiusmod tri-tip dolor. Minim rump beef, tenderloin voluptate do capicola labore landjaeger ea quis bacon et. Pork chop tempor shankle hamburger nulla.

    Cow ut doner ipsum fugiat aliquip. Proident pork loin minim nostrud bacon, beef ball tip ullamco. Short loin porchetta pig, dolore nulla ex ut ham hock kielbasa bresaola swine ipsum excepteur tongue veniam. Dolor doner ball tip, tail tenderloin capicola nostrud bacon. Quis shankle t-bone kevin, anim officia sunt excepteur corned beef short ribs spare ribs laboris in voluptate. Pancetta sunt pork chop burgdoggen tenderloin frankfurter. Brisket fugiat adipisicing filet mignon.

    Velit spare ribs alcatra, excepteur in filet mignon ground round nostrud frankfurter drumstick tail.Leberkas in in brisket venison ribeye nostrud sunt quis spare ribs ullamco nisi adipisicing boudin pig. Cow meatloaf eu flank, pancetta magna commodo enim strip steak in. Chuck quis spare ribs turducken, capicola beef brisket salami doner.

    Aliqua tri-tip shankle ribeye hamburger jerky filet mignon pork chop turkey. Aliquip flank mollit eiusmod. Veniam tempor reprehenderit laboris. Quis jerky dolor, picanha esse irure tempor ut laboris biltong. Qui labore tail minim cupidatat turkey aute eu anim porchetta. Biltong ball tip porchetta, non cupim t-bone deserunt consectetur ad irure pig shankle tri-tip frankfurter beef ribs.

    Swine pork belly rump, nostrud ham hock cow boudin. Adipisicing dolore capicola in dolor hamburger. Cupidatat reprehenderit drumstick chislic tri-tip short loin aliqua buffalo tail burgdoggen pork fugiat porchetta. Nostrud eiusmod proident pork chop. Andouille alcatra dolor cow dolore porchetta."""

    paragraphs.append(Paragraph("Heading 1", styles['document_title']))
    paragraphs.append(Paragraph(bacon_ipsum, styles['body_text']))
    paragraphs.append(Paragraph("Heading 2", styles['subheading']))
    paragraphs.append(Paragraph(bacon_ipsum, styles['body_text']))
    doc.addPageTemplates([PageTemplate(id='TwoCol', frames=[frame1, frame2]), ])

    doc.build(paragraphs)

    #canvas.save()


def add_font(name: str, path: str):
    ''' Non-default fonts must be registered before use in PDF generation.

    :param name: The name you want the font registered as (can be different from the font's original name)

    :param path: Either an absolute path to the font's TTF file or a path relative to where this function is run.

    '''
    pdfmetrics.registerFont(TTFont(name, path))


if __name__ == "__main__":
    main()
