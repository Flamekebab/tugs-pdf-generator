# Combines all the PDFs in the "source-pdfs"" directory into a single PDF.

import PyPDF2
import os

pdf_files = []
source_directory = "./source-pdfs/"

# Get all the PDF filenames.
for filename in os.listdir(source_directory):
    if filename.endswith(".pdf"):
        pdf_files.append(source_directory+filename)

# Sorts the found PDFs into alphabetical order.
pdf_files.sort(key = str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdf_files:
    pdf_file_obj = open(filename, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Loop through all the pages and add them.
    for page_number in range(0, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_number)
        pdf_writer.addPage(page_obj)

# Save the resulting PDF to a file.
pdf_output = open("combined_result.pdf", "wb")
pdf_writer.write(pdf_output)
pdf_output.close()