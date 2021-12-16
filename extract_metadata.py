from PyPDF2 import PdfFileReader
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    for k, v in info.items():
        print(k +":", v)
    print(f"Number of pages: {number_of_pages}")

if __name__ == '__main__':
    path = 'meta_data_test.pdf'
    get_info(path)