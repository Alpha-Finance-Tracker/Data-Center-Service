from datetime import datetime

from pydantic import BaseModel, Field, field_validator

class ExpenditureRegistration(BaseModel):
    name: str = Field(...,gt=0,max_length=45)
    price: float = Field(...,gt=0)
    category: str = Field(...,)
    expenditure_type: str = Field(...,)
    date: str = Field(..., )

    @field_validator('date', mode='after')
    def validate_date_format(cls, value):
        try:
            # Convert the string to a datetime object using the given format
            return datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError("Date must be in the format 'dd.mm.yyyy'")

    @field_validator('price', mode='after')
    def validate_price(cls, value):
        if value < 0:
            raise ValueError('Price must be a positive number')
        return float(value.replace(',', '.'))

    @field_validator('category', mode='after')
    def validate_category(cls, value):
        categories = {'Food', 'Entertainment', 'Health', 'Transport', 'Home', 'Sport'}

        if value not in categories:
            raise ValueError('Category not allowed!')

    @field_validator('expenditure_type', mode='after')
    def validate_expenditure_type(cls, value):
        expenditure_typs = {'Animal', 'Dairy', 'Nuts', 'Vegetables', 'Beverages', 'Communications', 'Electricity',
                            'Water'}

        if value not in expenditure_typs:
            raise ValueError('Expenditure type not allowed!')
