from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """
    Маскирует номер карты, показывая первые 6 цифр и последние 4 цифры
    """
    card_number_str = str(card_number)

    if len(card_number_str) != 16:
        raise ValueError("Ошибка: Номер карты должен содержать 16 цифр.")

    mask_card = f"{card_number_str[:6]}******{card_number_str[-4:]}"
    return " ".join(mask_card[i : i + 4] for i in range(0, len(mask_card), 4))


def get_mask_account(account_number: Union[str | int]) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры
    """
    account_number_str = str(account_number)

    if len(account_number_str) != 20:
        raise ValueError("Ошибка: Номер счета должен содержать 20 цифр.")

    mask_account = "**" + account_number_str[-4:]
    return mask_account
