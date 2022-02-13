from PIL import Image

# jpg photo path that you want to convert 
JPG_FILE_PATH = ''
# path of pdf file after conveting
PDF_FILE_PATH = ''

image = Image.open(JPG_FILE_PATH)

image_pdf = image.convert('RGB')
image_pdf.save(PDF_FILE_PATH)