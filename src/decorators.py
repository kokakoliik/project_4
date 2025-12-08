import datetime
from typing import Any, Callable, Optional, TypeVar, cast

T = TypeVar("T")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Декоратор для логирования начала и конца выполнения функции,
    а также результатов или ошибок.

    Args:
        filename: Путь к файлу для записи логов. Если None - вывод в консоль.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            # Формируем строку с входными параметрами
            args_str = ", ".join([repr(arg) for arg in args])
            kwargs_str = ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])
            params_str = ", ".join(filter(None, [args_str, kwargs_str]))

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            start_message = f"{timestamp} - {func.__name__} started with params: ({params_str})"

            # Логируем начало выполнения
            write_log(start_message, filename)

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение
                end_message = f"{timestamp} - {func.__name__} finished. Result: {result}"
                write_log(end_message, filename)

                return result

            except Exception as e:
                # Логируем ошибку
                error_message = (
                    f"{timestamp} - {func.__name__} failed with error: {type(e).__name__}: {e}. "
                    f"Params: ({params_str})"
                )
                write_log(error_message, filename)
                raise  # Пробрасываем исключение дальше

        # Вручную копируем метаданные функции вместо использования functools.wraps
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        wrapper.__qualname__ = func.__qualname__
        wrapper.__annotations__ = func.__annotations__

        return cast(Callable[..., T], wrapper)

    return decorator


def write_log(message: str, filename: Optional[str] = None) -> None:
    """
    Вспомогательная функция для записи лога в файл или консоль.

    Args:
        message: Сообщение для записи
        filename: Путь к файлу или None для вывода в консоль
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)
