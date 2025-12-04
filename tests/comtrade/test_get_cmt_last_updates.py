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

        expected_url = "/comtrade/updates/country/" "portugal"

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

        expected_url = "/comtrade/updates/country/" "portugal?from=2022-01-01"

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

        expected_url = "/comtrade/updates/country/all"

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type=None
        )
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_start_date_only(self, mock_dataRequest):
        """
        If only start_date is provided (no country), URL should default to /all
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtLastUpdates(start_date="2022-06-01")

        expected_url = "/comtrade/updates/country/all?from=2022-06-01"

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type=None
        )
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_with_output_type_df(self, mock_dataRequest):
        """
        Test output_type='df' is passed correctly
        """
        mock_dataRequest.return_value = "DataFrame"

        result = getCmtLastUpdates(
            country="portugal", start_date="2022-01-01", output_type="df"
        )

        expected_url = "/comtrade/updates/country/portugal?from=2022-01-01"

        mock_dataRequest.assert_called_once_with(
            api_request=expected_url, output_type="df"
        )
        self.assertEqual(result, "DataFrame")


if __name__ == "__main__":
    unittest.main()
