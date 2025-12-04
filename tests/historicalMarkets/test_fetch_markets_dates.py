import unittest
from unittest.mock import patch
from tradingeconomics.historicalMarkets import fetchMarkets
from tradingeconomics import glob


class TestFetchMarketsDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalMarkets.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value={"markets": "with_init"},
    )
    def test_fetch_markets_with_init_date(self, mock_request, mock_validate):
        # Get historical markets data with init date only
        result = fetchMarkets(symbol="indu:ind", initDate="2017-01-01")

        expected_url = "https://api.tradingeconomics.com/markets/historical/indu%3Aind?d1=2017-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "with_init"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalMarkets.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historicalMarkets.fn.validatePeriod")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value={"markets": "with_dates"},
    )
    def test_fetch_markets_with_date_range(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get historical markets data with date range
        result = fetchMarkets(
            symbol="indu:ind", initDate="2017-01-01", endDate="2017-06-15"
        )

        expected_url = "https://api.tradingeconomics.com/markets/historical/indu%3Aind?d1=2017-01-01&d2=2017-06-15"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "with_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value={"markets": "end_only"},
    )
    def test_fetch_markets_with_end_date_only(self, mock_request):
        # When only endDate is provided, initDate is auto-calculated as 1 month before
        result = fetchMarkets(symbol="indu:ind", endDate="2017-06-15")

        # initDate should be 2017-05-15 (1 month before endDate)
        expected_url = "https://api.tradingeconomics.com/markets/historical/indu%3Aind?d1=2017-05-15&d2=2017-06-15"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "end_only"})
