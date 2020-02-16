import fitz

pdf_document = "source/Computer-Vision-Resources.pdf"
doc = fitz.open(pdf_document)

print("Исходный документ", doc)
print("\nКоличество страниц: %i\n\n------------------\n\n" % doc.pageCount)
print(doc.metadata)

page_count = 0
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        pix1 = fitz.Pixmap(fitz.csRGB, pix)

        page_count += 1
        pix1.writePNG("images/picture_number_%s_from_page_%s.png" % (page_count, i+1))
        print("Image number ", page_count, " writed...")
        pix1 = None
