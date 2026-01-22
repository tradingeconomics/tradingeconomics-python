# Authentication Testing

## Overview

This directory contains comprehensive tests for API authentication and authorization scenarios in the Trading Economics Python SDK.

## What Was Changed

### 1. **New Exception: `AuthenticationError`**

- Added to `functions.py` to specifically handle authentication failures (401/403 errors)
- Provides clear, actionable error messages to users
- Exported in `tradingeconomics/__init__.py` for public use

### 2. **Enhanced `dataRequest()` Function**

- **Proper HTTP Error Handling**: Now catches and handles specific HTTP status codes

  - `401 Unauthorized` → `AuthenticationError` with guidance about invalid credentials
  - `403 Forbidden` → `AuthenticationError` mentioning permission issues
  - `404 Not Found` → `ParametersError` for invalid endpoints
  - `4xx Client Errors` → `ParametersError` for bad requests
  - `5xx Server Errors` → `WebRequestError` for API issues

- **Network Error Handling**: Separate handling for DNS, connection, and timeout errors

- **JSON Error Handling**: Catches malformed JSON responses

- **Removed Silent Failures**: No longer returns empty string `""` for non-200 codes

### 3. **Error Messages Include Details**

- All errors now include the HTTP status code
- API error messages are extracted and included when available
- Helpful guidance provided for common issues

## Test Coverage

### `test_authorization.py`

#### Authentication Scenarios Tested:

- ✅ **Successful authentication with guest credentials** - Validates that `'guest:guest'` works
- ❌ **No authentication** - Validates behavior when no login is performed
- ❌ **Invalid credentials format** - Catches malformed API keys (missing `:`) early
- ❌ **Valid format but incorrect credentials** - Tests 401 handling for wrong credentials
- ✅ **Authorization header** - Verifies header is properly added to requests
- ❌ **Empty/None API key** - Tests edge cases with empty authentication

#### Error Message Quality Tests:

- Validates that 401 errors provide helpful guidance about credentials
- Validates that 403 errors mention permission issues
- Ensures error messages are actionable for developers

#### HTTP Status Code Tests:

- Tests handling of various HTTP codes (404, 4xx, 5xx)
- Validates appropriate exception types for different errors

## Running Tests

```bash
# Run all authentication tests
python -m unittest tests.authentication.test_authorization -v

# Run specific test class
python -m unittest tests.authentication.test_authorization.TestAuthenticationScenarios -v

# Run specific test
python -m unittest tests.authentication.test_authorization.TestAuthenticationScenarios.test_successful_auth_with_guest_credentials -v
```

## Expected Behaviors

### ✅ Success Cases:

| Scenario      | API Key           | Expected Result               |
| ------------- | ----------------- | ----------------------------- |
| Guest access  | `'guest:guest'`   | Returns sample data (limited) |
| Valid API key | Valid credentials | Returns full data             |

### ❌ Failure Cases:

| Scenario          | API Key           | Expected Exception    | HTTP Code |
| ----------------- | ----------------- | --------------------- | --------- |
| No login          | None              | `AuthenticationError` | 401       |
| Invalid format    | `'no_colon'`      | `CredentialsError`    | -         |
| Wrong credentials | `'fake:key'`      | `AuthenticationError` | 401       |
| No permission     | Valid but limited | `AuthenticationError` | 403       |
| Bad endpoint      | Any               | `ParametersError`     | 404       |

## Migration Notes

### For Existing Code:

The changes are **backward compatible**. Existing code will continue to work, but now with better error messages.

### New Exception Available:

You can now catch authentication errors specifically:

```python
import tradingeconomics as te
from tradingeconomics import AuthenticationError

try:
    te.login('my:apikey')
    data = te.getCalendarData(output_type='df')
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
    # Handle authentication issues
except te.ParametersError as e:
    print(f"Invalid parameters: {e}")
    # Handle parameter issues
```

### Error Messages Are More Helpful:

**Before:**

```
WebRequestError: Request failed: HTTP Error 401: Unauthorized
```

**After:**

```
AuthenticationError: Authentication failed (401 Unauthorized).
Invalid API key or missing credentials.
Please check your login credentials.
Details: [API-specific error message]
```

## Implementation Details

### Key Changes in `functions.py`:

1. **Import HTTP error classes** based on Python version:

   ```python
   if PY3:
       from urllib.error import HTTPError, URLError
   else:
       from urllib2 import HTTPError, URLError
   ```

2. **Structured exception handling**:

   ```python
   try:
       # Make request
   except HTTPError as e:
       # Handle specific HTTP errors (401, 403, 404, etc.)
   except URLError as e:
       # Handle network errors
   except json.JSONDecodeError as e:
       # Handle JSON parsing errors
   except Exception as e:
       # Catch-all for unexpected errors
   ```

3. **Error message extraction** from API responses:
   - Attempts to parse JSON error messages
   - Falls back to raw response body
   - Includes HTTP status code and reason

## Future Enhancements

Potential improvements for the future:

1. **Retry logic** for transient 5xx errors
2. **Rate limiting detection** (429 status code handling)
3. **Detailed permission errors** based on specific 403 responses
4. **Authentication token refresh** for expired credentials
5. **Mock API responses** for faster unit testing

## Related Files

- [`tradingeconomics/functions.py`](../../tradingeconomics/functions.py) - Core implementation
- [`tradingeconomics/__init__.py`](../../tradingeconomics/__init__.py) - Exception exports
- [`tradingeconomics/glob.py`](../../tradingeconomics/glob.py) - Authentication state
