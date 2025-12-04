import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRSnaps
from tradingeconomics import glob


class TestGetFedRSnapsState(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"state": "ok"}
    )
    def test_snaps_state_single(self, mock_request):
        # Get snapshot by state
        result = getFedRSnaps(state="tennessee")

        expected_url = "/fred/snapshot/state/tennessee"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"state": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"state": "multiple"},
    )
    def test_snaps_state_multiple(self, mock_request):
        # Get snapshots by multiple states
        result = getFedRSnaps(state=["tennessee", "california"])

        expected_url = "/fred/snapshot/state/tennessee%2Fcalifornia"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"state": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"state": "page"}
    )
    def test_snaps_state_with_page(self, mock_request):
        # Get state snapshot with pagination
        result = getFedRSnaps(state="tennessee", page_number=3)

        expected_url = "/fred/snapshot/state/tennessee/3"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"state": "page"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"state": "df"}],
    )
    def test_snaps_state_output_type_df(self, mock_request):
        result = getFedRSnaps(state="nevada", output_type="df")

        expected_url = "/fred/snapshot/state/nevada"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"state": "df"}])
