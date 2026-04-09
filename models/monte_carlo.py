"""
Monte Carlo simulation for option pricing.
"""

import numpy as np


def monte_carlo_call(S, K, T, r, sigma, simulations=10000):
    """
    Estimate call option price using Monte Carlo simulation.
    """

    # Generate random normal values
    Z = np.random.standard_normal(simulations)

    # Simulate future stock prices
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    # Calculate payoff for each simulation
    payoffs = np.maximum(ST - K, 0)

    # Discount back to present value
    price = np.exp(-r * T) * np.mean(payoffs)

    return price
