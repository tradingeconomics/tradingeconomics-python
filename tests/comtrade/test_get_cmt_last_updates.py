# FILE: tests/comtrade/test_getCmtLastUpdates.py
# Unit tests for getCmtLastUpdates()
# - Tests URL generation
# - Tests passthrough of fn.dataRequest return value

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import getCmtLastUpdates


class TestGetCmtLastUpdates(unittest.TestCase):
    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_country_only(self, mock_dataRequest):
        """
        If only country is provided, URL must include /updates/country/<country>
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtLastUpdates(country="portugal")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/updates/country/" "portugal"
        )

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type=None
        )
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_country_and_start_date(self, mock_dataRequest):
        """
        If both country and start_date are provided, URL must include &from=<date>
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtLastUpdates(country="portugal", start_date="2022-01-01")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/updates/country/"
            "portugal?from=2022-01-01"
        )

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type=None
        )
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_no_country(self, mock_dataRequest):
        """
        If no country is provided, URL must become /updates/country/all
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtLastUpdates(start_date=None)

        expected_url = "https://api.tradingeconomics.com/comtrade/updates/country/all"

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type=None
        )
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
