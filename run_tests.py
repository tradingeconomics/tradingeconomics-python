#!/usr/bin/env python
"""
Script to run all unit tests by subdirectory to avoid pandas circular import issues.
Automatically discovers test subdirectories and runs them sequentially.
"""
import os
import sys
import subprocess
from pathlib import Path


def get_test_subdirectories(tests_dir="tests"):
    """Get all subdirectories in the tests folder that contain test files."""
    tests_path = Path(tests_dir)
    if not tests_path.exists():
        print(f"Error: {tests_dir} directory not found")
        sys.exit(1)

    subdirs = []
    for item in sorted(tests_path.iterdir()):
        if (
            item.is_dir()
            and not item.name.startswith("_")
            and not item.name == "__pycache__"
            and item.name != "integration"
        ):
            # Check if directory contains test files
            has_tests = any(
                f.name.startswith("test_") and f.suffix == ".py"
                for f in item.rglob("*.py")
            )
            if has_tests:
                subdirs.append(item.name)

    return subdirs


def run_tests_for_subdir(subdir, verbose=True):
    """Run tests for a specific subdirectory."""
    test_path = f"tests/{subdir}"
    cmd = ["python", "-m", "unittest", "discover", "-s", test_path]
    if verbose:
        cmd.append("-v")

    print(f"\n{'='*60}")
    print(f"Running tests in: {test_path}")
    print(f"{'='*60}")

    result = subprocess.run(cmd, capture_output=False)
    return result.returncode


def main():
    """Main function to run all tests."""
    verbose = "-v" in sys.argv or "--verbose" in sys.argv

    print("Discovering test subdirectories...")
    subdirs = get_test_subdirectories()

    if not subdirs:
        print("No test subdirectories found!")
        sys.exit(1)

    print(f"Found {len(subdirs)} test subdirectories: {', '.join(subdirs)}\n")

    failed_subdirs = []
    total_tests = 0

    for subdir in subdirs:
        returncode = run_tests_for_subdir(subdir, verbose)
        if returncode != 0:
            failed_subdirs.append(subdir)

    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total subdirectories tested: {len(subdirs)}")
    print(f"Passed: {len(subdirs) - len(failed_subdirs)}")
    print(f"Failed: {len(failed_subdirs)}")

    if failed_subdirs:
        print(f"\nFailed subdirectories:")
        for subdir in failed_subdirs:
            print(f"  - {subdir}")
        sys.exit(1)
    else:
        print("\n✅ All tests passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
