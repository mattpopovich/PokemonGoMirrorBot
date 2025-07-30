"""
Test utils.py's get_trade_counts function.
"""

import tempfile
import os
from datetime import datetime, timedelta

from functions.utils import get_trade_counts



def create_temp_file_with_lines(lines) -> str:
    """Create a temporary file with the given lines, returns the file name."""
    tmp = tempfile.NamedTemporaryFile(mode='w+', delete=False)
    tmp.write('\n'.join(lines))
    tmp.flush()
    return tmp.name

def test_no_trades():
    filename = create_temp_file_with_lines([])
    since_midnight, total = get_trade_counts(filename)
    assert since_midnight == 0
    assert total == 0
    os.remove(filename)  # Clean up the temporary file after the test

def test_file_does_not_exist():
    filename = "this_file_should_not_exist.txt"
    # Verify the file doesn't exist
    if os.path.exists(filename):
        assert False, f"Test file {filename} should not exist before the test."
    result = get_trade_counts(filename)
    assert result == (0, 0)

def test_all_trades_today():
    now = datetime.now()
    lines = [
        (now - timedelta(minutes=i)).isoformat()
        for i in range(3)
    ]
    filename = create_temp_file_with_lines(lines)
    since_midnight, total = get_trade_counts(filename)
    assert since_midnight == 3
    assert total == 3
    os.remove(filename)  # Clean up the temporary file after the test

def test_mixed_trades():
    """Test with trades from today and previous days."""
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    lines = [
        (now - timedelta(minutes=1)).isoformat(),
        (now - timedelta(minutes=10)).isoformat(),
        (yesterday - timedelta(minutes=10)).isoformat(),
    ]
    filename = create_temp_file_with_lines(lines)
    since_midnight, total = get_trade_counts(filename)
    assert since_midnight == 2
    assert total == 3
    os.remove(filename)  # Clean up the temporary file after the test

def test_invalid_lines_are_skipped():
    now = datetime.now()
    lines = [
        now.isoformat(),
        "not-a-date",
        "",
        (now - timedelta(days=2)).isoformat(),
    ]
    filename = create_temp_file_with_lines(lines)
    since_midnight, total = get_trade_counts(filename)
    assert since_midnight == 1  # Only the first line is from today
    assert total == 2           # Two valid timestamps
    os.remove(filename)  # Clean up the temporary file after the test

def test_get_trade_counts_return_type():
    filename = "dummy_log.txt"
    assert not os.path.exists(filename), "Dummy log file should not exist before the test."
    result = get_trade_counts(filename)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(count, int) for count in result)
