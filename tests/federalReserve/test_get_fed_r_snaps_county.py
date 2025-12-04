import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRSnaps
from tradingeconomics import glob


class TestGetFedRSnapsCounty(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"county": "ok"}
    )
    def test_snaps_county_single(self, mock_request):
        # Get snapshot by county
        result = getFedRSnaps(county="pike county, ar")

        expected_url = "/fred/snapshot/county/pike%20county%2C%20ar"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"county": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"county": "multiple"},
    )
    def test_snaps_county_multiple(self, mock_request):
        # Get snapshots by multiple counties
        result = getFedRSnaps(county=["pike county, ar", "dallas county, tx"])

        expected_url = (
            "/fred/snapshot/county/pike%20county%2C%20ar%2Fdallas%20county%2C%20tx"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"county": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"county": "df"}],
    )
    def test_snaps_county_output_type_df(self, mock_request):
        result = getFedRSnaps(county="pike county, ar", output_type="df")

        expected_url = "/fred/snapshot/county/pike%20county%2C%20ar"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"county": "df"}])
