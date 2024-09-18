from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from app.database.config import DATABASE_URL


if DATABASE_URL:
    engine = create_async_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
else:
    engine = None
    SessionLocal = None

Base = declarative_base()

@asynccontextmanager
async def get_db():
    async with SessionLocal() as db:
        yield db


async def custom_query(sql: str, sql_params=(), query_type='SELECT'):
    """Execute a custom SQL query with optional parameters.

    Args:
        sql (str): The SQL query to execute.
        sql_params (tuple, optional): The parameters to pass to the SQL query.
        query_type (str, optional): The type of query - 'SELECT' for read operations, 'INSERT', 'UPDATE', 'DELETE' for write operations.

    Returns:
        dict: For 'SELECT' queries, returns the result of the query. For 'INSERT', 'UPDATE', and 'DELETE', returns a status message.
    """
    async with SessionLocal() as db:
        try:
            if query_type.upper() == 'SELECT':
                result = await db.execute(text(sql), sql_params)
                return result.fetchall()
            elif query_type.upper() in ('INSERT', 'UPDATE', 'DELETE'):
                async with db.begin():
                    await db.execute(text(sql), sql_params)
                return {"message": "success"}
            else:
                return {"error": "Unsupported query type"}
        except SQLAlchemyError as e:
            print(f"An error occurred during custom_query: {e}")
            return {"error": str(e)}