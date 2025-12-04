import unittest
from unittest.mock import patch
from tradingeconomics.historicalEurostat import getHistoricalEurostat
from tradingeconomics import glob


class TestGetHistoricalEurostatDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalEurostat.fn.dataRequest",
        return_value={"historical": "with_init"},
    )
    def test_historical_eurostat_with_init_date(self, mock_request):
        # Get historical Eurostat data with init date only
        result = getHistoricalEurostat(ID="24804", initDate="2015-01-01")

        expected_url = "https://api.tradingeconomics.com/eurostat/historical/24804?d1=2015-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "with_init"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalEurostat.fn.dataRequest",
        return_value={"historical": "with_dates"},
    )
    def test_historical_eurostat_with_date_range(self, mock_request):
        # Get historical Eurostat data with date range
        result = getHistoricalEurostat(
            ID="24804", initDate="2015-01-01", endDate="2020-01-01"
        )

        expected_url = "https://api.tradingeconomics.com/eurostat/historical/24804?d1=2015-01-01&d2=2020-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "with_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalEurostat.fn.dataRequest",
        return_value={"historical": "with_dates_list"},
    )
    def test_historical_eurostat_multiple_ids_with_dates(self, mock_request):
        # Get historical Eurostat data for multiple IDs with date range
        result = getHistoricalEurostat(
            ID=["24804", "24805"], initDate="2015-01-01", endDate="2020-01-01"
        )

        expected_url = "https://api.tradingeconomics.com/eurostat/historical/24804%2C24805?d1=2015-01-01&d2=2020-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "with_dates_list"})
