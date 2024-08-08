#Years
import math
from scipy.stats import norm

def black_scholes_option_price(S, X, T, r, sigma, option_type):
    """
    Calculate the Black-Scholes option price.

    :param S: Current stock price
    :param X: Option strike price
    :param T: Time to expiration (in years)
    :param r: Risk-free interest rate
    :param sigma: Volatility of the stock price
    :param option_type: 'call' for call option or 'put' for put option
    :return: Option price
    """
    d1 = (math.log(S / X) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - X * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = X * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")

    return option_price

# Input parameters
S = 158.492  # Current stock price
X = 100  # Option strike price
T = 1.0  # Time to expiration (Time Expiration in Years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility of the stock price

# Calculate call option price
call_option_price = black_scholes_option_price(S, X, T, r, sigma, 'call')
print("Call Option Price: ${:.2f}".format(call_option_price))

# Calculate put option price
put_option_price = black_scholes_option_price(S, X, T, r, sigma, 'put')
print("Put Option Price: ${:.2f}".format(put_option_price))