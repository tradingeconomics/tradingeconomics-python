import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatData
from tradingeconomics import glob


class TestGetEurostatDataCategoryGroup(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest",
        return_value={"category_group": "ok"},
    )
    def test_category_group_parameter_single(self, mock_request):
        # Provide a single category_group and ensure URL is built correctly
        result = getEurostatData(category_group="Poverty")

        expected_url = (
            "https://api.tradingeconomics.com/eurostat?category_group=Poverty&c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"category_group": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest",
        return_value={"category_group": "multiple"},
    )
    def test_category_group_parameter_multiple(self, mock_request):
        # Provide multiple category_groups and ensure URL is built correctly
        result = getEurostatData(category_group=["Poverty", "Education"])

        expected_url = "https://api.tradingeconomics.com/eurostat?category_group=Poverty%2CEducation&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"category_group": "multiple"})
