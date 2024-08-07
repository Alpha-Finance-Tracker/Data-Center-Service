
from fastapi import APIRouter, File, UploadFile, Query

from app.api.services.auth_verification_services import verify_token
from app.api.services.kaufland_services import kaufland_service

from app.utils.query_services import add_product_into_db, get_expenditures_from_db

purchase_tracker_router = APIRouter(prefix='/purchases')

token_b = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4LCJlbWFpbCI6IkFsZXhEQGdtYWlsLmNvbSIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNzIzMDMxMDMyLCJsYXN0X2FjdGl2aXR5IjoiMjAyNC0wOC0wNyAxMToxMzo1Mi43OTk3NzcifQ.pmylS31H7yENUSQfBrzd2W-25g2jKC6rXuTPLLXOZho'


@purchase_tracker_router.post('/')
async def submit_new_kaufland_receipt(image: UploadFile = File(...), date = Query(...,)):
    return await kaufland_service(image,date)

@purchase_tracker_router.put('/product')
async def add_product(name:str = Query(...,),price:float = Query(...,),type=Query(),date=Query()):
    return await add_product_into_db(name,price,type,date)

@purchase_tracker_router.get('/monthly_expenditures')
async def view_monthly_expenditures(month:str):
    tt = token_b
    await verify_token(tt)
    return await get_expenditures_from_db(month)

@purchase_tracker_router.get('/biggest_passives')
async def view_biggest_passives():
    return f"To do"
