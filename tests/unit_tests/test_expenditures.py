import pytest

from app.api.services.expenditures import ExpendituresService
from tests.mocked_data import *


@pytest.mark.asyncio
async def test_display_method_when_data_is_present(mocker):
    mocker.patch('app.api.services.expenditures.ExpendituresService.retrieve_data',
                 mocker.AsyncMock(return_value=expenditures_mock_data))

    result = await ExpendituresService(None).display()

    assert len(result) > 0


@pytest.mark.asyncio
async def test_display_method_when_data_is__not_present(mocker):
    mocker.patch('app.api.services.expenditures.ExpendituresService.retrieve_data', mocker.AsyncMock(return_value=[]))

    result = await ExpendituresService(None).display()

    assert len(result) == 0
