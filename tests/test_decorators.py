from typing import Any

import pytest

from src.decorators import log


# Пример успешной функции
@log(filename="../logs/mylog.txt")
def successful_function(x: Any, y: Any) -> Any:
    return x + y


# Пример функции, которая вызывает ошибку
@log(filename="../logs/mylog.txt")
def error_function(x: Any, y: Any) -> Any:
    return x / y


def test_successful_function(capsys: Any) -> None:
    result = successful_function(1, 2)
    assert result == 3

    with open("../logs/mylog.txt", "r") as log_file:
        log_content = log_file.readlines()
        # Проверка, что лог содержит строку о запуске
        assert any("successful_function started with params" in line for line in log_content)
        # Проверка, что лог содержит строку о завершении и результате
        assert any("successful_function finished. Result: 3" in line for line in log_content)


def test_error_function(capsys: Any) -> None:
    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)
    with open("../logs/mylog.txt", "r") as log_file:
        log_content = log_file.readlines()
        assert any("error_function failed with error: ZeroDivisionError" in line for line in log_content)
