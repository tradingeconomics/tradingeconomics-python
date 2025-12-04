import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsDataByCategory
from tradingeconomics import glob


class TestGetFinancialsDataByCategoryNoParameter(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_financials_by_category_no_parameter(self):
        # When no category is provided, should return error message
        result = getFinancialsDataByCategory()

        self.assertEqual(result, "No category supplied")
