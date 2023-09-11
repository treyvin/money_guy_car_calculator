"""
Useful functions for the streamlit application
"""


def clean_divide(numerator: float, denominator: float, round_decimal: int) -> float:
    """Function to divide and handle for 0 with an option to round.
    If rounding to the 0 place it will return an integer

    Args:
        numerator (float): numerator
        denominator (float): denominator
        round_decimal (int): decimal places to round to

    Returns:
        float: dividing result
    """
    if denominator == 0:
        return 0
    if round_decimal == 0:
        return int(numerator / denominator)
    return round(numerator / denominator, round_decimal)


def calc_max_loan_amount(
    monthly_payment: float, interest_rate_per_month: float, number_months_loan: int
) -> float:
    """Formula used to calculate the max loan amount based on the parameters

    Args:
        max_monthly_payment (float): The max amount can pay for a monthly payment
        interest_rate_per_month (float): Interest rate on the loan
        number_months_loan (int): Length of the loan in Months

    Returns:
        float: the max total amount to borrow
    """
    max_loan_amount = monthly_payment / (
        (
            (
                interest_rate_per_month
                * (1 + interest_rate_per_month) ** number_months_loan
            )
        )
        / ((1 + interest_rate_per_month) ** number_months_loan - 1)
    )
    return max_loan_amount
