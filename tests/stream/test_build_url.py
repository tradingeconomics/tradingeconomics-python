import unittest
from unittest.mock import patch, MagicMock
from tradingeconomics import glob
from tradingeconomics import stream


class TestBuildUrl(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY:SECRET")
    @patch.object(glob, "STREAM_URL", "wss://stream.tradingeconomics.com")
    def test_build_url_with_credentials(self):
        # Test URL building with API key
        expected_url = "wss://stream.tradingeconomics.com?client=TESTKEY:SECRET&app=python&token=20171116"

        result = stream.build_url()

        self.assertEqual(result, expected_url)

    @patch.object(glob, "apikey", "")
    @patch.object(glob, "STREAM_URL", "wss://stream.tradingeconomics.com")
    def test_build_url_with_empty_credentials(self):
        # Test URL building with empty API key
        expected_url = (
            "wss://stream.tradingeconomics.com?client=&app=python&token=20171116"
        )

        result = stream.build_url()

        self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
