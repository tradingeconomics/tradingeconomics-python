import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatData
from tradingeconomics import glob


class TestGetEurostatDataCombined(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"combined": "ok"})
    def test_country_and_category(self, mock_request):
        # Provide country and category together
        result = getEurostatData(
            country="Denmark",
            category="People at risk of income poverty after social transfers",
        )

        expected_url = "/eurostat/country/Denmark?category=People%20at%20risk%20of%20income%20poverty%20after%20social%20transfers"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"combined": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"combined": "ok"})
    def test_country_and_category_group(self, mock_request):
        # Provide country and category_group together
        result = getEurostatData(country="Denmark", category_group="Poverty")

        expected_url = "/eurostat/country/Denmark?category_group=Poverty"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"combined": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"combined": "df"})
    def test_country_and_category_output_type_df(self, mock_request):
        result = getEurostatData(
            country="Denmark",
            category="People at risk of income poverty after social transfers",
            output_type="df",
        )

        expected_url = "/eurostat/country/Denmark?category=People%20at%20risk%20of%20income%20poverty%20after%20social%20transfers"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"combined": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"combined": "df"})
    def test_country_and_category_group_output_type_df(self, mock_request):
        result = getEurostatData(
            country="Denmark", category_group="Poverty", output_type="df"
        )

        expected_url = "/eurostat/country/Denmark?category_group=Poverty"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"combined": "df"})
