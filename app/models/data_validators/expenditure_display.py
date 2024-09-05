from pydantic import BaseModel, field_validator, Field


class ExpenditureDisplay(BaseModel):
    interval:str = Field(...,)
    column_type:str = Field(...,)
    category:str = Field(...,)

    @field_validator('category', mode='after')
    def validate_category(cls, value):
        categories = {'Food', 'Entertainment', 'Health', 'Transport', 'Home', 'Sport'}

        if value not in categories:
            raise ValueError('Category not allowed!')

    @field_validator('column_type', mode='after')
    def validate_column_type(cls, value):
        column_types = {'name','category','type'}

        if value not in column_types:
            raise ValueError('Column type not allowed!')
