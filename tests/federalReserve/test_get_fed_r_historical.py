import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRHistorical
from tradingeconomics import glob


class TestGetFedRHistorical(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"historical": "ok"},
    )
    def test_historical_symbol_single(self, mock_request):
        # Get historical data for single symbol
        result = getFedRHistorical(symbol="racedisparity005007")

        expected_url = "/fred/historical/racedisparity005007"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.stringOrList",
        return_value="racedisparity005007%2C2020ratio002013",
    )
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"historical": "multiple"},
    )
    def test_historical_symbol_multiple(self, mock_request, mock_string_or_list):
        # Get historical data for multiple symbols
        result = getFedRHistorical(symbol=["racedisparity005007", "2020ratio002013"])

        expected_url = "/fred/historical/racedisparity005007%2C2020ratio002013"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.federalReserve.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.federalReserve.fn.stringOrList",
        return_value="racedisparity005007",
    )
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"historical": "with_date"},
    )
    def test_historical_with_init_date(
        self, mock_request, mock_string_or_list, mock_validate
    ):
        # Get historical data with start date
        result = getFedRHistorical(symbol="racedisparity005007", initDate="2018-05-01")

        expected_url = "/fred/historical/racedisparity005007?d1=2018-05-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "with_date"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.federalReserve.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.federalReserve.fn.validatePeriod")
    @patch(
        "tradingeconomics.federalReserve.fn.stringOrList",
        return_value="racedisparity005007",
    )
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"historical": "with_dates"},
    )
    def test_historical_with_date_range(
        self, mock_request, mock_string_or_list, mock_validate_period, mock_validate
    ):
        # Get historical data with date range
        result = getFedRHistorical(
            symbol="racedisparity005007", initDate="2017-05-01", endDate="2019-01-01"
        )

        expected_url = (
            "/fred/historical/racedisparity005007?d1=2017-05-01&d2=2019-01-01"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "with_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"date": "2018-05-01"}],
    )
    def test_historical_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getFedRHistorical(symbol="racedisparity005007", output_type="df")

        expected_url = "/fred/historical/racedisparity005007"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"date": "2018-05-01"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"date": "2020-01-01"}],
    )
    def test_historical_output_type_raw(self, mock_request):
        result = getFedRHistorical(symbol="2020ratio002013", output_type="raw")

        expected_url = "/fred/historical/2020ratio002013"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"date": "2020-01-01"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.federalReserve.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.federalReserve.fn.stringOrList",
        return_value="racedisparity005007",
    )
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"date": "2019-01-01"}],
    )
    def test_historical_with_only_end_date(
        self, mock_request, mock_string_or_list, mock_validate
    ):
        result = getFedRHistorical(symbol="racedisparity005007", endDate="2019-01-01")

        expected_url = "/fred/historical/racedisparity005007&d2=2019-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, [{"date": "2019-01-01"}])
