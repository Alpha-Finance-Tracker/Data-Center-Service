from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from app.utils.responses import BadRequest, ProcessableEntity


class ExpenditureRegistration(BaseModel):
    name: str = Field(..., )
    price: float = Field(..., )
    category: str = Field(..., )
    expenditure_type: str = Field(..., )
    date: str = Field(..., )

    @field_validator('name', mode='after')
    def validate_name(cls, value):
        if len(value) == 0 or len(value) > 45:
            raise BadRequest('Name must be between 1 and 45 characters')
        return value

    @field_validator('price', mode='after')
    def validate_price(cls, value):
        if value < 0:
            raise BadRequest('Price must be a positive number')
        return value

    @field_validator('category', mode='after')
    def validate_category(cls, value):
        categories = {'Food', 'Entertainment', 'Health', 'Transport', 'Home', 'Sport'}

        if value not in categories:
            raise BadRequest('Category not allowed!')
        return value

    @field_validator('expenditure_type', mode='after')
    def validate_expenditure_type(cls, value):
        print(value)
        expenditure_types = {'Animal', 'Dairy', 'Nuts', 'Vegetables', 'Fruit', 'Beverages', 'Communications',
                             'Electricity','Water', 'Transport','Health','Entertainment','Sport'}

        if value not in expenditure_types:
            raise BadRequest('Expenditure type not allowed!')
        return value

    @field_validator('date', mode='after')
    def validate_date_format(cls, value):
        try:
            parsed_date = datetime.strptime(value, '%d.%m.%Y')
            formatted_date = parsed_date.date()
            return formatted_date
        except ValueError:
            raise ProcessableEntity('Date must be in the format dd.mm.yyyy')
