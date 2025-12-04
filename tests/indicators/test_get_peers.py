import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getPeers
from tradingeconomics import glob


class TestGetPeers(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"peers": "ticker"}
    )
    def test_get_peers_by_ticker(self, mock_request):
        # Get peers by ticker
        result = getPeers(ticker="CPI YOY")

        expected_url = "/peers/CPI%20YOY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"peers": "ticker"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"peers": "country"}
    )
    def test_get_peers_by_country(self, mock_request):
        # Get peers by country
        result = getPeers(country="united states")

        expected_url = "/peers/country/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"peers": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"peers": "country_category"},
    )
    def test_get_peers_by_country_and_category(self, mock_request):
        # Get peers by country and category
        result = getPeers(country="united states", category="money")

        expected_url = "/peers/country/united%20states/money"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"peers": "country_category"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.dataRequest", return_value={"peers": "df"})
    def test_get_peers_with_output_type(self, mock_request):
        # Get peers with output type
        result = getPeers(country="united states", output_type="df")

        expected_url = "/peers/country/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"peers": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "peers": "data"},
    )
    def test_get_peers_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getPeers(country="united states", output_type="raw")

        expected_url = "/peers/country/united%20states"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "peers": "data"})
