import numpy as np

k1 = 41000.0  
k2 = 40.0     
h = 0.41      
m = 98.0
g = 9.81

def f(d_prime):
    return (2.0 * k2 / 5.0) * (d_prime ** 2.5) + 0.5 * k1 * (d_prime ** 2) - m * g * d_prime - m * g * h

def df(d_prime):
    return k2 * (d_prime ** 1.5) + k1 * d_prime - m * g

def newton_raphson(x0, deghat=1e-6, max_tekrar=20):
    x = x0
    print(f"{'tekrar':<8}{'dprime':<18}{'khata f(x)':<15}")
    print("-" * 45)
    
    for tekrar in range(1, max_tekrar + 1):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            print("moshtagh 0 shod")
            return None
            
        x_new = x - fx / dfx
        print(f"{tekrar:<8}{x_new:<18.6f}{abs(f(x_new)):<15.2e}")
        
        if abs(x_new - x) < deghat:
            return x_new
            
        x = x_new
        
    return x
# haads avaliye =0.1
print("Newton Raphson calculation is now beginning:\n")
Rishe_nahayi = newton_raphson(x0=1.0)

print("\n" + "="*45)
print(f"d': {Rishe_nahayi:.6f}")
print("="*45)  