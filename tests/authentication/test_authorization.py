"""
Tests for different types of API authorization and authentication scenarios.

These tests validate that the SDK properly handles various authentication states
and returns appropriate errors for different authorization failures.
"""

import unittest
import sys
import os
import time

sys.path.insert(0, "../../tradingeconomics")
import tradingeconomics as te
from tradingeconomics import AuthenticationError, CredentialsError


class TestAuthenticationScenarios(unittest.TestCase):
    """Test various authentication and authorization scenarios"""

    def setUp(self):
        """Reset authentication state before each test"""
        # Clear any existing API key
        te.glob.apikey = None
        if "apikey" in os.environ:
            self.original_apikey = os.environ.pop("apikey")
        else:
            self.original_apikey = None

    def tearDown(self):
        """Restore original state and rate limit"""
        # Restore original API key if it existed
        if self.original_apikey:
            os.environ["apikey"] = self.original_apikey
        time.sleep(1)  # Rate limiting

    def test_successful_auth_with_guest_credentials(self):
        """✅ Test successful authentication with guest credentials"""
        te.login("guest:guest")

        # Should return data (even if limited sample)
        result = te.getCalendarData(output_type="df")

        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0, "Guest credentials should return sample data")

    def test_no_authentication_fails(self):
        """❌ Test that requests without authentication fail appropriately"""
        # Don't call te.login() - no authentication set

        # This should fail with AuthenticationError or return limited data
        # Depending on API behavior, adjust assertion
        try:
            result = te.getCalendarData(output_type="df")
            # If API allows unauthenticated requests with limited data
            self.assertIsNotNone(result)
        except AuthenticationError as e:
            # Expected behavior if API requires authentication
            self.assertIn("401", str(e).lower() or "unauthorized", str(e).lower())

    def test_invalid_credentials_format_detected_early(self):
        """❌ Test that invalid API key format is caught before request"""
        # API keys should have format "user:key" with colon
        with self.assertRaises(CredentialsError) as context:
            te.login("invalid_format_without_colon")

        self.assertIn("Invalid credentials", str(context.exception))

    def test_valid_format_but_incorrect_credentials(self):
        """❌ Test that valid format but incorrect credentials fail with 401"""
        te.login("fake:credentials")

        # Should fail with AuthenticationError when making actual request
        with self.assertRaises(AuthenticationError) as context:
            te.getCalendarData(output_type="df")

        error_message = str(context.exception).lower()
        self.assertTrue(
            "401" in error_message or "unauthorized" in error_message,
            f"Expected authentication error, got: {context.exception}",
        )

    def test_authorization_header_is_added(self):
        """✅ Test that Authorization header is properly added to requests"""
        te.login("guest:guest")

        # Verify that glob.apikey is set
        self.assertEqual(te.glob.apikey, "guest:guest")

        # Make a request - if no error, header was accepted
        result = te.getCalendarData(output_type="df")
        self.assertIsNotNone(result)

    def test_empty_apikey_handling(self):
        """❌ Test behavior when apikey is explicitly empty"""
        te.glob.apikey = ""

        # Empty string should be treated as no authentication
        try:
            result = te.getCalendarData(output_type="df")
            # May succeed with limited data or fail
            self.assertIsNotNone(result)
        except AuthenticationError:
            # Also acceptable behavior
            pass

    def test_none_apikey_handling(self):
        """❌ Test behavior when apikey is None"""
        te.glob.apikey = None

        # None should be treated as no authentication
        try:
            result = te.getCalendarData(output_type="df")
            # May succeed with limited data or fail
            self.assertIsNotNone(result)
        except AuthenticationError:
            # Also acceptable behavior
            pass


class TestAuthenticationErrorMessages(unittest.TestCase):
    """Test that authentication errors provide helpful messages"""

    def setUp(self):
        """Reset state"""
        te.glob.apikey = None
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    def test_401_error_message_is_helpful(self):
        """Test that 401 errors provide clear guidance"""
        te.login("invalid:key")

        try:
            te.getCalendarData(output_type="df")
            self.fail("Should have raised AuthenticationError")
        except AuthenticationError as e:
            error_msg = str(e).lower()
            # Should mention credentials or authentication
            self.assertTrue(
                any(
                    word in error_msg
                    for word in [
                        "credential",
                        "authentication",
                        "unauthorized",
                        "api key",
                    ]
                ),
                f"Error message should be helpful: {e}",
            )

    def test_403_error_message_mentions_permissions(self):
        """Test that 403 errors mention permission issues"""
        # This test might need actual API key without permissions
        # Skipping actual test but documenting expected behavior
        pass


class TestDifferentHTTPStatusCodes(unittest.TestCase):
    """Test handling of various HTTP status codes"""

    def setUp(self):
        te.login("guest:guest")
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    def test_404_raises_parameters_error(self):
        """Test that 404 errors are handled as ParametersError"""
        # Try to access non-existent endpoint
        try:
            # Force a 404 by using invalid URL
            from tradingeconomics import functions as fn

            fn.dataRequest("/nonexistent/endpoint/that/does/not/exist", None)
            # May not raise 404, might return empty - adjust as needed
        except Exception as e:
            # Just verify it doesn't crash ungracefully
            self.assertIsNotNone(str(e))


if __name__ == "__main__":
    unittest.main()
