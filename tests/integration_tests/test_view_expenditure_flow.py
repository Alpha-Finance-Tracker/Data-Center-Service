from fastapi import FastAPI
from httpx import AsyncClient

import pytest

from app.api.routers.finance_tracker import finance_tracker
from app.utils.responses import InternalServerError
from tests.mocked_data import *

app = FastAPI()
app.include_router(finance_tracker)


@pytest.mark.asyncio
async def test_view_expenditures_when_token_invalid():

        async with AsyncClient(app=app, base_url="http://testserver") as client:
            response = await client.post('/Finance_tracker/view_expenditures', json=mock_view_expenditures,
                                         headers={'Authorization': f'Bearer {invalid_token}'})

        assert response.status_code == 401


@pytest.mark.asyncio
async def test_view_expenditures_when_data_with_invalid_period():
    mock_data = mock_view_expenditures.copy()
    mock_data.update({'interval':'random'})
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/view_expenditures', json=mock_data,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 400
    assert response.json()['detail'] == 'Period not allowed!'


@pytest.mark.asyncio
async def test_view_expenditures_when_data_with_invalid_category():
    mock_data = mock_view_expenditures.copy()
    mock_data.update({'category': 'random'})
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/view_expenditures', json=mock_data,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 400
    assert response.json()['detail'] == 'Category not allowed!'




@pytest.mark.asyncio
async def test_view_expenditures_when_data_with_invalid_column_type():
    mock_data = mock_view_expenditures.copy()
    mock_data.update({'column_type': 'random'})
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/view_expenditures', json=mock_data,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 400
    assert response.json()['detail'] == 'Column type not allowed!'

@pytest.mark.asyncio
async def test_view_expenditures_successfully(mocker):
    mocker.patch('app.api.services.expenditures.Expenditures.retrieve_data',mocker.AsyncMock(return_value=[]))
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post('/Finance_tracker/view_expenditures', json=mock_view_expenditures,
                                     headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert response.status_code == 200



