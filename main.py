import easyocr

# Initialize the reader with desired languages
reader = easyocr.Reader(['en', 'bg'])  # English and Bulgarian

# Perform OCR on an image
results = reader.readtext('data/images/receipt1.jpg')

for result in results:
    print(result)
