from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_document = "example.pdf"
pdf = PdfFileReader(pdf_document)

# Выходные файлы для новых PDF-файлов
output_filename_even = "even.pdf"
output_filename_odd = "odd.pdf"

pdf_writer_even = PdfFileWriter()
pdf_writer_odd = PdfFileWriter()

# Получить досягаемую страницу и добавить ее в соответствующую
# выходной файл на основе номера страницы
for page in range(pdf.getNumPages()):
    current_page = pdf.getPage(page)
    if page % 2 == 0:
        pdf_writer_odd.addPage(current_page)
    else:
        pdf_writer_even.addPage(current_page)

# Записать данные на диск
with open(output_filename_even, "wb") as out:
     pdf_writer_even.write(out)
     print("created", output_filename_even)

# Записать данные на диск
with open(output_filename_odd, "wb") as out:
     pdf_writer_odd.write(out)
     print("created", output_filename_odd)
