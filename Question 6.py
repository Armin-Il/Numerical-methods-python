import numpy as np

# Hads avaliye
T11 = 0.0
T12 = 0.0
T21 = 0.0
T22 = 0.0

max_tekrar = 30  
deghat = 1e-4

print(f"{'tekrar':<6}{'T11':<10}{'T12':<10}{'T21':<10}{'T22':<10}")
print("-" * 46)
print(f"{0:<6}{T11:<10.3f}{T12:<10.3f}{T21:<10.3f}{T22:<10.3f}")

for k in range(1, max_tekrar + 1):
    T11_old, T12_old, T21_old, T22_old = T11, T12, T21, T22
    
    T11 = (175.0 + T12 + T21) / 4.0
    T12 = (125.0 + T11 + T22) / 4.0
    T21 = (75.0 + T11 + T22) / 4.0
    T22 = (25.0 + T12 + T21) / 4.0
    
    print(f"{k:<6}{T11:<10.3f}{T12:<10.3f}{T21:<10.3f}{T22:<10.3f}")
    
    # hamgerayi 
    errors = [abs(T11-T11_old), abs(T12-T12_old), abs(T21-T21_old), abs(T22-T22_old)]
    if max(errors) < deghat:
        print("\n hamgera shod")
        break

print("\n" + "="*46)
print("answers")
print(f"T11 = {T11:.2f} °C\nT12 = {T12:.2f} °C\nT21 = {T21:.2f} °C\nT22 = {T22:.2f} °C")
print("="*46)