from PyPDF2 import PdfFileReader
def get_metadata(input_file):

    # Opens (and closes because we are using "with".) provided input file in read mode.
    with open(input_file, 'rb') as metadata_file:

        # Creates the file reader and gets the metadata and number of pages
        pdf_file_reader = PdfFileReader(metadata_file)
        metadata = pdf_file_reader.getDocumentInfo()
        number_of_pages = pdf_file_reader.getNumPages()

    # Prints out the metadata and number of pages.
    for k, v in metadata.items():
        print(k +":", v)
    print(f"Number of pages: {number_of_pages}")

if __name__ == '__main__':
    input_file = 'meta_data_test.pdf'
    get_metadata(input_file)