import unittest
from typing import Any
from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub
from src.utils import load_transactions


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_transactions_empty_file(self, mock_file: Any) -> None:
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_load_transactions_valid_file(self, mock_file: Any, mock_isfile: Any) -> None:
        result = load_transactions("data/operations.json")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 100)

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_load_transactions_invalid_json(self, mock_file: Any) -> None:
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=False)
    def test_load_transactions_file_not_exist(self, mock_isfile: Any) -> None:
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
    def test_load_transactions_not_a_list(self, mock_file: Any, mock_isfile: Any) -> None:
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])

    @patch("requests.get")
    def test_convert_to_rub(self, mock_get: Any) -> None:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 7500}

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)


if __name__ == "__main__":
    unittest.main()  # Запуск тестов
