from PIL import Image

image = Image.open('GOV_ID.jpeg')

image_pdf = image.convert('RGB')
image_pdf.save('./Govt. ID.pdf')