from fastapi import APIRouter, Query

from app.api.entertainment_features.entertainment_queries import add_entertainment_into_db
from app.utils.auth_verification_services import verify_token

entertainment_expenditures_router = APIRouter(prefix='transportation')


@entertainment_expenditures_router.put('/expenditure')
async def add_health(token,name:str = Query(...,),price:float = Query(...,),category=Query(),type=Query(),date=Query()):
    user_token = await verify_token(token)
    return await add_entertainment_into_db(name,price,category,type,date,user_token)


@entertainment_expenditures_router.get('/biggest_passives')
async def biggest_passives():
    return f"To do"
