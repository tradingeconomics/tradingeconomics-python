import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getIndicatorData
from tradingeconomics import glob


class TestGetIndicatorDataCalendar(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"calendar": "all"}
    )
    def test_get_indicator_data_calendar(self, mock_request):
        # Get indicators with calendar events
        result = getIndicatorData(calendar=1)

        expected_url = (
            "https://api.tradingeconomics.com/indicators?calendar=1"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"calendar": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"calendar": "country"},
    )
    def test_get_indicator_data_calendar_with_country(self, mock_request):
        # Get indicators with calendar events for specific country
        result = getIndicatorData(country="United States", calendar=1)

        expected_url = "https://api.tradingeconomics.com/indicators?calendar=1&country=United%20States"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"calendar": "country"})
