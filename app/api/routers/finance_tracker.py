from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.models.data_validators.expenditure_display import ExpenditureDisplay
from app.models.data_validators.expenditure_registration import ExpenditureRegistration
from app.api.services.expenditures import ExpendituresService
from app.api.services.kaufland import Kaufland
from app.utils.auth_verification_services import verify_token

finance_tracker = APIRouter(prefix='/Finance_tracker')
security = HTTPBearer()

@finance_tracker.post('/kaufland_receipt')
async def kaufland_receipt(date: str,
                           image: UploadFile = File(...),
                           credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Uploads a Kaufland receipt, processes it using Tesseract and OpenAI. And register it in the database.

    Args:
    - date (str): The date of the receipt.
    - image (UploadFile): The receipt image file.
    - credentials (HTTPAuthorizationCredentials): JWT credentials for authentication.

    Returns:
    - JSON: Response confirming the registration of the receipt.
    """
    user_token = await verify_token(credentials.credentials)
    return await Kaufland(date, image).register_receipt(user_token.get('user_id'))


@finance_tracker.post('/update')
async def add_expenditure(data: ExpenditureRegistration,
                          credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Registers an expenditure for the authenticated user.

    The `ExpenditureRegistration` model contains the following fields:
    - `name` (str): Name of the expenditure.
    - `price` (float): Amount spent.
    - `category` (str): Category of expenditure.
    - `expenditure_type` (str): Type of expenditure
    - `date` (str): Date of the expenditure. dd.mm.yyyy

    Args:
    - data (ExpenditureRegistration): The expenditure details.
    - credentials (HTTPAuthorizationCredentials): JWT credentials for authentication.

    Returns:
    - JSON: Response confirming the registration of the expenditure.
    """
    user_token = await verify_token(credentials.credentials)
    return await ExpendituresService(data).register(user_token.get('user_id'))

@finance_tracker.post('/view_expenditures')
async def view_expenditures(data: ExpenditureDisplay,
                            credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Retrieves and displays the user's expenditures.

    The `ExpenditureDisplay` model contains the following fields:
    - `interval` (str): The time interval for viewing expenditures (e.g., "monthly", "yearly").
    - `column_type` (Optional[str]): Type of data column to filter (default: "Optional").
    - `category` (Optional[str]): Expenditure category to filter by (default: "Optional").

    Args:
    - data (ExpenditureDisplay): The parameters for viewing expenditures.
    - credentials (HTTPAuthorizationCredentials): JWT credentials for authentication.

    Returns:
    - JSON: List of expenditures for the authenticated user.
    """
    user_token = await verify_token(credentials.credentials)
    return await ExpendituresService(data).display()