from fastapi import APIRouter, UploadFile, File, Query
from app.data.queries import add_expenditure_into_db, get_category_expenditures_from_db
from app.utils.auth_verification_services import verify_token
from app.utils.kaufland_service import kaufland_service

finance_tracker = APIRouter(prefix='/Finance_tracker')

@finance_tracker.post('/receipt')
async def kaufland_receipt(token,image: UploadFile = File(...), date = Query(...,)):
    await verify_token(token)
    return await kaufland_service(image,date)

@finance_tracker.put('/update')
async def add_expenditure(token,name:str = Query(...,),price:float = Query(...,),category=Query(),type=Query(),date=Query()):
    user_token = await verify_token(token)
    return await add_expenditure_into_db(name,price,category,type,date,user_token)

@finance_tracker.get('/expenditures')
async def expenditures_from_date_to_date(token:str,start_date, end_date,category,type):
    user_token = await verify_token(token)
    return await get_category_expenditures_from_db(start_date,end_date,category,type)


@finance_tracker.get('/biggest_passives')
async def biggest_passives():
    return f"To do"
