import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRSnaps
from tradingeconomics import glob


class TestGetFedRSnapsUrl(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.federalReserve.fn.dataRequest", return_value={"url": "ok"})
    def test_snaps_url(self, mock_request):
        # Get snapshot by URL
        test_url = "united-states/white-to-non-white-racial-dissimilarity-index.html"
        result = getFedRSnaps(url=test_url)

        expected_url = f"https://api.tradingeconomics.com/fred/snapshot/url/?url=united-states/white-to-non-white-racial-dissimilarity-index.html"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"url": "ok"})
