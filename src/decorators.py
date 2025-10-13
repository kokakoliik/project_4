import logging
import os
import functools
from typing import Callable, Optional, TypeVar, ParamSpec
from datetime import datetime


# Настройка логирования
def setup_logger(filename: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(message)s")

    if filename is not None:
        log_file = os.path.join("logs", filename)
        os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Создание папки, если не существует
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


P = ParamSpec('P')
R = TypeVar('R')


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор для логирования вызовов функции.
    """
    logger = setup_logger(filename)  # Предполагается, что setup_logger определена где-то

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            function_name = func.__name__
            start_time = datetime.now()
            logger.info(f"{function_name} called at {start_time.isoformat()} with args: {args} and kwargs: {kwargs}")

            try:
                result = func(*args, **kwargs)
                logger.info(f"{function_name} result: {result}")
                return result
            except Exception as e:
                error_message = f"{function_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                logger.error(error_message)
                raise

        return wrapper

    return decorator
