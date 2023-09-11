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
