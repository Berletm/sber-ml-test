import numpy as np
from scipy.stats import norm

rf = 0.02821
T  = 1.0
sigma = 0.085
rd = 0.0364
K1 = 0.9
K2 = 1.1
S  = 1.17

c = lambda x1, x2, k: S * np.exp(-rf * T) * norm.cdf(x1) - k * np.exp(-rd * T) * norm.cdf(x2)
delta = lambda x: np.exp(-rf * T) * norm.cdf(x)
gamma = lambda x: np.exp(-rf * T) * norm.pdf(x) / (S * sigma * np.sqrt(T))
theta = lambda x1, x2, k: rf*S*np.exp(-rf * T) * norm.cdf(x1) - rd*k*np.exp(-rd * T) * norm.cdf(x2) - S * np.exp(-rf * T) * norm.pdf(x1) * sigma / (2 * np.sqrt(T))

d1 = lambda x: (np.log(S / x) + (rd - rf + (sigma**2) / 2)*T) / (sigma * np.sqrt(T))

d1_n1 = d1(K1 * S)
d1_n2 = d1(K2 * S)

delta_n1 = delta(d1_n1)
delta_n2 = delta(d1_n2)

gamma_n1 = gamma(d1_n1)
gamma_n2 = gamma(d1_n2)

theta_n1 = theta(d1_n1, d1_n1 - sigma*np.sqrt(T), S*K1)
theta_n2 = theta(d1_n2, d1_n2 - sigma*np.sqrt(T), S*K2)

c_n1 = c(d1_n1, d1_n1 - sigma*np.sqrt(T), S*K1)
c_n2 = c(d1_n2, d1_n2 - sigma*np.sqrt(T), S*K2)

# print(f"{delta_n1} {delta_n2}")
# print(f"{gamma_n1} {gamma_n2}")
print(f"Theta {theta_n1} {theta_n2}")
print(f"C     {c_n1} {c_n2}")
# print(100_000 / eval("1.1970 * 0.1259 - 0.7501 * 0.0080 - 0.9472 * 1.17"))
# print(eval("0.7501 * (-103785.8482)"))
# print(eval("-124.2316 * -0.0114 + 77.8497 * -0.0131"))
print(eval("0.3964 * -103785.8482"))
print(eval("-124231.6602 * -0.0114 + 77849.7647 * -0.0131"))
print(eval("-0.9472 * (-103785.8482)"))