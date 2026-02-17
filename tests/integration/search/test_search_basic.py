"""
Integration tests for Search module.

Tests the following API calls with guest:guest credentials:

Search:
- te.getSearch(term='gold')
- te.getSearch()
- te.getSearch(term='japan', category='markets')

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd


# Configure API access
te.login("guest:guest")


class TestSearch:
    """Test Search endpoints."""

    def test_search_by_term(self):
        """Test: te.getSearch(term='gold')"""
        result = te.getSearch(term="gold")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_search_all_categories(self):
        """Test: te.getSearch()"""
        result = te.getSearch()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_search_by_term_and_category(self):
        """Test: te.getSearch(term='japan', category='markets')"""
        result = te.getSearch(term="japan", category="markets")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestOutputFormats:
    """Test different output formats."""

    def test_search_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getSearch(term="gold", output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_search_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getSearch(term="gold", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_search_output_format_raw(self):
        """Test raw output format."""
        result = te.getSearch(term="gold", output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
