import pytest
from is_prime import is_prime

@pytest.mark.parametrize("n", [-10, -1, 0, 1])
def test_non_positive(n):
    assert is_prime(n) is False

@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 17, 19, 97, 101])
def test_small_primes(n):
    assert is_prime(n) is True

@pytest.mark.parametrize("n", [4, 6, 8, 9, 10, 12, 15, 21, 100, 121, 221])
def test_small_composites(n):
    assert is_prime(n) is False

def test_large_prime():
    # 1_000_000_007 là số nguyên tố (thường dùng trong lập trình)
    assert is_prime(1_000_000_007) is True

def test_large_composite():
    # 1_000_000_008 = 16 * 62_500_000
    assert is_prime(1_000_000_008) is False

@pytest.mark.parametrize("n", [2, 3])
def test_base_cases(n):
    assert is_prime(n) is True

def test_even_numbers_greater_than_two():
    for x in range(4, 200, 2):
        assert is_prime(x) is False

def test_multiples_of_three_greater_than_three():
    for x in range(6, 201, 3):
        assert is_prime(x) is False
