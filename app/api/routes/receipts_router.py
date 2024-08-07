
from fastapi import APIRouter, File, UploadFile, Query

from app.api.services.auth_verification_services import verify_token
from app.api.services.kaufland_services import kaufland_service

from app.utils.query_services import add_product_into_db, get_expenditures_from_db

purchase_tracker_router = APIRouter(prefix='/purchases')

@purchase_tracker_router.post('/')
async def submit_new_kaufland_receipt(token,image: UploadFile = File(...), date = Query(...,)):
    await verify_token(token)
    return await kaufland_service(image,date)

@purchase_tracker_router.put('/product')
async def add_product(token,name:str = Query(...,),price:float = Query(...,),type=Query(),date=Query()):
    await verify_token(token)
    return await add_product_into_db(name,price,type,date)

@purchase_tracker_router.get('/monthly_expenditures')
async def view_monthly_expenditures(token:str,month:str):
    await verify_token(token)
    return await get_expenditures_from_db(month)

@purchase_tracker_router.get('/biggest_passives')
async def view_biggest_passives():
    return f"To do"
