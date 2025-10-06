from datetime import datetime
from typing import Optional


def mask_account_card(data: Optional[str]) -> str:
    """
    Маскирует номер карты или счета
    """
    if not isinstance(data, str):
        return "Ошибка: Введен некорректный номер карты/счета"
    data = data.strip()
    # Разделяем строку по первому пробелу
    parts = data.split(" ", 1)

    card_name = ["visa", "mastercard", "american express", "jcb", "unionpay", "мир"]

    if len(parts) == 2:
        prefix, number_part = parts
    else:
        prefix, number_part = parts[0], ""

    number = "".join(number_part.split())

    if not number.isdigit():
        return "Ошибка: Введен некорректный номер карты/счета"
    elif len(number) == 20 and prefix.lower() == "счет":
        return f"{prefix} **{number[-4:]}"
    elif len(number) == 16 and prefix.lower() in card_name:
        return f"{prefix} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        return "Ошибка: Введен некорректный номер карты/счета"


def get_date(input_string: Optional[str]) -> Optional[str]:
    if not input_string:
        return None

    input_str = input_string.strip()

    # Попытка парсинга ISO формата (с временем и без)
    try:
        # Если строка содержит пробел, берем только первую часть (дату)
        date_part = input_str.split()[0]
        date_object = datetime.fromisoformat(date_part)
        return date_object.strftime("%d.%m.%Y")
    except (ValueError, IndexError):
        pass

    # Попытка распарсить в формате 'DD.MM.YYYY'
    try:
        date_object = datetime.strptime(input_str, "%d.%m.%Y")
        return date_object.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Попытка распарсить в формате 'April 15, 2023'
    try:
        date_object = datetime.strptime(input_str, "%B %d, %Y")
        return date_object.strftime("%d.%m.%Y")
    except ValueError:
        pass

    # Если ничего не подошло
    return None
