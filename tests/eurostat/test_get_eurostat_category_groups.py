import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatCategoryGroups
from tradingeconomics import glob


class TestGetEurostatCategoryGroups(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest", return_value={"categories": "ok"}
    )
    def test_get_eurostat_category_groups(self, mock_request):
        # Test getEurostatCategoryGroups function
        result = getEurostatCategoryGroups()

        expected_url = "https://api.tradingeconomics.com/eurostat/categories?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"categories": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest",
        return_value=[{"category": "Poverty"}],
    )
    def test_get_eurostat_category_groups_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getEurostatCategoryGroups(output_type="df")

        expected_url = "https://api.tradingeconomics.com/eurostat/categories?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"category": "Poverty"}])
