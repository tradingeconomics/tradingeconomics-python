import unittest
from unittest.mock import patch
from tradingeconomics.markets import getMarketsForecasts
from tradingeconomics import glob


class TestGetMarketsForecasts(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest",
        return_value={"forecasts": "category"},
    )
    def test_get_markets_forecasts_by_category(self, mock_request):
        # Get markets forecasts by category
        result = getMarketsForecasts(category="bond")

        expected_url = "/markets/forecasts/bond"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"forecasts": "category"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"forecasts": "symbol"}
    )
    def test_get_markets_forecasts_by_symbol(self, mock_request):
        # Get markets forecasts by symbol
        result = getMarketsForecasts(symbol="indu:ind")

        expected_url = "/markets/forecasts/symbol/indu%3Aind"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"forecasts": "symbol"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"forecasts": "symbols"}
    )
    def test_get_markets_forecasts_by_multiple_symbols(self, mock_request):
        # Get markets forecasts by multiple symbols
        result = getMarketsForecasts(symbol=["psi20:ind", "indu:ind"], output_type="df")

        expected_url = "/markets/forecasts/symbol/psi20%3Aind%2Cindu%3Aind"

        mock_request.assert_called_once_with(expected_url, "df")
        self.assertEqual(result, {"forecasts": "symbols"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest",
        return_value={"raw": "json", "forecasts": "data"},
    )
    def test_get_markets_forecasts_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getMarketsForecasts(category="bond", output_type="raw")

        expected_url = "/markets/forecasts/bond"

        mock_request.assert_called_once_with(expected_url, "raw")
        self.assertEqual(result, {"raw": "json", "forecasts": "data"})
