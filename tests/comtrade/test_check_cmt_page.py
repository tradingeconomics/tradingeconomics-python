# FILE: tests/comtrade/test_checkCmtPage.py
# Unit tests for checkCmtPage()
# - Tests URL concatenation behavior
# - Ensures page numbers append correctly
# - Ensures None does not modify the URL

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import checkCmtPage


class TestCheckCmtPage(unittest.TestCase):
    def test_page_number_appended(self):
        """
        When page_number is provided, it must be appended as '/<page>'
        to the existing URL.
        """
        base = "/comtrade/country/china"
        result = checkCmtPage(base, 3)
        expected = "/comtrade/country/china/3"
        self.assertEqual(result, expected)

    def test_page_number_none(self):
        """
        If page_number is None, the function must return the base URL unchanged.
        """
        base = "/comtrade/country/china"
        result = checkCmtPage(base, None)
        self.assertEqual(result, base)


if __name__ == "__main__":
    unittest.main()
