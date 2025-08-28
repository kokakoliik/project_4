from datetime import datetime


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    """
    parts = input_string.split()
    card_type = " ".join(parts[:-1])
    card_number_str = parts[-1]

    try:
        if "счет" in card_type.lower():
            masked_number = "**" + input_string[-4:]
        elif len(card_number_str) == 16:
            masked_card = f"{input_string[-16:-10]}******{input_string[-4:]}"
            masked_number = " ".join(masked_card[i:i + 4] for i in range(0, len(masked_card), 4))
        else:
            raise ValueError("Неверный формат номера счета или карты")
        return f"{card_type} {masked_number}"
    except ValueError as e:
        return f"Ошибка: {e}"


def get_date(input_string: str) -> str:
    """
    Преобразует строку с датой в формате 'YYYY-MM-DDTHH:MM:SS.ssssss' в формат 'DD.MM.YYYY'.
    """
    input_string = input_string.strip()

    if not input_string:
        return ""

    try:
        date_object = datetime.fromisoformat(input_string[:-7])
        return date_object.strftime("%d.%m.%Y")
    except ValueError:
        return ""
