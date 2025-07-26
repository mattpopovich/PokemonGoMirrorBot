"""
Test utils.py
"""

import pytest
import tempfile
from unittest import mock

from functions.utils import (
    randomize_location,
    random_sleep,
    log_trade,
    get_trade_counts
)

def test_log_trade_correct_time():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        log_file = tmp.name

    fixed_time = "2025-08-07T01:23:45"
    with mock.patch("logger_module.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.isoformat.return_value = fixed_time
        log_trade(log_file)

    with open(log_file, 'r') as f:
        contents = f.read()

    assert contents == fixed_time, f"Contents read from file was {contents}, expected {fixed_time}"

    os.remove(log_file)

def test_log_trade_appends_lines():
    # TODO: Ensure the function creates multiple lines in the file
    return 0




def test_get_trade_counts_no_file():
    # TODO: Ensure the function returns 0 if no file exists
    return 0

