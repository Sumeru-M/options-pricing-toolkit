"""
Input validation functions.
"""


def validate_inputs(S, K, T, sigma):
    """
    Ensure all inputs are valid.
    """
    if S <= 0:
        raise ValueError("Stock price must be positive")

    if K <= 0:
        raise ValueError("Strike price must be positive")

    if T <= 0:
        raise ValueError("Time to maturity must be positive")

    if sigma <= 0:
        raise ValueError("Volatility must be positive")
