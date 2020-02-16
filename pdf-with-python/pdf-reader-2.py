import fitz

pdf_document = "./source/Computer-Vision-Resources.pdf"
doc = fitz.open(pdf_document)
print("Исходный документ: ", doc)
print("\nКоличество страниц: %i\n\n------------------\n\n" % doc.pageCount)
print(doc.metadata)

for current_page in range(len(doc)):
    page = doc.loadPage(current_page)
    page_text = page.getText("text")
    print("Стр. ", current_page+1, "\n\nСодержание;\n")
    print(page_text)
