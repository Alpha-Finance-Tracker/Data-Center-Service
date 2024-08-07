
from fastapi import APIRouter, File, UploadFile, Query

from app.api.services.auth_verification_services import verify_token
from app.api.services.kaufland_services import kaufland_service

from app.utils.query_services import add_product_into_db, get_expenditures_from_db

purchased_food_router = APIRouter(prefix='/food')

@purchased_food_router.post('/receipt')
async def kaufland_receipt(token,image: UploadFile = File(...), date = Query(...,)):
    await verify_token(token)
    return await kaufland_service(image,date)

@purchased_food_router.put('/expenditure')
async def add_food(token,name:str = Query(...,),price:float = Query(...,),type=Query(),date=Query()):
    await verify_token(token)
    return await add_product_into_db(name,price,type,date)

@purchased_food_router.get('/monthly_expenditures')
async def monthly_expenditures(token:str,month:str):
    await verify_token(token)
    return await get_expenditures_from_db(month)

@purchased_food_router.get('/monthly_expenditures')
async def weekly_expenditures(token:str,week:str):
    await verify_token(token)
    print('To do ')

@purchased_food_router.get('/monthly_expenditures')
async def yearly_expenditures(token:str,year:str):
    await verify_token(token)
    print('To do ')


@purchased_food_router.get('/biggest_passives')
async def biggest_passives():
    return f"To do"
