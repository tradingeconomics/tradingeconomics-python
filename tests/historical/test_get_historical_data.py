import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalData
from tradingeconomics import glob


class TestGetHistoricalData(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.finalLink",
        side_effect=lambda url, dates: url + "/" + "/".join(dates),
    )
    @patch(
        "tradingeconomics.historical.fn.dataRequest", return_value={"historical": "ok"}
    )
    def test_historical_country_and_indicator(self, mock_request, mock_final_link):
        # Get historical data for country and indicator (auto-adds 15-year lookback)
        result = getHistoricalData(country="United States", indicator="Imports")

        # When no dates provided, auto-adds 15 years lookback date
        # Expected URL will have auto-generated date appended
        assert mock_request.called
        call_args = mock_request.call_args[1]
        assert call_args["output_type"] is None
        self.assertEqual(result, {"historical": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.finalLink",
        side_effect=lambda url, dates: url + "/" + "/".join(dates),
    )
    @patch("tradingeconomics.historical.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historical.fn.validatePeriod")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"historical": "with_dates"},
    )
    def test_historical_with_dates(
        self, mock_request, mock_validate_period, mock_validate, mock_final_link
    ):
        # Get historical data with date range
        result = getHistoricalData(
            country="United States",
            indicator="Imports",
            initDate="2011-01-01",
            endDate="2016-01-01",
        )

        expected_url = "https://api.tradingeconomics.com/historical/country/United%20States/indicator/Imports/2011-01-01/2016-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "with_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.finalLink",
        side_effect=lambda url, dates: url + "/" + "/".join(dates),
    )
    @patch("tradingeconomics.historical.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"historical": "init_only"},
    )
    def test_historical_with_init_date_only(
        self, mock_request, mock_validate, mock_final_link
    ):
        # Get historical data with only init date
        result = getHistoricalData(
            country="United States", indicator="GDP", initDate="2020-01-01"
        )

        expected_url = "https://api.tradingeconomics.com/historical/country/United%20States/indicator/GDP/2020-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "init_only"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.finalLink",
        side_effect=lambda url, dates: url + "/" + "/".join(dates),
    )
    @patch("tradingeconomics.historical.fn.dataRequest", return_value=[{"value": 100}])
    def test_historical_with_output_type(self, mock_request, mock_final_link):
        # Test with output_type parameter (auto-adds 15-year lookback)
        result = getHistoricalData(
            country="United States", indicator="Imports", output_type="df"
        )

        # Verify output_type was passed correctly
        assert mock_request.called
        call_args = mock_request.call_args[1]
        assert call_args["output_type"] == "df"
        self.assertEqual(result, [{"value": 100}])
