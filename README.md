# Black-Scholes Option Pricer

🔗 **Live App:** https://black-scholes-app-horia.streamlit.app/

This application computes the no-arbitrage European option prices using the Black-Scholes Pricing Model by allowing user to interactively change the parameters.

### Understanding the Formulas
The Black-Scholes Model assumes the stock price St at time t is given by the Geometric Brownian Motion (Solution of the SDE).
- For the European Call: EC(K,T) its price is given by the explicit formula: **`EC(K,T) = exp(-qT)S0*N(d1) - Kexp(-rT)N(d2)`**
  
- For the European Put: **`EP(K,T) = -exp(-qT)S0*N(-d1) + Kexp(-rT)N(-d2)`**

With: **`d1 = (log(S0/K) + (r - q - σ^2/2)T) / σ√T`**, and **`d2 = d1 - σ√T`**

**`N(x)`** is the Cumulative Distribution Function (CDF) of the Standard Normal Distribution ~ N(0,1)

### Input Parameters
**`T`** Time to Maturity

**`S0`** Current Stock Price

**`K`** Strike Price

**`σ`** Annualized Volatility of the Stock 

**`r`** Continuously Compounded Annual Interest Rate

If we were to price **American Options**, both Calls and Puts, under a non-negative risk-free rate (`r >= 0)`:
- For **American Calls**: If the dividend yield `q` is zero or very small, `AC = EC` under a positive risk-free rate, therefore the price is correctly given by the Black-Scholes Pricing Model.

- To **American Puts** we need to construct a **Binomial Tree Model** with N > 100 nodes (ideally 500), where at each node the algorithm must determine the correct option price
