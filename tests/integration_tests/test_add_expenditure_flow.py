import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from app.api.routers.finance_tracker import finance_tracker
from tests.mocked_data import *

app = FastAPI()
app.include_router(finance_tracker)

@pytest.mark.asyncio
async def test_add_expenditure_when_token_invalid():

        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post('/Finance_tracker/update', json=mock_expenditure,
                                         headers={'Authorization': f'Bearer {invalid_token}'})

        assert response.status_code == 401

@pytest.mark.asyncio
async def test_add_expenditure_when_data_with_invalid_name():
        mock_data = mock_expenditure.copy()
        mock_data.update({'name':'a' * 46})
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post('/Finance_tracker/update', json=mock_data,
                                         headers={'Authorization': f'Bearer {valid_mock_access_token}'})

        assert response.status_code == 400
        assert response.json()['detail'] == 'Name must be between 1 and 45 characters'


@pytest.mark.asyncio
async def test_add_expenditure_when_data_with_invalid_price():
        mock_data = mock_expenditure.copy()
        mock_data.update({'price':-1})
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post('/Finance_tracker/update', json=mock_data,
                                         headers={'Authorization': f'Bearer {valid_mock_access_token}'})

        assert response.status_code == 400
        assert response.json()['detail'] == 'Price must be a positive number'

@pytest.mark.asyncio
async def test_add_expenditure_when_data_with_invalid_category():
        mock_data = mock_expenditure.copy()
        mock_data.update({'category':'random'})
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post('/Finance_tracker/update', json=mock_data,
                                         headers={'Authorization': f'Bearer {valid_mock_access_token}'})

        assert response.status_code == 400
        assert response.json()['detail'] == 'Category not allowed!'

@pytest.mark.asyncio
async def test_add_expenditure_when_data_with_invalid_type():
        mock_data = mock_expenditure.copy()
        mock_data.update({'expenditure_type':'random'})
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post('/Finance_tracker/update', json=mock_data,
                                         headers={'Authorization': f'Bearer {valid_mock_access_token}'})

        assert response.status_code == 400
        assert response.json()['detail'] == 'Expenditure type not allowed!'


@pytest.mark.asyncio
async def test_add_expenditure_when_data_with_invalid_type():
    mock_data = mock_expenditure.copy()
    mock_data.update({'date': '2024.12.12'})
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/update', json=mock_data,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 422
    assert response.json()['detail'] == 'Date must be in the format dd.mm.yyyy'

@pytest.mark.asyncio
async def test_add_expenditure_successfully(mocker):
    mocker.patch('app.api.services.expenditures.Expenditures.register',mocker.AsyncMock(return_value=[]))
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/update', json=mock_expenditure,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 200



