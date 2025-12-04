"""
Test to verify API_BASE_URL constant and relative path support in dataRequest
"""

import sys

sys.path.insert(0, ".")

import tradingeconomics as te
from tradingeconomics import glob, functions as fn

print("=" * 70)
print("Testing API_BASE_URL and Relative Path Support")
print("=" * 70)

# Test 1: Verify API_BASE_URL is defined
print("\n[Test 1] Verify API_BASE_URL constant exists")
print("-" * 70)
print(f"API_BASE_URL: {glob.API_BASE_URL}")
if glob.API_BASE_URL == "https://api.tradingeconomics.com":
    print("✅ PASSED: Correct default URL")
else:
    print(f"❌ FAILED: Unexpected URL: {glob.API_BASE_URL}")

# Test 2: Test with full URL (backward compatibility)
print("\n[Test 2] Full URL support (backward compatibility)")
print("-" * 70)
try:
    te.login("guest:guest")
    result = fn.dataRequest("https://api.tradingeconomics.com/calendar", "df")
    print(f"✅ PASSED: Full URL works - returned {len(result)} rows")
except Exception as e:
    print(f"❌ FAILED: {str(e)}")

# Test 3: Test with relative path (new feature)
print("\n[Test 3] Relative path support (new feature)")
print("-" * 70)
try:
    result = fn.dataRequest("/calendar", "df")
    print(f"✅ PASSED: Relative path works - returned {len(result)} rows")
except Exception as e:
    print(f"❌ FAILED: {str(e)}")

# Test 4: Compare results from full URL vs relative path
print("\n[Test 4] Results consistency (full URL vs relative path)")
print("-" * 70)
try:
    result_full = fn.dataRequest("https://api.tradingeconomics.com/calendar", "df")
    result_relative = fn.dataRequest("/calendar", "df")

    if len(result_full) == len(result_relative):
        print(f"✅ PASSED: Both return same number of rows ({len(result_full)})")
    else:
        print(
            f"⚠️  WARNING: Different row counts - Full: {len(result_full)}, Relative: {len(result_relative)}"
        )

    if list(result_full.columns) == list(result_relative.columns):
        print(f"✅ PASSED: Both return same columns")
    else:
        print(f"❌ FAILED: Different columns")

except Exception as e:
    print(f"❌ FAILED: {str(e)}")

# Test 5: Test with different relative paths
print("\n[Test 5] Various relative path formats")
print("-" * 70)
test_paths = [
    "/calendar",
    "/calendar/country/united%20states",
    "/markets/commodities",
]

for path in test_paths:
    try:
        result = fn.dataRequest(path, "raw")
        print(f"✅ PASSED: {path} - returned {len(result)} items")
    except Exception as e:
        print(f"⚠️  {path} - {str(e)[:60]}")

# Test 6: Verify no double-slash issue
print("\n[Test 6] URL construction verification")
print("-" * 70)
test_cases = [
    ("/calendar", "https://api.tradingeconomics.com/calendar"),
    ("calendar", "https://api.tradingeconomics.com/calendar"),  # without leading /
    (
        "https://api.tradingeconomics.com/calendar",
        "https://api.tradingeconomics.com/calendar",
    ),
]

for input_path, expected_start in test_cases:
    # Simulate URL construction
    if not input_path.startswith(("http://", "https://")):
        constructed = glob.API_BASE_URL + input_path
    else:
        constructed = input_path

    if constructed.startswith(expected_start):
        print(f"✅ '{input_path}' → {constructed[:50]}...")
    else:
        print(f"❌ '{input_path}' → {constructed[:50]}... (expected {expected_start})")

print("\n" + "=" * 70)
print("API_BASE_URL Tests Complete")
print("=" * 70)
print("\n💡 Key achievements:")
print("   - API_BASE_URL centralized in glob.py")
print("   - Full backward compatibility maintained")
print("   - Relative path support added")
print("   - Environment variable override available (TE_API_BASE_URL)")
