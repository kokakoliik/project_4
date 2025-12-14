import logging
import os
from typing import Union

# Создание папки logs, если она не существует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Настройка логирования для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("../logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Форматирование логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """
    Маскирует номер карты,  показывая первые 6 цифр и последние 4 цифры
    """
    logger.debug(f"Получение маски для номера карты: {card_number}")

    card_number_str = str(card_number)

    card_number_clear = card_number_str.replace(" ", "")

    if len(card_number_clear) != 16:
        logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
        return "Ошибка: Номер карты должен содержать 16 цифр."

    masked_card = f"{card_number_clear[:6]}******{card_number_clear[-4:]}"

    mask_card = " ".join(masked_card[i : i + 4] for i in range(0, len(masked_card), 4))
    logger.info(f"Маска карты успешно создана: {mask_card}")

    return mask_card


def get_mask_account(account_number: Union[str | int]) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры
    """
    logger.debug(f"Получение маски для номера счета: {account_number}")

    account_number_str = str(account_number)

    account_number_clear = account_number_str.replace(" ", "")

    if len(account_number_clear) != 20:
        logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
        return "Ошибка: Номер счета должен содержать 20 цифр."

    mask_account = "**" + account_number_clear[-4:]
    logger.info(f"Маска счета успешно создана: {mask_account}")

    return mask_account
