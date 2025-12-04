import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRSnaps
from tradingeconomics import glob


class TestGetFedRSnapsSymbol(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"symbol": "ok"}
    )
    def test_snaps_symbol_single(self, mock_request):
        # Get snapshot by single symbol
        result = getFedRSnaps(symbol="ALLMARGATTN")

        expected_url = "/fred/snapshot/symbol/ALLMARGATTN"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"symbol": "multiple"},
    )
    def test_snaps_symbol_multiple(self, mock_request):
        # Get snapshots by multiple symbols
        result = getFedRSnaps(symbol=["SYMBOL1", "SYMBOL2"])

        expected_url = "/fred/snapshot/symbol/SYMBOL1%2FSYMBOL2"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"symbol": "page"},
    )
    def test_snaps_symbol_with_page(self, mock_request):
        # Get snapshot with pagination
        result = getFedRSnaps(symbol="ALLMARGATTN", page_number=2)

        expected_url = "/fred/snapshot/symbol/ALLMARGATTN/2"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "page"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"symbol": "df"}],
    )
    def test_snaps_symbol_output_type_df(self, mock_request):
        result = getFedRSnaps(symbol="ALLMARGATTN", output_type="df")

        expected_url = "/fred/snapshot/symbol/ALLMARGATTN"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"symbol": "df"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"symbol": "raw"}],
    )
    def test_snaps_symbol_output_type_raw(self, mock_request):
        result = getFedRSnaps(symbol="SYMBOL1", output_type="raw")

        expected_url = "/fred/snapshot/symbol/SYMBOL1"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"symbol": "raw"}])
