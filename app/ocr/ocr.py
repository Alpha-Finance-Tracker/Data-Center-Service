import re
from io import BytesIO
import cv2
from PIL import Image
import pytesseract
import numpy as np
from app.utils.helpers import convert_to_float

# Update this path to where Tesseract is installed on your system

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'



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


def extract_products(data):
    product_price_dict = {}

    # Regular expression to match product names and prices
    product_price_pattern = re.compile(r'^(.*?)(\d+,\d{2})$')

    for line in data:
        line = line.strip()
        if not line or "Total" in line:
            continue

        match = product_price_pattern.match(line)
        if match:
            product_name = match.group(1).strip()
            price_tag = match.group(2).strip()
            price = convert_to_float(price_tag)
            if product_name in product_price_dict:
                product_price_dict[product_name] += price
            else:
                product_price_dict[product_name] = price


    return product_price_dict


