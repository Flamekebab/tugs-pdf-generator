from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.lib.units import mm, cm
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Image
from reportlab.pdfgen.canvas import Canvas


def frontpage_generator(body_text_input: str, output_filename: str = "test.pdf"):
    """ Generates PDFs with arbitrary text content for merging with existing blank PDFs.

    :param body_text_input: Currently any old string - to be modified later

    :param output_filename: The path the finished PDF will be written to.

    """

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

    # Add the style elements
    add_tugs_style()
    # These dimensions worked out from existing PDFs
    doc = BaseDocTemplate(
        output_filename,
        showBoundary=0,
        leftMargin=14.5 * mm,
        rightMargin=14.5 * mm,
        bottomMargin=35 * mm,
        topMargin=30 * mm)


    # As yet undecided on whether to allow header paragraphs (all bold SSP, centre aligned)
    # If so push the paragraphs down.
    header_paragraph = False
    if header_paragraph:
        body_text_height = doc.height * 0.9
    else:
        body_text_height = doc.height

    frame1 = Frame(doc.leftMargin, doc.bottomMargin, doc.width / 2 - 6, body_text_height, id='col1')
    frame2 = Frame(doc.leftMargin + doc.width / 2 + 6, doc.bottomMargin, doc.width / 2 - 6, body_text_height, id='col2')

    # paragraphs is a list of ReportLab Paragraph objects
    paragraphs = []

    # The body_text_input may need processing as it comes in - it'll depend on how much heavy lifting the GUI does
    # e.g. converting "<h2>subheading</h2> some body text" to [('h2', 'subheading'), ('body', 'some body text')]
    # We may also want to limit the amount of allowed input

    # <br/> tags work but <br> causes errors

    # Test formatting
    # paragraphs.append(Image(footer, width=19.5 * cm))
    paragraphs.append(Paragraph("Heading 1", styles['document_title']))
    paragraphs.append(Paragraph(body_text_input, styles['body_text']))
    paragraphs.append(Paragraph("Heading 2", styles['subheading']))
    paragraphs.append(Paragraph(body_text_input, styles['body_text']))
    paragraphs.append(Paragraph(body_text_input, styles['body_text']))
    ####

    # The table of contents (ToC) will always be on a new page:
    paragraphs.append(PageBreak())


    def add_header_footer(canvas, doc):
        # The coordinates end up a bit strange with the images
        canvas.translate(16,-265)
        if canvas.getPageNumber() % 2 == 0:
            footer = footer_l
            header = header_l
            page_num_x = 1.3 * cm
            page_num_y = 1.3 * cm
        else:
            footer = footer_r
            header = header_r
            page_num_x = 19.3 * cm
            page_num_y = 1.3 * cm
        canvas.drawImage(footer, 0 * cm, 0 * cm, width=19.9 * cm, preserveAspectRatio=True, anchor='c')
        canvas.drawImage(header, 0.07 * cm, 26.56 * cm, width=19.8 * cm, preserveAspectRatio=True, anchor='c')

        # Reset the coordinates for text
        canvas.translate(-16, 265)
        canvas.setFont("Ridgeline", 30)

        canvas.drawString(page_num_x, page_num_y, str(canvas.getPageNumber()))


    header_r = "./headers-footers/top-bar-R.jpg"
    header_l = "./headers-footers/top-bar-L.jpg"
    footer_r = "./headers-footers/bottom-bar-R.jpg"
    footer_l = "./headers-footers/bottom-bar-L.jpg"


    # As far as I can see, so far, ReportLab only supports links with anchors (and we're not adding those!)
    # TODO: Split the PDFs by type (from metadata keywords)
    # Provide a list of PDFs


    page_template = PageTemplate(id='TwoCol', frames=[frame1, frame2], onPageEnd=add_header_footer)
    doc.addPageTemplates(page_template)

    doc.build(paragraphs)


def add_font(name: str, path: str):
    """ Non-default fonts must be registered before use in PDF generation.

    :param name: The name you want the font registered as (can be different from the font's original name)

    :param path: Either an absolute path to the font's TTF file or a path relative to where this function is run.

    """
    pdfmetrics.registerFont(TTFont(name, path))


def add_tugs_style():
    """ Abstracting this out to make changes to the style easier.

    """

    # The sample stylesheet provides a base
    global styles
    styles = getSampleStyleSheet()
    # To see the various existing style components use:
    # print(styles.list())

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
        fontSize=12,
        alignment=4,  # page 77 of the Reference PDF (4 = justify)
        spaceAfter=12,
        bulletFontName="SSP"
        )
    styles.add(h1)
    styles.add(h2)
    styles.add(body_paragraph)


if __name__ == "__main__":
    bacon_ipsum = """Pork belly ut enim aliquip andouille irure. Ground round velit brisket shoulder, eiusmod tri-tip dolor. Minim rump beef, tenderloin voluptate do capicola labore landjaeger ea quis bacon et. Pork chop tempor shankle hamburger nulla.

        Cow ut doner ipsum fugiat aliquip. Proident pork loin minim nostrud bacon, beef ball tip ullamco. Short loin porchetta pig, dolore nulla ex ut ham hock kielbasa bresaola swine ipsum excepteur tongue veniam. Dolor doner ball tip, tail tenderloin capicola nostrud bacon. Quis shankle t-bone kevin, anim officia sunt excepteur corned beef short ribs spare ribs laboris in voluptate. Pancetta sunt pork chop burgdoggen tenderloin frankfurter. Brisket fugiat adipisicing filet mignon.

        Velit spare ribs alcatra, excepteur in filet mignon ground round nostrud frankfurter drumstick tail.Leberkas in in brisket venison ribeye nostrud sunt quis spare ribs ullamco nisi adipisicing boudin pig. Cow meatloaf eu flank, pancetta magna commodo enim strip steak in. Chuck quis spare ribs turducken, capicola beef brisket salami doner.

        Aliqua tri-tip shankle ribeye hamburger jerky filet mignon pork chop turkey. Aliquip flank mollit eiusmod. Veniam tempor reprehenderit laboris. Quis jerky dolor, picanha esse irure tempor ut laboris biltong. Qui labore tail minim cupidatat turkey aute eu anim porchetta. Biltong ball tip porchetta, non cupim t-bone deserunt consectetur ad irure pig shankle tri-tip frankfurter beef ribs.

        Swine pork belly rump, nostrud ham hock cow boudin. Adipisicing dolore capicola in dolor hamburger. Cupidatat reprehenderit drumstick chislic tri-tip short loin aliqua buffalo tail burgdoggen pork fugiat porchetta. Nostrud eiusmod proident pork chop. Andouille alcatra dolor cow dolore porchetta."""

    frontpage_generator(bacon_ipsum)
