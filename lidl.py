
from io import BytesIO

import cv2
from PIL import Image
import pytesseract
import numpy as np

# Update this path to where Tesseract is installed on your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


async def handle_image(file):
    # Read the file into a byte stream
    file_content = await file.read()
    # Convert byte stream to an image
    image = Image.open(BytesIO(file_content))
    # Convert PIL image to OpenCV format
    open_cv_image = np.array(image)
    if open_cv_image.ndim == 3:
        # Convert RGB to BGR
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    return open_cv_image


def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # Invert colors
    thresh = cv2.bitwise_not(thresh)
    return thresh


def perform_ocr(image):
    # Perform OCR using Tesseract with multiple languages
    text = pytesseract.image_to_string(image, lang='bul+eng')  # Use 'bul+eng' for Bulgarian and English
    return text


def extract_info(text):
    lines = text.strip().split('\n')
    data = []

    for line in lines:
        data.append(line)

    return data

#
# processed_image = preprocess_image('lidl1.jpg')
# # Perform OCR
# ocr_text = perform_ocr(processed_image)
# # Extract product names and prices
# extracted_data = extract_info(ocr_text)
#
# # Create a DataFrame
# df = pd.DataFrame(extracted_data)
# pd.set_option('display.max_rows', None)
# print(df)
#
#
