import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRSnaps
from tradingeconomics import glob


class TestGetFedRSnapsNoParameters(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_snaps_no_parameters(self):
        # When no parameters are provided, should return error message
        result = getFedRSnaps()

        self.assertEqual(result, "A parameter must be provided!")
