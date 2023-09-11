"""
Unit Tests for application
"""
import pytest

from application.app_functions import clean_divide


@pytest.mark.parametrize(
    ("numerator", "denomerator", "round_decimal", "expected"),
    ((10, 20, 1, 0.5), (100, 0, 0, 0), (20, 10, 0, 2)),
)
def test_clean_divide(numerator, denomerator, round_decimal, expected) -> None:
    """
    Pytest to test the divide function
    """
    # Act
    actual = clean_divide(numerator, denomerator, round_decimal)
    # Assert
    assert actual == expected
