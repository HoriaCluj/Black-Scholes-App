import streamlit as st
import numpy as np
import math
from scipy.stats import norm

def BlackScholesCall(r, T, S0, K, sigma):
  d1 = (math.log(S0/K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T)

  EC = S0*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
  return round(float(EC), 2)


def BlackScholesPut(r, T, S0, K, sigma):
  d1 = (math.log(S0/K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T)

  EP = -S0*norm.cdf(-d1) + K*np.exp(-r*T)*norm.cdf(-d2)
  return round(float(EP), 2)

st.title("Black-Scholes Option Pricer 📈")
st.write("This app computes the No-Arbitrage prices of European Options using the Black-Scholes Pricing Model")
S = st.number_input("Current Stock Price", value=100.0)
K = st.number_input("Strike Price", value=105.0)
sigma = st.number_input("Annual Volatility", value=0.2)
r = st.number_input("Annual Risk-Free Rate", value=0.05)
T = st.number_input("Time to Maturity (Years)", value=1)

price_call = BlackScholesCall(r, T, S, K, sigma)
price_put = BlackScholesPut(r, T, S, K, sigma)
st.metric("European Call", price_call)
st.metric("European Put", price_put)
