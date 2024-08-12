import uvicorn
from fastapi import FastAPI

from app.api.food_features.food_router import purchased_food_router 

app = FastAPI()

app.include_router(purchased_food_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)