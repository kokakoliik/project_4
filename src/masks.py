from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """
    Маскирует номер карты,  показывая первые 6 цифр и последние 4 цифры
    """
    card_number_str = str(card_number)

    card_number_clear = card_number_str.replace(" ", "")

    if len(card_number_clear) != 16:
        return "Ошибка: Номер карты должен содержать 16 цифр."

    masked_card = f"{card_number_clear[:6]}******{card_number_clear[-4:]}"

    mask_card = " ".join(masked_card[i : i + 4] for i in range(0, len(masked_card), 4))
    return mask_card


def get_mask_account(account_number: Union[str | int]) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры
    """
    account_number_str = str(account_number)

    account_number_clear = account_number_str.replace(" ", "")

    if len(account_number_clear) != 20:
        return "Ошибка: Номер счета должен содержать 20 цифр."

    mask_account = "**" + account_number_clear[-4:]
    return mask_account
