from datetime import datetime
from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_data: List[Dict[str, Any]]) -> None:
    result = filter_by_state(sample_data)
    # Проверяем, что все результаты с state == "EXECUTED"
    assert all(item.get("state") == "EXECUTED" for item in result)
    # Проверяем, что 4 элемента
    assert len(result) == 6


def test_sort_by_date(sample_data: List[Dict[str, Any]]) -> None:
    sorted_list = sort_by_date(sample_data)
    # Проверяем, что список отсортирован по дате по убыванию
    dates = []
    for item in sorted_list:
        d = item.get("date")
        if d is None:
            dates.append(datetime.min)
        elif d == "invalid-date":
            dates.append(datetime.min)
        else:
            try:
                dates.append(datetime.fromisoformat(d))
            except Exception:
                dates.append(datetime.min)
    # Проверка сортировки
    assert dates == sorted(dates, reverse=True)


# Дополнительно можно проверить порядок элементов для уверенности
def test_ordering_of_sorted_data(sample_data: List[Dict[str, Any]]) -> None:
    sorted_list = sort_by_date(sample_data)
    # Даты должны быть в убывающем порядке
    dates = []
    for item in sorted_list:
        d = item.get("date")
        if d is None or d == "invalid-date":
            dates.append(datetime.min)
        else:
            dates.append(datetime.fromisoformat(d))
    assert all(earlier >= later for earlier, later in zip(dates, dates[1:]))
