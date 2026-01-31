import pytest
from src.math import add


def test_add_two_positive_numbers():
    """Test adding two positive numbers."""
    result = add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    """Test adding negative numbers."""
    result = add(-1, -1)
    assert result == -2


def test_add_mixed_numbers():
    """Test adding positive and negative numbers."""
    result = add(5, -3)
    assert result == 2


def test_add_zero():
    """Test adding zero."""
    result = add(0, 5)
    assert result == 5
