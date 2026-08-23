import numpy as np

def f(x):
    return np.tanh(x**2 - 9.0109)

def df(x):
    return 2 * x * (1 - np.tanh(x**2 - 9.0109)**2)

x0 = 3.0  # حدس اولیه نزدیک به ریشه
deghat = 1e-6  #دقت
max_tekrar = 20  #تکرار ماکسیمم

print(f"{'tekrar':<7}{'x_n':<12}{'f(x_n)':<15}{'df(x_n)':<15}")
print("-" * 50)

x = x0
for i in range(max_tekrar):
    fx = f(x)
    dfx = df(x)
    
    print(f"{i:<5}{x:<12.6f}{fx:<15.6e}{dfx:<15.6f}")
    
    if abs(fx) < deghat:
        print(f"\n Rishe peyda shod dar x = {x:.6f} baad {i} tekrar.")
        break
    
    if dfx == 0:
        print("0 shod va in ravesh javab nemide")
        break
    #نیوتن رافسون 
    x = x - fx / dfx