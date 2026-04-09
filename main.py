"""
Main script to test the toolkit from command line.
"""

from models.black_scholes import call_option_price, put_option_price
from models.monte_carlo import monte_carlo_call
from models.greeks import delta_call, gamma
from utils.validators import validate_inputs
from utils.helpers import format_output


def run():
    """
    Run sample calculations.
    """

    # Sample inputs
    S = 100      # Stock price
    K = 100      # Strike price
    T = 1        # Time (years)
    r = 0.05     # Risk-free rate
    sigma = 0.2  # Volatility

    # Validate inputs
    validate_inputs(S, K, T, sigma)

    # Calculate option prices
    call_bs = call_option_price(S, K, T, r, sigma)
    put_bs = put_option_price(S, K, T, r, sigma)
    call_mc = monte_carlo_call(S, K, T, r, sigma)

    # Calculate Greeks
    delta = delta_call(S, K, T, r, sigma)
    gamma_val = gamma(S, K, T, r, sigma)

    # Print results
    print(format_output("Black-Scholes Call", call_bs))
    print(format_output("Black-Scholes Put", put_bs))
    print(format_output("Monte Carlo Call", call_mc))
    print(format_output("Delta", delta))
    print(format_output("Gamma", gamma_val))


if __name__ == "__main__":
    run()
