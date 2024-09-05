from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.models.data_validators.expenditure_display import ExpenditureDisplay
from app.models.data_validators.expenditure_registration import ExpenditureRegistration
from app.models.data_validators.kaufland_receipt import KauflandReceipt
from app.api.services.expenditures import Expenditures
from app.api.services.kaufland import Kaufland
from app.utils.auth_verification_services import verify_token

finance_tracker = APIRouter(prefix='/Finance_tracker')
security = HTTPBearer()


@finance_tracker.post('/kaufland_receipt')
async def kaufland_receipt(data: KauflandReceipt,
                           image: UploadFile = File(...),

                           credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    return await Kaufland(data, image).register_receipt()


@finance_tracker.put('/update')
async def add_expenditure(data: ExpenditureRegistration,
                          credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_token = await verify_token(credentials.credentials)
    return await Expenditures(data).register(user_token.get('user_id'))


@finance_tracker.get('/expenditures')
async def view_expenditures(data: ExpenditureDisplay,
                            credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    return await Expenditures(data).display()