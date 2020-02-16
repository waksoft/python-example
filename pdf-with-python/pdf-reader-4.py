from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_document = "source/Computer-Vision-Resources.pdf"
pdf = PdfFileReader(pdf_document)

for page in range(pdf.getNumPages()):  
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    pdf_writer.addPage(current_page)

    outputFilename = "dist/Computer-Vision-Resources-page-{}.pdf".format(page + 1)
    with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

        print("created", outputFilename)
