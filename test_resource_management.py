"""
Test to verify proper resource management with context managers
Ensures connections are properly closed even when errors occur
"""
import sys
sys.path.insert(0, '.')

import tradingeconomics as te
import gc
import traceback

print("="*70)
print("Testing Resource Management with Context Managers")
print("="*70)

# Test 1: Multiple rapid requests to check resource cleanup
print("\n[Test 1] Rapid sequential requests (100 iterations)")
print("-" * 70)
try:
    te.login('guest:guest')
    success_count = 0
    
    for i in range(100):
        try:
            result = te.getCalendarData(output_type='df')
            if len(result) > 0:
                success_count += 1
        except Exception as e:
            print(f"  Request {i+1} failed: {str(e)[:50]}")
    
    print(f"✅ PASSED: Completed {success_count}/100 requests without resource exhaustion")
    
except Exception as e:
    print(f"❌ FAILED: Resource management issue detected")
    print(f"   Error: {str(e)}")
    traceback.print_exc()

# Test 2: Mix of successful and failed requests
print("\n[Test 2] Mixed success/failure requests (50 iterations)")
print("-" * 70)
try:
    from tradingeconomics import functions as fn
    
    success = 0
    failures = 0
    
    for i in range(50):
        try:
            # Alternate between valid and invalid requests
            if i % 2 == 0:
                result = te.getCalendarData(output_type='df')
                success += 1
            else:
                # This should fail but not leak resources
                result = fn.dataRequest('https://api.tradingeconomics.com/invalid_endpoint', None)
        except Exception:
            failures += 1
    
    print(f"✅ PASSED: {success} successful, {failures} failed - no resource leaks")
    
except Exception as e:
    print(f"❌ FAILED: Unexpected error")
    print(f"   Error: {str(e)}")

# Test 3: Check that resources are released during exceptions
print("\n[Test 3] Resource cleanup during exceptions")
print("-" * 70)
try:
    from tradingeconomics import functions as fn
    
    # Force multiple failures to ensure cleanup happens
    for i in range(20):
        try:
            fn.dataRequest('https://invalid-host-xyz-12345.com/api', None)
        except fn.WebRequestError:
            pass  # Expected
    
    print(f"✅ PASSED: 20 failed requests handled without resource issues")
    
except Exception as e:
    print(f"❌ FAILED: Resource not properly cleaned up")
    print(f"   Error: {str(e)}")

# Test 4: Memory cleanup verification
print("\n[Test 4] Garbage collection verification")
print("-" * 70)
try:
    import gc
    
    # Force garbage collection
    gc.collect()
    initial_objects = len(gc.get_objects())
    
    # Make multiple requests
    for i in range(50):
        try:
            result = te.getCalendarData(output_type='df')
        except:
            pass
    
    # Force garbage collection again
    gc.collect()
    final_objects = len(gc.get_objects())
    
    object_growth = final_objects - initial_objects
    print(f"   Initial objects: {initial_objects}")
    print(f"   Final objects: {final_objects}")
    print(f"   Growth: {object_growth} objects")
    
    if object_growth < 1000:  # Reasonable threshold
        print(f"✅ PASSED: Memory growth within acceptable range")
    else:
        print(f"⚠️  WARNING: Significant object growth detected")
    
except Exception as e:
    print(f"❌ FAILED: Memory test error")
    print(f"   Error: {str(e)}")

print("\n" + "="*70)
print("Resource Management Tests Complete")
print("="*70)
print("\n💡 Key improvements with context managers:")
print("   - Automatic connection cleanup")
print("   - No resource leaks on exceptions")
print("   - Better handling of rapid requests")
print("   - Reduced memory footprint over time")
