from pydantic import BaseModel, field_validator, Field
from typing import Optional

from app.utils.responses import BadRequest


class ExpenditureDisplay(BaseModel):
    interval:str = Field(...,)
    column_type:Optional[str] = Field(default='Optional')
    category: Optional[str] = Field(default='Optional')

    @field_validator('interval', mode='after')
    def validate_interval(cls, value):
        periods = {'Week', 'Month', 'Quarter', 'Year', 'Total',}
        if value not in periods:
            raise BadRequest('Period not allowed!')
        return value

    @field_validator('category', mode='after')
    def validate_category(cls, value):
        categories = {'Food', 'Entertainment', 'Health', 'Transport', 'Home', 'Sport','Optional'}
        if value not in categories:
            raise BadRequest('Category not allowed!')
        return value

    @field_validator('column_type', mode='after')
    def validate_column_type(cls, value):
        column_types = {'name','category','type','Optional'}

        if value not in column_types:
            raise BadRequest('Column type not allowed!')
        return value
