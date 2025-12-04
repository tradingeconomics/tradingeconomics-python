import unittest
from unittest.mock import patch
from tradingeconomics.markets import getCurrencyCross, ParametersError
from tradingeconomics import glob


class TestGetCurrencyCross(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"currency": "eur"})
    def test_get_currency_cross(self, mock_request):
        # Get currency cross for EUR
        result = getCurrencyCross(cross="EUR")

        expected_url = (
            "https://api.tradingeconomics.com/markets/currency?cross=EUR&c=TESTKEY"
        )

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"currency": "eur"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"currency": "usd"})
    def test_get_currency_cross_with_output_type(self, mock_request):
        # Get currency cross with output type
        result = getCurrencyCross(cross="EUR", output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/markets/currency?cross=EUR&c=TESTKEY"
        )

        mock_request.assert_called_once_with(expected_url, "df")
        self.assertEqual(result, {"currency": "usd"})

    def test_get_currency_cross_no_cross(self):
        # Test error when cross is not provided
        with self.assertRaises(ParametersError) as context:
            getCurrencyCross(cross=None)

        self.assertEqual(
            str(context.exception), "You must provide a cross for your currency pair"
        )
