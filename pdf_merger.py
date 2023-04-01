import os
import PyPDF2

def merge_pdfs(input_dir, output_dir, output_filename, file_order):
    # Open all PDF files in the input directory
    pdf_files = [os.path.join(input_dir, filename) for filename in os.listdir(input_dir) if filename.endswith(".pdf")]
    pdf_files_sorted = [pdf_files[i] for i in file_order]

    # Merge PDF files into a single PDF file
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf_file in pdf_files_sorted:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

    # Save the merged PDF file to the output directory
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)

input_dir = "/path/to/input/directory"
output_dir = "/path/to/output/directory"
output_filename = "merged_file.pdf"
file_order = [1, 0, 2] # The order in which to merge the files (in this case, the second file will be first, followed by the first file, and then the third file)

merge_pdfs(input_dir, output_dir, output_filename, file_order)
