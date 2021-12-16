from PyPDF2 import PdfFileReader
import json

def get_metadata(input_file):

    # Opens (and closes because we are using "with".) provided input file in 
    # read mode.
    with open(input_file, "rb") as metadata_file:

        # Creates the file reader and gets the metadata and number of pages
        pdf_file_reader = PdfFileReader(metadata_file)
        metadata = pdf_file_reader.getDocumentInfo()
        number_of_pages = pdf_file_reader.getNumPages()

    # Prints out the metadata and number of pages to the console for 
    # verification purposes. The metadata is sorted alphabetically and indented 
    # with 4 spaces. The number of pages is not exported to the JSON.
    json_object = json.dumps(metadata, sort_keys = True, indent = 4)
    print("Metadata that was found:\n", json_object)
    print(f"Number of pages: {number_of_pages}")
    print("Adding Number Of Pages value to metadata.")
    pages_dict = {"/NumberOfPages": number_of_pages}
    metadata.update(pages_dict)

    # Creates output file in write mode ("w"). Sorts the "key : value" pairs 
    # alphabetically and indents 4 spaces when exporting.
    with open(output_file, "w") as metadata_json_file:
        print("Exporting metadata to JSON file:", output_file)
        json.dump(metadata, metadata_json_file, sort_keys = True, indent = 4)

if __name__ == "__main__":
    input_file = "meta_data_test.pdf"
    output_file = "metadata.json"
    get_metadata(input_file)