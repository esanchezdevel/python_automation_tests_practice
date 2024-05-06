# To install pytest we run in our virtual environment:
# pip install -U pytest

import pytest

def add_two_numbers(a, b):
    return a + b

# PyTest only execute tests methods that starts by test, and files that starts by test
@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, 'The sum of 1 and 2 should be 3'

@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, 'The sum of 100 and 300 should be 400'

test_small_numbers
test_large_numbers