from fastapi import APIRouter, UploadFile, File, Query

from app.api.food_features.food_queries import get_food_expenditures_from_db, add_food_into_db
from app.api.food_features.food_services import kaufland_service
from app.utils.auth_verification_services import verify_token



purchased_food_router = APIRouter(prefix='/food')

@purchased_food_router.post('/receipt')
async def kaufland_receipt(token,image: UploadFile = File(...), date = Query(...,)):
    await verify_token(token)
    return await kaufland_service(image,date)

@purchased_food_router.put('/update')
async def add_food(token,name:str = Query(...,),price:float = Query(...,),category=Query(),type=Query(),date=Query()):
    user_token = await verify_token(token)
    return await add_food_into_db(name,price,category,type,date,user_token)

@purchased_food_router.get('/expenditures')
async def expenditures_from_date_to_date(token:str,start_date, end_date):
    user_token = await verify_token(token)
    return await get_food_expenditures_from_db(start_date,end_date)


@purchased_food_router.get('/biggest_passives')
async def biggest_passives():
    return f"To do"
