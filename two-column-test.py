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
from reportlab.lib.enums import TA_JUSTIFY
import random

# Load some defaults
styles=getSampleStyleSheet()

# We'll need to check these margins, I suspect
# We can turn off showBoundary when we're ready but it's handy for debugging
doc = BaseDocTemplate('test.pdf',showBoundary=1,leftMargin=0.553,rightMargin=0.553)

#Two Columns
# Frame(x1, y1, width,height, leftPadding=6, bottomPadding=6, rightPadding=6, topPadding=6, id=None, showBoundary=0)
frame1 = Frame(doc.leftMargin, doc.bottomMargin, doc.width/2-6, doc.height, id='col1')
frame2 = Frame(doc.leftMargin+doc.width/2+6, doc.bottomMargin, doc.width/2-6, doc.height, id='col2')

# It looks like we're creating a "flowable" here:
words = "lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam nonumy eirmod tempor invidunt ut labore et".split()
Elements=[]
Elements.append(Paragraph(" ".join([random.choice(words) for i in range(1000)]),styles['Normal']))


doc.addPageTemplates([PageTemplate(id='TwoCol',frames=[frame1,frame2]), ])


#start the construction of the pdf
# .build() takes a List of flowables 
doc.build(Elements)