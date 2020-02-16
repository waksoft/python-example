from PyPDF2 import PdfFileReader

pdf_document = "source/Computer-Vision-Resources.pdf"
with open(pdf_document, "rb") as filehandle:  
    pdf = PdfFileReader(filehandle)
   
    info = pdf.getDocumentInfo()
    pages = pdf.getNumPages()
    print("Количество страниц в документе: %i\n\n" % pages)
    print("Мета-описание: ", info)

    for i in range(pages):
        page = pdf.getPage(i)
        print("Стр.", i, " мета: ", page, "\n\nСодержание;\n")
        print(page.extractText())
