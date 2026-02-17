import unittest
from unittest.mock import patch
from tradingeconomics.news import getArticleId
from tradingeconomics import glob


class TestGetArticleId(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"article": "ok"})
    def test_get_article_by_id(self, mock_request):
        # Get article by id
        result = getArticleId(id="20580")

        expected_url = "/articles/id//20580"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"article": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"article": "df"})
    def test_get_article_by_id_with_output_type(self, mock_request):
        # Get article by id with output type
        result = getArticleId(id="20580", output_type="df")

        expected_url = "/articles/id//20580"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"article": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest",
        return_value={"raw": "json", "article": "data"},
    )
    def test_get_article_by_id_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getArticleId(id="20580", output_type="raw")

        expected_url = "/articles/id//20580"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "article": "data"})
