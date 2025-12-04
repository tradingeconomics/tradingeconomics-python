import unittest
from unittest.mock import patch
from tradingeconomics.historicalMarkets import fetchMarkets
from tradingeconomics import glob


class TestFetchMarketsMultipleSymbolsWithDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalMarkets.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historicalMarkets.fn.validatePeriod")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value={"markets": "multiple_with_dates"},
    )
    def test_fetch_markets_multiple_symbols_with_dates(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get historical markets data for multiple symbols with date range
        result = fetchMarkets(
            symbol=["aapl:us", "indu:ind"], initDate="2017-01-01", endDate="2017-06-15"
        )

        expected_url = "https://api.tradingeconomics.com/markets/historical/aapl%3Aus%2Cindu%3Aind?c=TESTKEY&d1=2017-01-01&d2=2017-06-15"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "multiple_with_dates"})
