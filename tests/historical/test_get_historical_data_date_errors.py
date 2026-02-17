import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalData
from tradingeconomics import glob
from tradingeconomics.historical import DateError


class TestGetHistoricalDataDateErrors(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_historical_end_date_without_init_date(self):
        # Should raise DateError when endDate provided without initDate
        with self.assertRaises(DateError) as context:
            getHistoricalData(
                country="United States", indicator="GDP", endDate="2020-12-31"
            )

        self.assertIn("initDate value is missing", str(context.exception))
