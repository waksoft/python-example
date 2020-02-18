# !/usr/bin/python
# Remove the first two pages (cover sheet) from the PDF

from pdfrw import PdfReader, PdfWriter

input_file = "example.pdf"
output_file = "example-updated.pdf"

# Define the reader and writer objects
reader_input = PdfReader(input_file)
writer_output = PdfWriter()

# Go through the pages one after the next
for current_page in range(len(reader_input.pages)):
    if current_page > 1:
        writer_output.addpage(reader_input.pages[current_page])
        print("adding page %i" % (current_page + 1))

# Write the modified content to disk
writer_output.write(output_file)
