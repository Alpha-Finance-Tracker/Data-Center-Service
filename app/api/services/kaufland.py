from app.database import update_query
from app.models.data_validators.image import ImageValidator
from app.models.ocr import OCR


class Kaufland:

    def __init__(self, data, image):
        self.date = data.date
        self.image = image

    @property
    def validated_image(self):
        return ImageValidator().validate_image(self.image)

    async def extract_data(self):
        return await OCR(self.validated_image).perform_image_to_product_extraction()

    async def register_receipt(self):
        receipt_products = await self.extract_data()
        return await self.store_receipt(receipt_products)

    async def store_receipt(self,receipt_data):
        for pair in receipt_data:
            await update_query(
                'INSERT INTO expenditures(name,price,category,type,date,user_id) VALUES(%s,%s,%s, %s,%s,%s)',
                (pair['Name'], pair['Price'], 'Food', pair['Type'], self.date, 8))
