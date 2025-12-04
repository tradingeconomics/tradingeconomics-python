import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatData
from tradingeconomics import glob


class TestGetEurostatDataCategory(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"category": "ok"})
    def test_category_parameter_single(self, mock_request):
        # Provide a single category and ensure URL is built correctly
        result = getEurostatData(
            category="People at risk of income poverty after social transfers"
        )

        expected_url = "/eurostat?category=People%20at%20risk%20of%20income%20poverty%20after%20social%20transfers"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"category": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest",
        return_value={"category": "multiple"},
    )
    def test_category_parameter_multiple(self, mock_request):
        # Provide multiple categories and ensure URL is built correctly
        result = getEurostatData(category=["Category1", "Category2"])

        expected_url = "/eurostat?category=Category1%2CCategory2"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"category": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"category": "df"})
    def test_category_output_type_df(self, mock_request):
        result = getEurostatData(
            category="People at risk of income poverty after social transfers",
            output_type="df",
        )

        expected_url = "/eurostat?category=People%20at%20risk%20of%20income%20poverty%20after%20social%20transfers"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"category": "df"})
