# Удалите первые две страницы (титульный лист) из PDF

from pdfrw import PdfReader, PdfWriter

input_file = "example.pdf"
output_file = "example-updated.pdf"

# Определить объекты чтения и записи
reader_input = PdfReader(input_file)
writer_output = PdfWriter()

# Перейти на страницу один за другим
for current_page in range(len(reader_input.pages)):
    if current_page > 1:
        writer_output.addpage(reader_input.pages[current_page])
        print("adding page %i" % (current_page + 1))

# Записать измененный контент на диск
writer_output.write(output_file)
