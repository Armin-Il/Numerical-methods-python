import numpy as np

a, c, d, b = 9, 1, 0, 0
meghdar_hadaf = float(f"0.7{a}{c}{d}{b}") # 0.79100

print(f"---sabet masale : {meghdar_hadaf} ---\n")

def f(x):
    return np.log(x**2) - meghdar_hadaf

def df(x):
    return 2.0 / x

def newton_raphson(x0, deghat=1e-6, max_tekrar=20):
    x = x0
    print(f"{'tekrar':<8}{'meghdar x':<15}{'khata f(x)':<15}")
    print("-" * 40)
    
    for tekrar in range(1, max_tekrar + 1):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            print("moshtagh 0 shod")
            return None
            
        x_new = x - fx / dfx
        print(f"{tekrar:<8}{x_new:<15.6f}{abs(f(x_new)):<15.2e}")
        
        if abs(x_new - x) < deghat:
            return x_new
            
        x = x_new
        
    return x

# hads avaliye 2
Rishe_nahayi = newton_raphson(x0=2.0)

print("\n" + "="*40)
print(f"{Rishe_nahayi:.6f}")
print(f"*(rishe dige {(-Rishe_nahayi):.6f} )*")
print("="*40)