from app.database import update_query
from app.models.data_validators.kaufland_receipt import KauflandReceiptValidator
from app.models.ocr import OCR


class Kaufland:

    def __init__(self, date, image):
        self.date = date
        self.image = image
        self.kaufland_receipt_validator = KauflandReceiptValidator(self.date,self.image)


    async def register_receipt(self):
        receipt_products = await self._extract_data()
        await self._store_receipt(receipt_products)
        return {'message':'Receipt registered successfully.'}

    async def _extract_data(self):
        image = await self.kaufland_receipt_validator.validate_image()
        return await OCR().perform_image_to_product_extraction(image)

    async def _store_receipt(self,receipt_data):
        date_of_purchase = await self.kaufland_receipt_validator.validate_date()

        for pair in receipt_data:
            await update_query(
                'INSERT INTO expenditures(name,price,category,type,date,user_id) VALUES(%s,%s,%s, %s,%s,%s)',
                (pair['Name'], pair['Price'], 'Food', pair['Type'], date_of_purchase, 8))
