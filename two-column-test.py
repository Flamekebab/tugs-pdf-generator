#from reportlab.pdfgen.canvas import Canvas
## It defaults to A4 but here's how to do the US letter bollocks
## from reportlab.lib.pagesizes import letter
#
#pdf = Canvas("test.pdf")
##More about US proprietary bullshit
##pdf = Canvas("test.pdf", pagesize = letter)
#
#
##An important thing to note here is that when specifying coordinates, the origin is in the lower left hand corner of the page, rather than the top left
#pdf.setFont("Courier", 12)
#pdf.setStrokeColorRGB(1, 0, 0)
#pdf.drawString(300, 300, "CLASSIFIED")
#
##It's also possible to specify measurements in other units. You can use centimeters, millimeters, inches and picas. The default unit of measurement is a point, equal to one seventy-second of an inch. The extra measurements are available from reportlab.lib.units:
#from reportlab.lib.units import cm, mm, inch, pica
#
#pdf.drawString(2 * inch, inch, "For Your Eyes Only")
#
##The showPage method closes the current page. Any further drawing will occur on the next page, though if all drawing has ended, another page will not be added.
#pdf.showPage()
#
#pdf.save()

from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
#from reportlab.lib.enums import TA_JUSTIFY

# Load some defaults
styles=getSampleStyleSheet()

# We'll need to check these margins, I suspect
# We can turn off showBoundary when we're ready but it's handy for debugging
# We create a basic document template and then add *page* templates to it.
doc = BaseDocTemplate('test.pdf',showBoundary=1,leftMargin=0.553,rightMargin=0.553)

#Two Columns
# Frame(x1, y1, width,height, leftPadding=6, bottomPadding=6, rightPadding=6, topPadding=6, id=None, showBoundary=0)
frame1 = Frame(doc.leftMargin, doc.bottomMargin, doc.width/2-6, doc.height, id='col1')
frame2 = Frame(doc.leftMargin+doc.width/2+6, doc.bottomMargin, doc.width/2-6, doc.height, id='col2')


# From the documentation (page 22 of the reference PDF):
# Class Paragraph:
# Paragraph(text, style, bulletText=None, caseSensitive=1)
# text - a string of stuff to go into the paragraph.
# style - a style definition as in reportlab.lib.styles.
# bulletText - an optional bullet defintion.
# caseSensitive - set this to 0 if you want the markup tags and their attributes to be case-insensitive.
# This class is a flowable that can format a block of text
# into a paragraph with a given style.

# Huh, triple quotes allows for multi-line strings. Useful!
bacon_ipsum = """Pork belly ut enim aliquip andouille irure. Ground round velit brisket shoulder, eiusmod tri-tip dolor. Minim rump beef, tenderloin voluptate do capicola labore landjaeger ea quis bacon et. Pork chop tempor shankle hamburger nulla.

Cow ut doner ipsum fugiat aliquip. Proident pork loin minim nostrud bacon, beef ball tip ullamco. Short loin porchetta pig, dolore nulla ex ut ham hock kielbasa bresaola swine ipsum excepteur tongue veniam. Dolor doner ball tip, tail tenderloin capicola nostrud bacon. Quis shankle t-bone kevin, anim officia sunt excepteur corned beef short ribs spare ribs laboris in voluptate. Pancetta sunt pork chop burgdoggen tenderloin frankfurter. Brisket fugiat adipisicing filet mignon.

Velit spare ribs alcatra, excepteur in filet mignon ground round nostrud frankfurter drumstick tail. Leberkas in in brisket venison ribeye nostrud sunt quis spare ribs ullamco nisi adipisicing boudin pig. Cow meatloaf eu flank, pancetta magna commodo enim strip steak in. Chuck quis spare ribs turducken, capicola beef brisket salami doner.

Aliqua tri-tip shankle ribeye hamburger jerky filet mignon pork chop turkey. Aliquip flank mollit eiusmod. Veniam tempor reprehenderit laboris. Quis jerky dolor, picanha esse irure tempor ut laboris biltong. Qui labore tail minim cupidatat turkey aute eu anim porchetta. Biltong ball tip porchetta, non cupim t-bone deserunt consectetur ad irure pig shankle tri-tip frankfurter beef ribs.

Swine pork belly rump, nostrud ham hock cow boudin. Adipisicing dolore capicola in dolor hamburger. Cupidatat reprehenderit drumstick chislic tri-tip short loin aliqua buffalo tail burgdoggen pork fugiat porchetta. Nostrud eiusmod proident pork chop. Andouille alcatra dolor cow dolore porchetta."""

# We need to add paragraphs, a kind of "flowable"
paragraphs = []
paragraphs.append(Paragraph(bacon_ipsum,styles['Normal']))
paragraphs.append(Paragraph(bacon_ipsum,styles['Normal']))
paragraphs.append(Paragraph(bacon_ipsum,styles['Normal']))
# If we add even more text another page is automatically created with more frames for it to flow into
# paragraphs.append(Paragraph(bacon_ipsum,styles['Normal']))
# paragraphs.append(Paragraph(bacon_ipsum,styles['Normal']))
# paragraphs.append(Paragraph(bacon_ipsum,styles['Normal']))

# I believe that listing the frames like this causes text to overflow into the next frame
# I've yet to figure out where these IDs are actually used though!
doc.addPageTemplates([PageTemplate(id='TwoCol',frames=[frame1,frame2]), ])

#start the construction of the pdf
# .build() takes a List of flowables 
# BaseDocTemplate.build(self, flowables, filename=None, canvasmaker=canvas.Canvas)
doc.build(paragraphs)