import time

from sqlalchemy import Column, String, Float, Integer, Date, func, select, desc
from sqlalchemy.exc import SQLAlchemyError

from app.database.database import Base, get_db


class Expenditures(Base):
    __tablename__ = 'expenditures'

    expenditure_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    expenditure_type = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, nullable=False)

    async def retrieve_data(cls, column_type: str, category: str, time_frame) -> list:

        async with get_db() as db:
            try:
                time_period_condition = time_frame if type(time_frame) != tuple else Expenditures.date.between(time_frame[0],
                                                                                                         time_frame[1])

                if category != 'Optional':
                    column = getattr(Expenditures, column_type)
                    stmt = (
                        select(column, func.round(func.sum(Expenditures.price), 2).label('total_price'))
                        .filter(time_period_condition, Expenditures.category == category)
                        .group_by(column)
                        .order_by(desc('total_price'))
                    )
                else:
                    column = getattr(Expenditures, 'category')
                    stmt = (
                        select(column, func.round(func.sum(Expenditures.price), 2).label('total_price'))
                        .filter(time_period_condition)
                        .group_by(column)
                        .order_by(desc('total_price'))
                    )

                result = await db.execute(stmt)
                data = [x for x in result]
                return data
            except SQLAlchemyError as e:
                # Handle SQLAlchemy exceptions
                print(f"An error occurred during retrieve_data: {e}")
                return {"error": str(e)}

    @classmethod
    async def register(cls, data):
        async with get_db() as db:
            try:
                db.add(data)
                await db.commit()
            except SQLAlchemyError as e:
                # Handle SQLAlchemy exceptions
                print(f"An error occurred during add_expenditure: {e}")
                await db.rollback()  # Rollback in case of an error
