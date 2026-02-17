import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getIndicatorByCategoryGroup
from tradingeconomics import glob


class TestGetIndicatorByCategoryGroup(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"category": "ok"}
    )
    def test_get_indicator_by_category_group(self, mock_request):
        # Get indicators by country and category group
        result = getIndicatorByCategoryGroup(
            country="united states", category_group="gdp"
        )

        expected_url = "/country/united%20states?group=gdp"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"category": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"category": "multiple"},
    )
    def test_get_indicator_by_category_group_multiple_countries(self, mock_request):
        # Get indicators by multiple countries and category group
        result = getIndicatorByCategoryGroup(
            country=["united states", "china"], category_group="markets"
        )

        expected_url = "/country/united%20states,china?group=markets"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"category": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"category": "df"}
    )
    def test_get_indicator_by_category_group_with_output_type(self, mock_request):
        # Get indicators with output type
        result = getIndicatorByCategoryGroup(
            country="united states", category_group="gdp", output_type="df"
        )

        expected_url = "/country/united%20states?group=gdp"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"category": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "category": "data"},
    )
    def test_get_indicator_by_category_group_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getIndicatorByCategoryGroup(
            country="united states", category_group="gdp", output_type="raw"
        )

        expected_url = "/country/united%20states?group=gdp"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "category": "data"})

    def test_get_indicator_by_category_group_missing_parameters(self):
        # Test error when parameters are missing
        result = getIndicatorByCategoryGroup()

        self.assertEqual(result, "Country and category are required")

    def test_get_indicator_by_category_group_missing_category(self):
        # Test error when category is missing
        result = getIndicatorByCategoryGroup(country="united states")

        self.assertEqual(result, "Country and category are required")
