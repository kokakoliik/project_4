import json
import logging
import os
from typing import Any, Dict, List

if not os.path.exists("logs"):
    os.makedirs("logs")


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)


file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)


logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загрузить транзакции из JSON-файла.
    """
    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Транзакции успешно загружены из файла: {file_path}")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком.")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при декодировании JSON из файла {file_path}: {e}")
        return []
