# FILE: tests/comtrade/test_getCmtUpdates.py
# Unit tests for getCmtUpdates()
# - Tests URL generation
# - Tests passthrough of fn.dataRequest

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import getCmtUpdates


class TestGetCmtUpdates(unittest.TestCase):
    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_updates_basic(self, mock_dataRequest):
        """
        getCmtUpdates() should call dataRequest with
        https://api.tradingeconomics.com/comtrade/updates?c=guest:guest
        """

        mock_dataRequest.return_value = {"status": "ok"}

        result = getCmtUpdates()

        expected_url = "https://api.tradingeconomics.com/comtrade/updates?c=guest:guest"

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"status": "ok"})


if __name__ == "__main__":
    unittest.main()