import logging

from app.database import update_query
from app.models.data_validators.kaufland_receipt import KauflandReceiptValidator
from app.models.ocr import OCR


class Kaufland:

    def __init__(self, date, image):
        self.date = date
        self.image = image
        self.validated_image = None
        self.validated_date = None

    async def validate_image_and_date(self):
        self.validated_image = await KauflandReceiptValidator(self.date, self.image).validate_image()
        self.validated_date = await KauflandReceiptValidator(self.date, self.image).validate_date()

    async def register_receipt(self):
        await self.validate_image_and_date()

        receipt_products = await self._extract_data()
        await self._store_receipt(receipt_products)
        return {'message': 'Receipt registered successfully.'}

    async def _extract_data(self):
        return await OCR().perform_image_to_product_extraction(self.validated_image)

    async def _store_receipt(self, receipt_data):
        for pair in receipt_data:
            try:
                await update_query(
                    'INSERT INTO expenditures(name,price,category,type,date,user_id) VALUES(%s,%s,%s, %s,%s,%s)',
                    (pair['Name'], pair['Price'], 'Food', pair['Type'], self.validated_date, 8))
            except Exception as e:
                logging.error('Data received from OpenAI, does not match the expected format', e)
