import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRSnaps
from tradingeconomics import glob


class TestGetFedRSnapsCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"country": "ok"}
    )
    def test_snaps_country_single(self, mock_request):
        # Get snapshot by country
        result = getFedRSnaps(country="united states")

        expected_url = "https://api.tradingeconomics.com/fred/snapshot/country/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"country": "multiple"},
    )
    def test_snaps_country_multiple(self, mock_request):
        # Get snapshots by multiple countries (though only US is supported)
        result = getFedRSnaps(country=["united states", "usa"])

        expected_url = "https://api.tradingeconomics.com/fred/snapshot/country/united%20states%2Fusa"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "multiple"})
