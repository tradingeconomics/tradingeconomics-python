"""
Test script to verify error handling in dataRequest function
Tests various error scenarios to ensure robust exception handling
"""

import sys

sys.path.insert(0, ".")

import tradingeconomics as te

print("=" * 70)
print("Testing Error Handling in dataRequest()")
print("=" * 70)

# Test 1: Invalid API endpoint (404 error)
print("\n[Test 1] Invalid API endpoint (should trigger HTTP error)")
print("-" * 70)
try:
    te.login("guest:guest")
    result = te.getCalendarData()
    # Now try an invalid direct call to see error handling
    from tradingeconomics import functions as fn

    result = fn.dataRequest(
        "https://api.tradingeconomics.com/invalid_endpoint_xyz", None
    )
    print("❌ FAILED: Should have raised an exception")
except Exception as e:
    print(f"✅ PASSED: Caught exception: {type(e).__name__}")
    print(f"   Message: {str(e)[:100]}")

# Test 2: Malformed URL
print("\n[Test 2] Malformed URL")
print("-" * 70)
try:
    from tradingeconomics import functions as fn

    result = fn.dataRequest("not_a_valid_url", None)
    print("❌ FAILED: Should have raised an exception")
except Exception as e:
    print(f"✅ PASSED: Caught exception: {type(e).__name__}")
    print(f"   Message: {str(e)[:100]}")

# Test 3: Invalid output_type
print("\n[Test 3] Invalid output_type parameter")
print("-" * 70)
try:
    from tradingeconomics import functions as fn

    result = fn.dataRequest("https://api.tradingeconomics.com/calendar", "invalid_type")
    print("❌ FAILED: Should have raised ParametersError")
except Exception as e:
    print(f"✅ PASSED: Caught exception: {type(e).__name__}")
    print(f"   Message: {str(e)}")

# Test 4: Valid request with no data (empty result)
print("\n[Test 4] Valid request returning empty data")
print("-" * 70)
try:
    from tradingeconomics import functions as fn

    # Try to get data with impossible filter that returns empty list
    result = fn.dataRequest(
        "https://api.tradingeconomics.com/calendar/country/NONEXISTENTCOUNTRY123", None
    )
    print("❌ FAILED: Should have raised ParametersError for empty data")
except Exception as e:
    print(f"✅ PASSED: Caught exception: {type(e).__name__}")
    print(f"   Message: {str(e)}")

# Test 5: Successful request
print("\n[Test 5] Valid successful request")
print("-" * 70)
try:
    te.login("guest:guest")
    result = te.getCalendarData(output_type="df")
    print(f"✅ PASSED: Request successful, returned {len(result)} rows")
    print(f"   Columns: {list(result.columns[:5])}...")
except Exception as e:
    print(f"❌ FAILED: Should have succeeded")
    print(f"   Exception: {type(e).__name__}: {str(e)}")

# Test 6: Network timeout simulation (if possible)
print("\n[Test 6] Testing with invalid host")
print("-" * 70)
try:
    from tradingeconomics import functions as fn

    result = fn.dataRequest(
        "https://invalid-host-that-does-not-exist-12345.com/api", None
    )
    print("❌ FAILED: Should have raised an exception")
except Exception as e:
    print(f"✅ PASSED: Caught exception: {type(e).__name__}")
    print(f"   Message: {str(e)[:100]}")

print("\n" + "=" * 70)
print("Error Handling Tests Complete")
print("=" * 70)
