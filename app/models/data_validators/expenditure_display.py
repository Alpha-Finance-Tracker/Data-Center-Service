from pydantic import BaseModel, field_validator, Field
from typing import Optional


class ExpenditureDisplay(BaseModel):
    interval:str = Field(...,)
    column_type:Optional[str] = Field(default='Optional')
    category: Optional[str] = Field(default='Optional')

    @field_validator('category', mode='after')
    def validate_category(cls, value):
        categories = {'Food', 'Entertainment', 'Health', 'Transport', 'Home', 'Sport'}

        if value is None or value == 'Optional':
            return
        if value not in categories:
            raise ValueError('Category not allowed!')
        return value

    @field_validator('column_type', mode='after')
    def validate_column_type(cls, value):
        column_types = {'name','category','type'}

        if value not in column_types:
            raise ValueError('Column type not allowed!')
        return value
