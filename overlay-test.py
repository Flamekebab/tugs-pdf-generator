from PyPDF2 import PdfFileWriter, PdfFileReader
def watermark(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)
    
    pdf = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()
    
    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)
    
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)
        
if __name__ == '__main__':
    watermark(input_pdf='test.pdf', 
              output_pdf='overlayed.pdf',
              watermark_pdf='blank-pdfs/blank_title_page_r.pdf')