import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getIndicatorData
from tradingeconomics import glob


class TestGetIndicatorData(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"indicators": "all"}
    )
    def test_get_indicator_data_no_parameters(self, mock_request):
        # Get all indicators
        result = getIndicatorData()

        expected_url = "/indicators/"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicators": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"indicators": "country"},
    )
    def test_get_indicator_data_by_country(self, mock_request):
        # Get indicators by country
        result = getIndicatorData(country="United States")

        expected_url = "/country/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicators": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"indicators": "countries"},
    )
    def test_get_indicator_data_by_multiple_countries(self, mock_request):
        # Get indicators by multiple countries
        result = getIndicatorData(country=["United States", "Portugal"])

        expected_url = "/country/United%20States%2CPortugal"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicators": "countries"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"indicators": "indicator"},
    )
    def test_get_indicator_data_by_indicators(self, mock_request):
        # Get data for specific indicators across all countries
        result = getIndicatorData(indicators="Imports")

        expected_url = "/country/all/Imports"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicators": "indicator"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"indicators": "indicators"},
    )
    def test_get_indicator_data_by_multiple_indicators(self, mock_request):
        # Get data for multiple indicators across all countries
        result = getIndicatorData(indicators=["Imports", "Exports"])

        expected_url = "/country/all/Imports%2CExports"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicators": "indicators"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "indicators": "data"},
    )
    def test_get_indicator_data_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getIndicatorData(country="United States", output_type="raw")

        expected_url = "/country/united%20states"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "indicators": "data"})

    def test_get_indicator_data_country_and_indicators_error(self):
        # Test that error is returned when both country and indicators are provided
        result = getIndicatorData(country="United States", indicators="Imports")

        self.assertEqual(
            result,
            "Error: You can not use both country and indicators parameters at the same time.",
        )
