import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import getWBCountry
from tradingeconomics import glob


class TestGetWBCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"country": "single_country"},
    )
    def test_get_wb_country_single_country(self, mock_request):
        # Get indicators for single country
        result = getWBCountry(country="portugal")

        expected_url = (
            "https://api.tradingeconomics.com/worldBank/country/portugal"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "single_country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"country": "multiple_countries"},
    )
    def test_get_wb_country_multiple_countries(self, mock_request):
        # Get indicators for multiple countries
        result = getWBCountry(country=["portugal", "spain"])

        expected_url = "https://api.tradingeconomics.com/worldBank/country/portugal,spain"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "multiple_countries"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"country": "country_with_page"},
    )
    def test_get_wb_country_with_page_number(self, mock_request):
        # Get country indicators with page number
        result = getWBCountry(country="portugal", page_number=3)

        expected_url = (
            "https://api.tradingeconomics.com/worldBank/country/portugal/3"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "country_with_page"})

    def test_get_wb_country_no_parameters(self):
        # Test that error message is returned when no country provided
        result = getWBCountry()

        self.assertEqual(result, "A country is required!")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.worldBank.fn.dataRequest", return_value="df_output")
    def test_get_wb_country_with_output_type(self, mock_request):
        # Get country with DataFrame output type
        result = getWBCountry(country="portugal", output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/worldBank/country/portugal"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, "df_output")


if __name__ == "__main__":
    unittest.main()
