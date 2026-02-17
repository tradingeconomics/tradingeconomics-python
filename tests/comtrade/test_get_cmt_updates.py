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
        https://api.tradingeconomics.com/comtrade/updates
        """

        mock_dataRequest.return_value = {"status": "ok"}

        result = getCmtUpdates()

        expected_url = "/comtrade/updates"

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type=None
        )
        self.assertEqual(result, {"status": "ok"})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_updates_with_df_output(self, mock_dataRequest):
        """
        getCmtUpdates(output_type='df') should pass output_type to dataRequest
        """
        mock_dataRequest.return_value = "DataFrame"

        result = getCmtUpdates(output_type="df")

        expected_url = "/comtrade/updates"

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type="df"
        )
        self.assertEqual(result, "DataFrame")

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_updates_with_raw_output(self, mock_dataRequest):
        """
        getCmtUpdates(output_type='raw') should pass output_type to dataRequest
        """
        mock_dataRequest.return_value = [{"raw": "data"}]

        result = getCmtUpdates(output_type="raw")

        expected_url = "/comtrade/updates"

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"raw": "data"}])


if __name__ == "__main__":
    unittest.main()
