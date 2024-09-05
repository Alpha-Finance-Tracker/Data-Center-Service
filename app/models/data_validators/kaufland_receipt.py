from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class KauflandReceipt(BaseModel):
    date: str = Field(..., )

    @field_validator('date', mode='after')
    def validate_date_format(cls, value):
        try:
            return datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError("Date must be in the format 'dd.mm.yyyy'")
