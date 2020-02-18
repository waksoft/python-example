# Добавление QR-кода в многостраничный PDF документ

from pdfrw import PdfReader, PdfWriter, PageMerge

input_file = "source/Computer-Vision-Resources.pdf"
output_file = "dist/Computer-Vision-Resources-QR-pages.pdf"
watermark_file = "source/waksoft-QR-code.pdf"

# определяем объекты чтения и записи
reader_input = PdfReader(input_file)
writer_output = PdfWriter()
watermark_input = PdfReader(watermark_file)
watermark = watermark_input.pages[0]

# просматривать страницы одну за другой
for current_page in range(len(reader_input.pages)):
    merger = PageMerge(reader_input.pages[current_page])
    merger.add(watermark).render()

# записать измененный контент на диск
writer_output.write(output_file, reader_input)
