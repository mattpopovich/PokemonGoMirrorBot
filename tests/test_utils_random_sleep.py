"""
Test utils.py's random_sleep function.
"""

from functions.utils import random_sleep


def test_random_sleep_within_bounds():
    base = 2.0
    randomness = 0.5
    trials = 100

    for _ in range(trials):
        sleep_time = random_sleep(base, randomness, unittest=True)
        assert 1.5 <= sleep_time <= 2.5, f"Sleep time {sleep_time} out of bounds"


def test_random_sleep_no_randomness():
    base = 1.5
    randomness = 0.0
    sleep_time = random_sleep(base, randomness, unittest=True)
    assert sleep_time == base


def test_random_sleep_never_negative():
    base = 0.2
    randomness = 1.0
    trials = 100

    for _ in range(trials):
        sleep_time = random_sleep(base, randomness, unittest=True)
        assert sleep_time >= 0, "Sleep time should never be negative"


def test_random_sleep_return_type():
    result = random_sleep(1.0, 0.1, unittest=True)
    assert isinstance(result, float)
