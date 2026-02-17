import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatData
from tradingeconomics import glob


class TestGetEurostatDataNoParameters(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_no_parameters_raises_error(self):
        # When no parameters are provided, should raise ValueError
        with self.assertRaises(ValueError) as context:
            getEurostatData()

        self.assertIn(
            "At least one of the parameters, needs to be supplied.",
            str(context.exception),
        )
