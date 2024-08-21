from fastapi import APIRouter, UploadFile, File, Query, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.data.queries import add_expenditure_into_db, get_expenditures_from_db, category_expenditures_from_db, \
    food_expenditures_from_db, food_expenditures_by_name_from_db
from app.utils.auth_verification_services import verify_token
from app.utils.kaufland_service import kaufland_service


finance_tracker = APIRouter(prefix='/Finance_tracker')
security = HTTPBearer()

@finance_tracker.post('/receipt')
async def kaufland_receipt(image: UploadFile = File(...),
                           date = Query(...,),
                           credentials: HTTPAuthorizationCredentials = Depends(security)):

    await verify_token(credentials.credentials)
    return await kaufland_service(image,date)

@finance_tracker.put('/update')
async def add_expenditure(name:str = Query(...,),
                          price:str = Query(...,),
                          category=Query(),
                          type=Query(),
                          date=Query(),
                          credentials: HTTPAuthorizationCredentials = Depends(security)):


    user_token = await verify_token(credentials.credentials)
    return await add_expenditure_into_db(name,price,category,type,date,user_token)

@finance_tracker.get('/expenditures')
async def expenditures_from_date_to_date(start_date,
                                         end_date,
                                         category,
                                         type,
                                         credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    return await get_expenditures_from_db(start_date,end_date,category,type)


@finance_tracker.get('/biggest_passives')
async def biggest_passives(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return f"To do"

@finance_tracker.get('/category_expenditures')
async def category_expenditures(interval:str,credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    return await category_expenditures_from_db(interval)

@finance_tracker.get('/food_type_expenditures')
async def food_type_expenditures(interval:str,credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    return await food_expenditures_from_db(interval)

@finance_tracker.get('/food_name_expenditures')
async def food_name_expenditures(interval:str,credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    return await food_expenditures_by_name_from_db(interval)

