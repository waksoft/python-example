import fitz

input_file = "source/Computer-Vision-Resources.pdf"
output_file = "dist/Computer-Vision-Resources-page-image.pdf"
barcode_file = "source/waksoft-QR-code.jpg"

# определить позицию (верхний правый угол)
image_rectangle = fitz.Rect(450, 170, 550, 270)

# retrieve the first page of the PDF
file_handle = fitz.open(input_file)
first_page = file_handle[0]

# добавить изображение
first_page.insertImage(image_rectangle, filename=barcode_file)

file_handle.save(output_file)
