from fastapi import APIRouter, Query

from app.api.services.auth_verification_services import verify_token

transportation_expenditures_router = APIRouter(prefix='transportation')


@transportation_expenditures_router.put('/expenditure')
async def add_transportation(token,name:str = Query(...,),price:float = Query(...,),type=Query(),date=Query()):
    await verify_token(token)
    print('To do')
@transportation_expenditures_router.get('/monthly_expenditures')
async def monthly_expenditures(token:str,month:str):
    await verify_token(token)
    print('To do')

@transportation_expenditures_router.get('/monthly_expenditures')
async def weekly_expenditures(token:str,week:str):
    await verify_token(token)
    print('To do')

@transportation_expenditures_router.get('/monthly_expenditures')
async def yearly_expenditures(token:str,year:str):
    await verify_token(token)
    print('To do')


@transportation_expenditures_router.get('/biggest_passives')
async def biggest_passives():
    return f"To do"
