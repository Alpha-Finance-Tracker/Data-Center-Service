import uvicorn
from fastapi import FastAPI

from app.api.routes.food_router import purchase_tracker_router

app = FastAPI()

app.include_router(purchase_tracker_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)