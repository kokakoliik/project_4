from datetime import datetime

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_value,expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),  # карта
        ("Счет 40817810099910004312", "Счет **4312"),  # счет
    ],
)
def test_mask_account_card(input_value: str, expected: str) -> None:
    assert mask_account_card(input_value) == expected


@pytest.mark.parametrize("bad_input", ["", None, 12345, [], {}, "abc123", "12 34 56"])
def test_mask_account_card_invalid_input(bad_input: str | None) -> None:
    from src.widget import mask_account_card  # импорт вашей функции

    result = mask_account_card(bad_input)
    assert result == "Ошибка: Введен некорректный номер карты/счета"


def test_get_date(widget_date: datetime) -> None:
    assert get_date("2023-04-15 12:54:12.454542542") == widget_date

    assert get_date("15.04.2023") == widget_date

    assert get_date("April 15, 2023") == widget_date


@pytest.mark.parametrize(
    "input_date,expected",
    [
        ("", None),
        (None, None),
        ("invalid date", None),
    ],
)
def test_get_date_parametrize(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected
