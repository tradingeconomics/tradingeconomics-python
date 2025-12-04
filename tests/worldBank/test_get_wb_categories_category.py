import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import getWBCategories
from tradingeconomics import glob


class TestGetWBCategoriesCategory(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"categories": "single_category"},
    )
    def test_get_wb_categories_single_category(self, mock_request):
        # Get single category
        result = getWBCategories(category="education")

        expected_url = (
            "https://api.tradingeconomics.com/worldBank/category/education?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"categories": "single_category"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"categories": "category_with_page"},
    )
    def test_get_wb_categories_with_page_number(self, mock_request):
        # Get category with page number
        result = getWBCategories(category="education", page_number=3)

        expected_url = (
            "https://api.tradingeconomics.com/worldBank/category/education/3?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"categories": "category_with_page"})


if __name__ == "__main__":
    unittest.main()
