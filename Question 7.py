import numpy as np
from scipy.linalg import eigh

a, b, c, d_prime = 9, 0, 1, 0

def daryaft(d1, d2, d3, d4):
    return float(f"0.{d1}{d2}{d3}{d4}")

L1 = daryaft(b, d_prime, c, a)
L2 = daryaft(c, d_prime, a, b)
L3 = daryaft(a, d_prime, b, c)

C1 = daryaft(d_prime, c, b, a)
C2 = daryaft(d_prime, a, b, c)
C3 = daryaft(b, c, d_prime, a)

print("parameter")
print(f"L = [{L1}, {L2}, {L3}]")
print(f"C = [{C1}, {C2}, {C3}]")
print("-" * 30)

M = np.diag([L1, L2, L3])

K = np.array([
    [1/C1, -1/C1, 0],
    [-1/C1, (1/C1 + 1/C2), -1/C2],
    [0, -1/C2, (1/C2 + 1/C3)]
])

eigenvalues, eigenvectors = eigh(K, M)

idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("\n--- Answers ---")
for i in range(3):
    # manfi nabashe zir radikal
    val = max(eigenvalues[i], 0)
    freq = np.sqrt(val)
    print(f"Mode {i+1}:")
    print(f"  Lambda: {val:.4f}")
    print(f"  Natural Frequency omega w: {freq:.4f} rad/s")
    print(f"  Eigenvector: {eigenvectors[:, i]}")
    print("-" * 20)