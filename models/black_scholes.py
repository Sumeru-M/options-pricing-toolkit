"""
Black-Scholes pricing model for European options.
"""

import numpy as np
from scipy.stats import norm


def _calculate_d1(S, K, T, r, sigma):
    """Helper function to calculate d1."""
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))


def _calculate_d2(d1, sigma, T):
    """Helper function to calculate d2."""
    return d1 - sigma * np.sqrt(T)


def call_option_price(S, K, T, r, sigma):
    """
    Calculate European call option price using Black-Scholes formula.
    """
    d1 = _calculate_d1(S, K, T, r, sigma)
    d2 = _calculate_d2(d1, sigma, T)

    # Call option formula
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


def put_option_price(S, K, T, r, sigma):
    """
    Calculate European put option price using Black-Scholes formula.
    """
    d1 = _calculate_d1(S, K, T, r, sigma)
    d2 = _calculate_d2(d1, sigma, T)

    # Put option formula
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price
