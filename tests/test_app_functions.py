"""
Unit Tests for application
"""
import pytest

from application.app_functions import calc_max_loan_amount, clean_divide


@pytest.mark.parametrize(
    ("numerator", "denomerator", "round_decimal", "expected"),
    ((10, 20, 1, 0.5), (100, 0, 0, 0), (20, 10, 0, 2)),
)
def test_clean_divide(numerator, denomerator, round_decimal, expected) -> None:
    """
    Unit Test to test the divide function
    """
    # Act
    actual = clean_divide(numerator, denomerator, round_decimal)
    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    ("monthly_payment", "interest_rate_per_month", "number_months_loan", "expected"),
    ((1000, 0.005, 36, 32871.01623926526),),
)
def test_calc_max_loan_amount(
    monthly_payment, interest_rate_per_month, number_months_loan, expected
) -> None:
    """
    Unit Test to test the calculate loan amount
    """
    # Act
    actual = calc_max_loan_amount(
        monthly_payment, interest_rate_per_month, number_months_loan
    )
    # Assert
    assert actual == expected
