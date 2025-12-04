import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getDiscontinuedIndicator
from tradingeconomics import glob


class TestGetDiscontinuedIndicator(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"discontinued": "all"},
    )
    def test_get_discontinued_indicator_no_parameters(self, mock_request):
        # Get all discontinued indicators
        result = getDiscontinuedIndicator()

        expected_url = "/country/all/discontinued"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"discontinued": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"discontinued": "country"},
    )
    def test_get_discontinued_indicator_by_country(self, mock_request):
        # Get discontinued indicators by country
        result = getDiscontinuedIndicator(country="china")

        expected_url = "/country/china/discontinued"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"discontinued": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"discontinued": "countries"},
    )
    def test_get_discontinued_indicator_by_multiple_countries(self, mock_request):
        # Get discontinued indicators by multiple countries
        result = getDiscontinuedIndicator(country=["united states", "china"])

        expected_url = "/country/united%20states,china/discontinued"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"discontinued": "countries"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"discontinued": "df"},
    )
    def test_get_discontinued_indicator_with_output_type(self, mock_request):
        # Get discontinued indicators with output type
        result = getDiscontinuedIndicator(country="china", output_type="df")

        expected_url = "/country/china/discontinued"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"discontinued": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "discontinued": "data"},
    )
    def test_get_discontinued_indicator_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getDiscontinuedIndicator(country="china", output_type="raw")

        expected_url = "/country/china/discontinued"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "discontinued": "data"})
