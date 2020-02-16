import fitz

filename = "source/Computer-Vision-Resources.pdf"

search_term = "COMPUTER VISION"  
pdf_document = fitz.open(filename)

for current_page in range(len(pdf_document)):  
    page = pdf_document.loadPage(current_page)
    if page.searchFor(search_term):
        print("%s найдено на странице %i" % (search_term, current_page+1))
