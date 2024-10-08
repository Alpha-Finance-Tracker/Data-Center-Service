import re
from io import BytesIO
import cv2
from PIL import Image
import pytesseract
import numpy as np

from app.models.open_ai import OpenAiService
from app.utils.responses import InternalServerError

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

class OCR:

    async def convert_file_to_opencv_image(self, file):
        file_content = await file.read()
        image = Image.open(BytesIO(file_content))
        open_cv_image = np.array(image)
        if open_cv_image.ndim == 3:
            open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
        return open_cv_image

    async def threshold_and_invert_image(self, open_cv_image):
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        thresh = cv2.bitwise_not(thresh)
        return thresh

    async def extract_text_from_image(self, inverted_image):
        text = pytesseract.image_to_string(inverted_image, lang='bul+eng')
        return text

    async def split_text_into_lines(self, text):
        lines = text.strip().split('\n')
        return [line for line in lines]

    async def parse_product_information(self, data):
        product_price_dict = []
        product_price_pattern = re.compile(r'^(.*?)(\d+,\d{2})$')

        for line in data:
            line = line.strip()
            if not line or "Total" in line:
                continue

            match = product_price_pattern.match(line)
            if match:
                product_name = match.group(1).strip()
                price_tag = match.group(2).strip()
                price = float(price_tag.replace(',', '.'))
                product_price_dict.append({'Name': product_name, 'Price': price})

        return product_price_dict

    async def perform_image_to_product_extraction(self, image):
        try:
            open_cv_image = await self.convert_file_to_opencv_image(image)
            inverted_image = await self.threshold_and_invert_image(open_cv_image)
            text = await self.extract_text_from_image(inverted_image)

            extracted_data = await self.split_text_into_lines(text)
            parsed_data = await self.parse_product_information(extracted_data)
            classified_products = await OpenAiService().classify_products(parsed_data)
            return classified_products
        except InternalServerError:
            raise InternalServerError()
