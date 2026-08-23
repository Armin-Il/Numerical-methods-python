import numpy as np

a, b, c = 9, 0, 1
coeff = float(f"{a}.{b}{c}")  # 9.01

def f(x):
    numerator = coeff * x
    denominator = 2 * np.exp(x) - np.exp(-x)
    return numerator / denominator

def simpson_13_rule(a_lim, b_lim, n):
    if n % 2 != 0:
        n += 1  
        
    h = (b_lim - a_lim) / n
    x = np.linspace(a_lim, b_lim, n + 1)
    y = f(x)
    
    sum_odd = np.sum(y[1:-1:2])
    sum_even = np.sum(y[2:-1:2])
    
    integral = (h / 3) * (y[0] + 4 * sum_odd + 2 * sum_even + y[-1])
    return integral

print(f"--- integral calculate ba zarib soorat : {coeff} ---")
for n_val in [2, 4, 10, 100]:
    result = simpson_13_rule(0, 1, n_val)
    print(f"n = {n_val:<3} -> meghdar integral : {result:.6f}")