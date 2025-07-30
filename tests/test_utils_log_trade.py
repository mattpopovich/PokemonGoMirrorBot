"""
Test utils.py's log_trade function.
"""

import tempfile
import os
from unittest import mock

from functions.utils import log_trade


def test_log_trade_correct_time():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        log_file_name = tmp.name

    fixed_time = "2025-08-07T01:23:45"
    with mock.patch("functions.utils.datetime") as mock_datetime:
        mock_datetime.now.return_value.isoformat.return_value = fixed_time
        log_trade(log_file_name)

    with open(log_file_name, 'r') as f:
        contents = f.read()

    assert contents == fixed_time + '\n', f"Contents read from file was {contents}, expected {fixed_time}"

    os.remove(log_file_name)

def test_log_trade_appends_lines():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        log_file_name = tmp.name

    t1 = "time1"
    t2 = "time2"
    with mock.patch("functions.utils.datetime") as mock_datetime:
        mock_datetime.now.return_value.isoformat.return_value = t1
        log_trade(log_file_name)

        mock_datetime.now.return_value.isoformat.return_value = t2
        log_trade(log_file_name)

    with open(log_file_name, 'r') as f:
        lines = f.readlines()

    assert lines[0].strip() == t1
    assert lines[1].strip() == t2
    assert len(lines) == 2

    os.remove(log_file_name)

def test_log_trades_does_not_overwrite_existing_content():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
        tmp.write("existing line\n")
        log_file_name = tmp.name

    new_time = "2025-07-26T15:00:00"
    with mock.patch("functions.utils.datetime") as mock_datetime:
        mock_datetime.now.return_value.isoformat.return_value = new_time
        log_trade(log_file_name)

    with open(log_file_name, 'r') as f:
        lines = f.readlines()

    assert lines[0].strip() == "existing line"
    assert lines[1].strip() == new_time
    assert len(lines) == 2

    os.remove(log_file_name)

def test_log_trade_return_type():
    filename = "dummy_log.txt"
    result = log_trade(filename)
    assert result is None
    os.remove(filename)
