from fastapi import FastAPI
from httpx import AsyncClient


import pytest

from app.api.routers.finance_tracker import finance_tracker
from app.utils.responses import InternalServerError
from tests.mocked_data import *

app = FastAPI()
app.include_router(finance_tracker)


@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_token_is_not_valid():
    files = small_mock_file
    params = {'date': '2024-06-09'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files,
                                     headers={'Authorization': f'Bearer {invalid_token}'})

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_file_exceeds_4MB():
    files = large_mock_file
    params = {'date': '06.09.2024'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 413
    assert response.json()['detail'] == 'File size exceeds 4 MB limit'


@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_file_format_invalid():
    files = invalid_mock_file
    params = {'date': '06.09.2024'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 415
    assert response.json()['detail'] == 'Unsupported image format'


@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_date_format_invalid(mocker):

    mocker.patch('app.models.data_validators.kaufland_receipt.KauflandReceiptValidator.validate_image',
                 mocker.AsyncMock(return_value=True))

    files = small_mock_file
    params = {'date': '2024-06-09'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 422
    assert response.json()['detail'] == 'Date must be in the format dd.mm.yyyy'


@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_extract_data_fails(mocker):
    mocker.patch('app.models.data_validators.kaufland_receipt.KauflandReceiptValidator.validate_image',
                 mocker.AsyncMock(return_value=True))

    mocker.patch('app.models.data_validators.kaufland_receipt.KauflandReceiptValidator.validate_date',
                 mocker.AsyncMock(return_value=True))

    mocker.patch('app.api.services.kaufland.Kaufland._extract_data', side_effect=InternalServerError)

    files = small_mock_file
    params = {'date': '09.06.2024'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.json()['detail'] == 'Internal Server Error'
    assert response.status_code == 500


@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_from_start_to_end(mocker):
    mocker.patch('app.models.data_validators.kaufland_receipt.KauflandReceiptValidator.validate_image',
                 mocker.AsyncMock(return_value=True))

    mocker.patch('app.models.data_validators.kaufland_receipt.KauflandReceiptValidator.validate_date',
                 mocker.AsyncMock(return_value=True))
    mocker.patch('app.api.services.kaufland.Kaufland._extract_data', mocker.AsyncMock(return_value=[]))
    mocker.patch('app.api.services.kaufland.Kaufland._store_receipt', mocker.AsyncMock(return_value=[]))
    files = small_mock_file
    params = {'date': '09.06.2024'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 200
