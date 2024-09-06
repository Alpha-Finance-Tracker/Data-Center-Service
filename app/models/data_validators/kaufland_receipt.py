from datetime import datetime

from app.models.data_validators.image import ImageValidator
from app.utils.responses import DateFormat


class KauflandReceiptValidator:

    def __init__(self,date,image):
        self.date = date
        self.image = image

    async def validate_image(self):
        return await ImageValidator().validate_image(self.image)


    async def validate_date(self):
        try:
            return datetime.strptime(self.date, '%d.%m.%Y').date()
        except Exception:
            raise DateFormat()
