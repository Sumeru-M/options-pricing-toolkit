"""
Advanced Streamlit UI for Options Pricing Toolkit
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Fix import path issue
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.black_scholes import call_option_price, put_option_price
from models.monte_carlo import monte_carlo_call
from models.greeks import delta_call, gamma
from utils.validators import validate_inputs


# -------------------------------
# UI Title
# -------------------------------
st.title("📊 Options Pricing Toolkit")

st.markdown("Compare **Black-Scholes** and **Monte Carlo** models with interactive inputs.")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("Input Parameters")

S = st.sidebar.slider("Stock Price (S)", 1.0, 500.0, 100.0)
K = st.sidebar.slider("Strike Price (K)", 1.0, 500.0, 100.0)
T = st.sidebar.slider("Time to Maturity (Years)", 0.1, 5.0, 1.0)
r = st.sidebar.slider("Risk-Free Rate", 0.0, 0.2, 0.05)
sigma = st.sidebar.slider("Volatility (σ)", 0.01, 1.0, 0.2)
simulations = st.sidebar.slider("Monte Carlo Simulations", 1000, 50000, 10000)

# -------------------------------
# Validation
# -------------------------------
try:
    validate_inputs(S, K, T, sigma)

    # -------------------------------
    # Pricing Calculations
    # -------------------------------
    call_bs = call_option_price(S, K, T, r, sigma)
    put_bs = put_option_price(S, K, T, r, sigma)
    call_mc = monte_carlo_call(S, K, T, r, sigma, simulations)

    delta = delta_call(S, K, T, r, sigma)
    gamma_val = gamma(S, K, T, r, sigma)

    # -------------------------------
    # Display Prices
    # -------------------------------
    st.subheader("💰 Option Prices")

    col1, col2, col3 = st.columns(3)

    col1.metric("Call (Black-Scholes)", f"{call_bs:.4f}")
    col2.metric("Put (Black-Scholes)", f"{put_bs:.4f}")
    col3.metric("Call (Monte Carlo)", f"{call_mc:.4f}")

    # -------------------------------
    # Greeks
    # -------------------------------
    st.subheader("📐 Greeks")

    col1, col2 = st.columns(2)
    col1.metric("Delta", f"{delta:.4f}")
    col2.metric("Gamma", f"{gamma_val:.6f}")

    # -------------------------------
    # Payoff Diagram
    # -------------------------------
    st.subheader("📈 Payoff Diagram (Call Option)")

    stock_prices = np.linspace(0.5 * S, 1.5 * S, 100)
    payoff = np.maximum(stock_prices - K, 0)

    fig, ax = plt.subplots()
    ax.plot(stock_prices, payoff)
    ax.set_xlabel("Stock Price at Expiry")
    ax.set_ylabel("Payoff")
    ax.set_title("Call Option Payoff")

    st.pyplot(fig)

    # -------------------------------
    # Model Comparison Insight
    # -------------------------------
    st.subheader("🧠 Model Insight")

    diff = abs(call_bs - call_mc)

    st.write(f"Difference between models: **{diff:.6f}**")

    if diff < 0.5:
        st.success("Models are closely aligned ✅")
    else:
        st.warning("Models differ significantly ⚠️ (increase simulations?)")

except ValueError as e:
    st.error(str(e))