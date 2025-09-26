import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(masks_card_number: str) -> None:
    assert get_mask_card_number(1234567890123456) == masks_card_number

    assert get_mask_card_number("1234567890123456") == masks_card_number


@pytest.mark.parametrize(
    "input_number,expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),  # стандартный 16 цифр
        ("1234 5678 1234 5678", "1234 56** **** 5678"),  # с пробелами
        ("1234567", "Ошибка: Номер карты должен содержать 16 цифр."),  # короткий номер
        ("", "Ошибка: Номер карты должен содержать 16 цифр."),  # пустая строка
        (None, "Ошибка: Номер карты должен содержать 16 цифр."),  # None
    ],
)
def test_get_mask_card_number_parametrize(input_number: str | int, expected: str) -> None:
    assert get_mask_card_number(input_number) == expected


def test_get_mask_account(masks_account_number: str) -> None:
    assert get_mask_account(12345678901234567890) == masks_account_number

    assert get_mask_account("12345678901234567890") == masks_account_number


@pytest.mark.parametrize(
    "input_account,expected_1",
    [
        ("40817810099910004312", "**4312"),  # стандартный
        ("4081 7810 0999 1000 4312", "**4312"),
        ("12345", "Ошибка: Номер счета должен содержать 20 цифр."),  # слишком короткий, не маскируется
        ("", "Ошибка: Номер счета должен содержать 20 цифр."),
        (None, "Ошибка: Номер счета должен содержать 20 цифр."),
    ],
)
def test_get_mask_account_parametrize(input_account: str | int, expected: str) -> None:
    assert get_mask_account(input_account) == expected
