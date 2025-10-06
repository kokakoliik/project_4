from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    def get_date(item: Dict[str, Any]) -> datetime:
        date_str = item.get("date")
        if not date_str:
            return datetime.min
        try:
            return datetime.fromisoformat(date_str)
        except Exception:
            return datetime.min

    return sorted(data, key=get_date, reverse=descending)
