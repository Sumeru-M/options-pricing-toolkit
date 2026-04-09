"""
Option Greeks (sensitivity measures).
"""

import numpy as np
from scipy.stats import norm


def delta_call(S, K, T, r, sigma):
    """
    Measures sensitivity of option price to stock price changes.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return norm.cdf(d1)


def gamma(S, K, T, r, sigma):
    """
    Measures rate of change of delta.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))
