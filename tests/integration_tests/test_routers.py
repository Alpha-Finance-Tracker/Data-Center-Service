from io import BytesIO

from fastapi import FastAPI
from httpx import AsyncClient

import pytest

from app.api.routers.finance_tracker import finance_tracker
from tests.mocked_data import *

app = FastAPI()
app.include_router(finance_tracker)

@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_file_exceeds_4MB():
    files=large_mock_file
    params = {'date':'06.09.2024'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        with pytest.raises(ValueError,match='File size exceeds 4 MB limit') as e:
            await client.post('/Finance_tracker/kaufland_receipt',params=params,files=files,headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert isinstance(e.value,ValueError)


@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_file_format_invalid():
    files = invalid_mock_file
    params = {'date':'06.09.2024'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        with pytest.raises(ValueError,match='Unsupported image format') as e:
            await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files, headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert isinstance(e.value,ValueError)




@pytest.mark.asyncio
async def test_kaufland_receipt_workflow_when_date_format_invalid():
    files = small_mock_file
    params = {'date': '2024-06-09'}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        with pytest.raises(ValueError,match="Date must be in the format 'dd.mm.yyyy'") as e:
            await client.post('/Finance_tracker/kaufland_receipt', params=params, files=files, headers={'Authorization': f'Bearer {valid_mock_access_token}'})

    assert isinstance(e.value,ValueError)


