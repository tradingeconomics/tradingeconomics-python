import unittest
from unittest.mock import patch
from tradingeconomics.markets import getMarketsIntraday
from tradingeconomics import glob


class TestGetMarketsIntraday(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"intraday": "ok"})
    def test_get_markets_intraday_single(self, mock_request):
        # Get intraday data for single symbol
        result = getMarketsIntraday(symbols="indu:ind")

        expected_url = "/markets/intraday/indu%3Aind"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"intraday": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"intraday": "multiple"}
    )
    def test_get_markets_intraday_multiple(self, mock_request):
        # Get intraday data for multiple symbols
        result = getMarketsIntraday(symbols=["aapl:us", "indu:ind"])

        expected_url = "/markets/intraday/aapl%3Aus%2Cindu%3Aind"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"intraday": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.markets.fn.dataRequest",
        return_value={"intraday": "with_date"},
    )
    def test_get_markets_intraday_with_init_date(self, mock_request, mock_validate):
        # Get intraday data with init date
        result = getMarketsIntraday(symbols="indu:ind", initDate="2018-03-13")

        expected_url = "/markets/intraday/indu%3Aind?d1=2018-03-13"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"intraday": "with_date"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.markets.fn.validatePeriod")
    @patch(
        "tradingeconomics.markets.fn.dataRequest",
        return_value={"intraday": "date_range"},
    )
    def test_get_markets_intraday_with_date_range(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get intraday data with date range
        result = getMarketsIntraday(
            symbols=["aapl:us", "indu:ind"],
            initDate="2022-01-01",
            endDate="2022-12-31",
            output_type="raw",
        )

        expected_url = (
            "/markets/intraday/aapl%3Aus%2Cindu%3Aind?d1=2022-01-01&d2=2022-12-31"
        )

        mock_request.assert_called_once_with(expected_url, "raw")
        self.assertEqual(result, {"intraday": "date_range"})
