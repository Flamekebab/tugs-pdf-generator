# We'll be using ReportLab to generate PDFs as that's currently what I've got
# If something else is a better fit then I definitely want to hear about it!
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.lib import utils
from reportlab.lib.units import cm
from reportlab.platypus import Frame, Image

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
    canvas.drawString(72, 72, "Hello, World")

    canvas.save()


def add_font(name: str, path: str):
    ''' Non-default fonts must be registered before use in PDF generation.

    :param name: The name you want the font registered as (can be different from the font's original name)

    :param path: Either an absolute path to the font's TTF file or a path relative to where this function is run.

    '''
    pdfmetrics.registerFont(TTFont(name, path))


if __name__ == "__main__":
    main()
