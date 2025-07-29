"""
Test utils.py's randomize_location function.
"""

from functions.utils import randomize_location

def test_randomize_location_within_bounds():
    location = [100, 200]
    pixel_randomness = 10
    trials = 100

    for _ in range(trials):
        new_location = randomize_location(location, pixel_randomness)
        assert len(new_location) == 2
        dx = new_location[0] - location[0]
        dy = new_location[1] - location[1]
        assert -pixel_randomness <= dx <= pixel_randomness
        assert -pixel_randomness <= dy <= pixel_randomness

def test_randomize_location_changes_output():
    location = [50, 50]
    pixel_randomness = 5
    trials = 100

    different_found = False
    for _ in range(trials):
        new_location = randomize_location(location, pixel_randomness)
        if new_location != location:
            different_found = True
            break
    assert different_found, "Expected at least one output to differ from the input"

def test_zero_randomness_returns_same_location():
    location = [10, 20]
    pixel_randomness = 0
    new_location = randomize_location(location, pixel_randomness)
    assert new_location == location

def test_randomize_location_return_type():
    result = randomize_location([0, 0], 10)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(coord, int) for coord in result)
