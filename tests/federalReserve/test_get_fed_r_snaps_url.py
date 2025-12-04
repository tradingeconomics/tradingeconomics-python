import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRSnaps
from tradingeconomics import glob


class TestGetFedRSnapsUrl(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.federalReserve.fn.dataRequest", return_value={"url": "ok"})
    def test_snaps_url(self, mock_request):
        # Get snapshot by URL
        test_url = "united states/white-to-non-white-racial-dissimilarity-index-for-benton-county-ar-fed-data.html"
        result = getFedRSnaps(url=test_url)

        expected_url = f"/fred/snapshot/url/?url={test_url.replace(' ', '%20')}"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"url": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value=[{"url": "df"}]
    )
    def test_snaps_url_output_type_df(self, mock_request):
        test_url = "united states/indicator.html"
        result = getFedRSnaps(url=test_url, output_type="df")

        expected_url = f"/fred/snapshot/url/?url={test_url.replace(' ', '%20')}"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"url": "df"}])
