import unittest
from unittest.mock import patch
from tradingeconomics import stream


class TestOnError(unittest.TestCase):

    @patch("builtins.print")
    def test_on_error_prints_error(self, mock_print):
        # Test that on_error prints the error message
        mock_ws = None
        error_message = "Connection failed"

        stream.on_error(mock_ws, error_message)

        mock_print.assert_called_once_with(error_message)

    @patch("builtins.print")
    def test_on_error_with_exception(self, mock_print):
        # Test on_error with exception object
        mock_ws = None
        error = Exception("Test exception")

        stream.on_error(mock_ws, error)

        mock_print.assert_called_once_with(error)


if __name__ == "__main__":
    unittest.main()
