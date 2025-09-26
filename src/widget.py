from datetime import datetime


def mask_account_card(data):
    """
    Маскирует номер карты или счета без использования модуля re.

    - Для счета (например, "Счет 1234567890123456"):
        возвращает: "Счет **3456"
    - Для карты (например, "Visa 1234567890123456"):
        возвращает: "Visa 1234 56** **** 3456"
    - При неправильных данных возвращает: "Ошибка: Введен некорректный номер карты/счета"
    """
    if not isinstance(data, str):
        return "Ошибка: Введен некорректный номер карты/счета"

    data = data.strip()
    # Разделяем строку по первому пробелу
    parts = data.split(' ', 1)

    if len(parts) == 2:
        prefix, number_part = parts
    else:
        # В случае отсутствия пробела, предполагаем, что либо нет типа, либо неправильный формат
        prefix, number_part = parts[0], ""

    # Удаляем все пробелы внутри номера
    number = "".join(number_part.split())

    # Проверка длинны и содержимого номера
    if not number.isdigit() or len(number) != 16:
        return "Ошибка: Введен некорректный номер карты/счета"

    # Маскировка
    if prefix.lower() == "счет":
        return f"{prefix} **{number[-4:]}"
    elif prefix:
        # Карта с названием
        return f"{prefix} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        # Нет названия - просто маска номера
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def get_date(input_string: str) -> str:
    """
    Преобразует строку с датой в формате 'YYYY-MM-DDTHH:MM:SS.ssssss' в формат 'DD.MM.YYYY'.
    Если дата некорректна, возвращает: "Ошибка: Неверная дата"
    """
    input_string = input_string.strip()

    if not input_string:
        return ""

    try:
        # Убираем часть времени, чтобы парсить только дату
        date_str = input_string[:-7]
        date_object = datetime.fromisoformat(date_str)
        return date_object.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: Неверная дата"