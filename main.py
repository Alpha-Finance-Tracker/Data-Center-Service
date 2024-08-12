import uvicorn
from fastapi import FastAPI

from app.api.finance_tracker import finance_tracker

app = FastAPI()

app.include_router(finance_tracker,tags=['Finance Tracker'])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)