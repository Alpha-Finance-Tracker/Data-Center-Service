import logging

from app.database.models.expenditures import Expenditures
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

    async def register_receipt(self,user_id):
        await self.validate_image_and_date()

        receipt_products = await self._extract_data()
        await self._store_receipt(receipt_products,user_id)
        return {'message': 'Receipt registered successfully.'}

    async def _extract_data(self):
        return await OCR().perform_image_to_product_extraction(self.validated_image)

    async def _store_receipt(self, receipt_data,user_id):
        for pair in receipt_data:
            try:
                new_expenditure = Expenditures(name=pair['Name'],price=pair['Price'],category='Food',
                                               expenditure_type=pair['Type'],date=self.validated_date,user_id=user_id)
                await Expenditures().register(new_expenditure)
            except Exception as e:
                logging.error('Data received from OpenAI, does not match the expected format', e)
