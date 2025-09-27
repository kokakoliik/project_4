from typing import Any, Dict, List

import pytest


@pytest.fixture
def masks_card_number() -> str:
    return "1234 56** **** 3456"


@pytest.fixture
def masks_account_number() -> str:
    return "**7890"


@pytest.fixture
def widget_date() -> str:
    return "15.04.2023"


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"state": "EXECUTED", "date": "2023-04-15T10:15:30"},
        {"state": "PENDING", "date": "2023-04-14T09:00:00"},
        {"state": "EXECUTED", "date": "2023-04-16T12:00:00"},
        {"state": "CANCELLED", "date": "2023-04-13T08:30:00"},
        {"state": "EXECUTED", "date": "2023-04-15T11:00:00"},
        {"state": "EXECUTED", "date": None},  # проверка элемента без даты
        {"state": "EXECUTED"},  # проверка элемента без поля date
        {"state": "EXECUTED", "date": "invalid-date"},  # проверка некорректной даты
    ]
