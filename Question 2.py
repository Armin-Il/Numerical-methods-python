import numpy as np

def f(x):
    return x**3 - 9.010*x - 5

def df(x):
    return 3*x**2 - 9.010

x0 = 3.5  # حدس اولیه
deghat = 1e-6  # دقت
max_tekrar = 20  #تکرار

# Print table header
print(f"{'tekrar':<5}{'x_n':<12}{'f(x_n)':<15}{'df(x_n)':<15}")
print("-" * 50)

x = x0
for i in range(max_tekrar):
    fx = f(x)
    dfx = df(x)
    
    print(f"{i:<5}{x:<12.6f}{fx:<15.6e}{dfx:<15.6f}")
    
    if abs(fx) < deghat:
        print(f"\n Rishe peyda shod dar x = {x:.6f} baad {i} tekrar.")
        break
    # نیوتن رافسون 
    x = x - fx / dfx