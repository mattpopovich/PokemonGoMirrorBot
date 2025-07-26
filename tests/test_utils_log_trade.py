"""
Test utils.py's log_trade function.
"""

import tempfile
import os
from unittest import mock

from functions.utils import (
    log_trade
)

def test_log_trade_correct_time():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        log_file = tmp.name

    fixed_time = "2025-08-07T01:23:45"
    with mock.patch("functions.utils.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.isoformat.return_value = fixed_time
        log_trade(log_file)

    with open(log_file, 'r') as f:
        contents = f.read()

    assert contents == fixed_time + '\n', f"Contents read from file was {contents}, expected {fixed_time}"

    os.remove(log_file)

def test_log_trade_appends_lines():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        log_file = tmp.name

    with mock.patch("functions.utils.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.isoformat.return_value = "time1"
        log_trade(log_file)

        mock_datetime.datetime.now.return_value.isoformat.return_value = "time2"
        log_trade(log_file)

    with open(log_file, 'r') as f:
        lines = f.readlines()

    assert lines[0].strip() == "time1"
    assert lines[1].strip() == "time2"
    assert len(lines) == 2

    os.remove(log_file)

def test_log_trades_does_not_overwrite_existing_content():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
        tmp.write("existing line\n")
        log_file = tmp.name

    new_time = "2025-07-26T15:00:00"
    with mock.patch("functions.utils.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.isoformat.return_value = new_time
        log_trade(log_file)

    with open(log_file, 'r') as f:
        lines = f.readlines()

    assert lines[0].strip() == "existing line"
    assert lines[1].strip() == new_time
    assert len(lines) == 2

    os.remove(log_file)
