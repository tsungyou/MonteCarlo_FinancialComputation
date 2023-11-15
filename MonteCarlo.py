import math
from scipy.stats import norm
import numpy as np
S = 100
r = 0.05
q = 0.02
sigma = 0.5
T = 0.4
K1 = 90
K2 = 98
K3 = 102
K4 = 110

'''
Option price when K4 is 110: 1.1717
Option price when K4 is 104: 0.9013
'''

def d(K, is_d1=True):
    term1 = math.log(S/K) + (r - q + (sigma**2)/2)*T
    term2 = math.log(S/K) + (r - q - (sigma**2)/2)*T
    if is_d1:
        return term2 / (sigma*math.sqrt(T))
    else:
        return term1 / (sigma*math.sqrt(T))
    
# Distribution
def N(x):
    return norm.cdf(x)
def black_scholes_custom(K4=110):

    price = (
        S*math.exp(-q*T)*(N(-d(K2, False))-N(-d(K1, False)))
        -K1*math.exp(-r*T)*(N(-d(K2, True))-N(-d(K1, True)))
        +math.exp(-r*T)*(K2-K1)*(N(-d(K3, True))-N(-d(K2, True)))
        -S*math.exp(-q*T)*((K2-K1)/(K4-K3))*(N(-d(K4, False))-N(-d(K3, False)))
        +(((K2-K1)/(K4-K3))*K3 + K2 - K1)*math.exp(-r*T)*(N(-d(K4, True))-N(-d(K3, True)))
    )
    return np.round(price, 4)

def main():
    print("Option price when K4 is 110:", black_scholes_custom())
    print("Option price when K4 is 104:", black_scholes_custom(K4 = 104))
    


if __name__ == "__main__":
    main()
