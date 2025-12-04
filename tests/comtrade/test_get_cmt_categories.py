# FILE: tests/comtrade/test_getCmtCategories.py
# Unit tests for getCmtCategories()
# - Tests URL generation
# - Tests passthrough of fn.dataRequest

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import getCmtCategories


class TestGetCmtCategories(unittest.TestCase):
    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_categories_basic(self, mock_dataRequest):
        """
        getCmtCategories() should call dataRequest with:
        https://api.tradingeconomics.com/comtrade/categories
        """

        mock_dataRequest.return_value = {"categories": "ok"}

        result = getCmtCategories()

        expected_url = "https://api.tradingeconomics.com/comtrade/categories"

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"categories": "ok"})


if __name__ == "__main__":
    unittest.main()