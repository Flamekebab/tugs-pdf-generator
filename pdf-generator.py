# We"ll be using ReportLab to generate PDFs as that"s currently what I"ve got
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

def main(american_user = False): 
    # We default to A4 but American users may want US Letter instead
    # I might cut this functionality!
    if american_user is True:
        canvas = Canvas("test.pdf", pagesize=LETTER)
        width, height = LETTER
    else:
        canvas = canvas = Canvas("test.pdf")

    # We"re going to need two fonts for these documents
    # Ridgeline for the titles
    pdfmetrics.registerFont(TTFont("Ridgeline", "./fonts/Ridgeline.ttf"))

    # Source Sans Pro for the body text
    pdfmetrics.registerFont(TTFont("SSP", "./fonts/SourceSansPro-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("SSP Italic", "./fonts/SourceSansPro-It.ttf"))
    pdfmetrics.registerFont(TTFont("SSP Bold", "./fonts/SourceSansPro-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("SSP Bold Italic", "./fonts/SourceSansPro-BoldIt.ttf"))

    # addMapping(face, bold, italic, psname)
    addMapping('SSP', 0, 0, 'SSP') #normal
    addMapping('SSP', 0, 1, 'SSP Italic') #italic
    addMapping('SSP', 1, 0, 'SSP Bold') #bold
    addMapping('SSP', 1, 1, 'SSP Bold Italic') #italic and bold

    # From now on we can use the syntax "canvas.setFont("Ridgeline", 32)" to set the font and size

    # We're going to need to draw a box for this image but that can happen later
    
    footer = "./footers/bottom-bar-R.png"
    # the 0s are anchoring co-ordinates. The anchor parameter is a compass reference 
    # "ne", "sw" with "c" being the centre of the compass
    # 19.5cm is the correct value - just trust my maths on this ;)
    canvas.drawImage(footer, 0, 0, width=19.5*cm, preserveAspectRatio=True, anchor='c')




    canvas.setFont("Ridgeline", 18)
    canvas.drawString(72, 72, "Hello, World")
    
    canvas.save()




if __name__ == "__main__":
    main()