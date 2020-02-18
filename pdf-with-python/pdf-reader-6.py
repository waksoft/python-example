# Добавление водяного знака в одностраничный PDF

import PyPDF2

input_file = "source/Computer-Vision-Resources.pdf"
output_file = "dist/Computer-Vision-Resources-page-drafted.pdf"
watermark_file = "source/mshe-logo-512x512.pdf"

with open(input_file, "rb") as filehandle_input:
    # читать содержимое исходного файла
    pdf = PyPDF2.PdfFileReader(filehandle_input)
    
    with open(watermark_file, "rb") as filehandle_watermark:
        # читать содержание водяного знака
        watermark = PyPDF2.PdfFileReader(filehandle_watermark)
        
        # получить первую страницу оригинального PDF
        first_page = pdf.getPage(0)
        
        # получить первую страницу водяного знака PDF
        first_page_watermark = watermark.getPage(0)
        
        # объединить две страницы
        first_page.mergePage(first_page_watermark)
        
        # создать объект записи PDF для выходного файла
        pdf_writer = PyPDF2.PdfFileWriter()
        
        # добавить страницу
        pdf_writer.addPage(first_page)
        
        with open(output_file, "wb") as filehandle_output:
            # записать файл с водяными знаками в новый файл
            pdf_writer.write(filehandle_output)
