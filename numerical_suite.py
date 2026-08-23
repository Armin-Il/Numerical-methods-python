"""
Numerical Analysis Suite Engine
A modular object-oriented Python framework for solving scientific & engineering numerical problems.
"""

import numpy as np
from scipy.linalg import eigh


class NumericalSuite:
    def __init__(self, student_id: str = "1234"):
        """Extract parameters dynamically from student ID digits."""
        digits = [int(d) for d in student_id.zfill(4)[-4:]]
        self.a, self.b, self.c, self.d = digits[0], digits[1], digits[2], digits[3]

    # ----------------------------------------------------
    # Problem 1: Newton-Raphson Hyperbolic Solver
    # ----------------------------------------------------
    def solve_hyperbolic_newton(self, x0: float = 3.0, tol: float = 1e-6, max_iter: int = 20):
        """Solves f(x) = tanh(x^2 - c) using Newton-Raphson method."""
        const_val = float(f"{self.a}.{self.b}{self.c}{self.d}")

        def f(x):
            return np.tanh(x**2 - const_val)

        def df(x):
            return 2 * x * (1 - np.tanh(x**2 - const_val)**2)

        print(f"\n--- Problem 1: Newton-Raphson Hyperbolic Solver (c = {const_val}) ---")
        print(f"{'Iter':<7}{'x_n':<12}{'f(x_n)':<15}{'df(x_n)':<15}")
        print("-" * 50)

        x = x0
        for i in range(max_iter):
            fx, dfx = f(x), df(x)
            print(f"{i:<7}{x:<12.6f}{fx:<15.6e}{dfx:<15.6f}")

            if abs(fx) < tol:
                print(f"\n[+] Root found at x = {x:.6f} after {i} iterations.")
                return x
            if dfx == 0:
                print("[-] Derivative is zero. Method failed.")
                return None
            x = x - fx / dfx
        return x

    # ----------------------------------------------------
    # Problem 2: Polynomial Root Finder
    # ----------------------------------------------------
    def solve_polynomial_newton(self, x0: float = 3.5, tol: float = 1e-6, max_iter: int = 20):
        """Solves f(x) = x^3 - c*x - 5 using Newton-Raphson method."""
        coeff = float(f"{self.a}.{self.b}{self.c}{self.d}")

        def f(x):
            return x**3 - coeff * x - 5

        def df(x):
            return 3 * x**2 - coeff

        print(f"\n--- Problem 2: Polynomial Root Finder (coeff = {coeff}) ---")
        print(f"{'Iter':<7}{'x_n':<12}{'f(x_n)':<15}{'df(x_n)':<15}")
        print("-" * 50)

        x = x0
        for i in range(max_iter):
            fx, dfx = f(x), df(x)
            print(f"{i:<7}{x:<12.6f}{fx:<15.6e}{dfx:<15.6f}")

            if abs(fx) < tol:
                print(f"\n[+] Root found at x = {x:.6f} after {i} iterations.")
                return x
            if dfx == 0:
                print("[-] Derivative is zero.")
                return None
            x = x - fx / dfx
        return x

    # ----------------------------------------------------
    # Problem 3: Non-Linear Spring Equilibrium
    # ----------------------------------------------------
    def solve_spring_equilibrium(self, x0: float = 1.0, tol: float = 1e-6, max_iter: int = 20):
        """Solves spring deflection equilibrium using Newton-Raphson method."""
        k1, k2 = 41000.0, 40.0
        h = 0.41
        m, g = 98.0, 9.81

        def f(d_prime):
            return (2.0 * k2 / 5.0) * (d_prime ** 2.5) + 0.5 * k1 * (d_prime ** 2) - m * g * d_prime - m * g * h

        def df(d_prime):
            return k2 * (d_prime ** 1.5) + k1 * d_prime - m * g

        print("\n--- Problem 3: Non-Linear Spring Equilibrium ---")
        print(f"{'Iter':<8}{'d_prime':<18}{'f(x) Error':<15}")
        print("-" * 45)

        x = x0
        for iteration in range(1, max_iter + 1):
            fx, dfx = f(x), df(x)
            if dfx == 0:
                print("[-] Derivative is zero.")
                return None

            x_new = x - fx / dfx
            print(f"{iteration:<8}{x_new:<18.6f}{abs(f(x_new)):<15.2e}")

            if abs(x_new - x) < tol:
                print("=" * 45)
                print(f"[+] Final Deflection (d'): {x_new:.6f} m")
                print("=" * 45)
                return x_new
            x = x_new
        return x

    # ----------------------------------------------------
    # Problem 4: Logarithmic Equation Solver
    # ----------------------------------------------------
    def solve_logarithmic_newton(self, x0: float = 2.0, tol: float = 1e-6, max_iter: int = 20):
        """Solves ln(x^2) - target = 0 using Newton-Raphson method."""
        target_val = float(f"0.7{self.a}{self.c}{self.d}{self.b}")

        def f(x):
            return np.log(x**2) - target_val

        def df(x):
            return 2.0 / x

        print(f"\n--- Problem 4: Logarithmic Equation Solver (Target = {target_val}) ---")
        print(f"{'Iter':<8}{'x Value':<15}{'f(x) Error':<15}")
        print("-" * 40)

        x = x0
        for iteration in range(1, max_iter + 1):
            fx, dfx = f(x), df(x)
            if dfx == 0:
                print("[-] Derivative is zero.")
                return None

            x_new = x - fx / dfx
            print(f"{iteration:<8}{x_new:<15.6f}{abs(f(x_new)):<15.2e}")

            if abs(x_new - x) < tol:
                print("=" * 40)
                print(f"[+] Positive Root:  {x_new:.6f}")
                print(f"[+] Negative Root: {-x_new:.6f}")
                print("=" * 40)
                return x_new
            x = x_new
        return x

    # ----------------------------------------------------
    # Problem 5: Simpson's 1/3 Numerical Quadrature
    # ----------------------------------------------------
    def integrate_simpson(self, a_lim: float = 0.0, b_lim: float = 1.0, n_list=None):
        """Computes definite integral using Simpson's 1/3 Rule."""
        if n_list is None:
            n_list = [2, 4, 10, 100]

        coeff = float(f"{self.a}.{self.b}{self.c}")

        def f(x):
            numerator = coeff * x
            denominator = 2 * np.exp(x) - np.exp(-x)
            return numerator / denominator

        def simpson_13(a_val, b_val, n):
            if n % 2 != 0:
                n += 1
            h = (b_val - a_val) / n
            x = np.linspace(a_val, b_val, n + 1)
            y = f(x)
            sum_odd = np.sum(y[1:-1:2])
            sum_even = np.sum(y[2:-1:2])
            return (h / 3) * (y[0] + 4 * sum_odd + 2 * sum_even + y[-1])

        print(f"\n--- Problem 5: Simpson's 1/3 Quadrature (Coeff = {coeff}) ---")
        for n_val in n_list:
            result = simpson_13(a_lim, b_lim, n_val)
            print(f"n = {n_val:<3} -> Integral Value: {result:.6f}")

    # ----------------------------------------------------
    # Problem 6: 2D Heat Transfer PDE (Gauss-Seidel)
    # ----------------------------------------------------
    def solve_heat_transfer_gauss_seidel(self, max_iter: int = 30, tol: float = 1e-4):
        """Solves 2D steady-state heat conduction PDE via Gauss-Seidel iteration."""
        T11, T12, T21, T22 = 0.0, 0.0, 0.0, 0.0

        print("\n--- Problem 6: 2D Heat Conduction (Gauss-Seidel Iteration) ---")
        print(f"{'Iter':<6}{'T11':<10}{'T12':<10}{'T21':<10}{'T22':<10}")
        print("-" * 46)
        print(f"{0:<6}{T11:<10.3f}{T12:<10.3f}{T21:<10.3f}{T22:<10.3f}")

        for k in range(1, max_iter + 1):
            T11_old, T12_old, T21_old, T22_old = T11, T12, T21, T22

            T11 = (175.0 + T12 + T21) / 4.0
            T12 = (125.0 + T11 + T22) / 4.0
            T21 = (75.0 + T11 + T22) / 4.0
            T22 = (25.0 + T12 + T21) / 4.0

            print(f"{k:<6}{T11:<10.3f}{T12:<10.3f}{T21:<10.3f}{T22:<10.3f}")

            errors = [abs(T11 - T11_old), abs(T12 - T12_old), abs(T21 - T21_old), abs(T22 - T22_old)]
            if max(errors) < tol:
                print("\n[+] System converged successfully.")
                break

        print("=" * 46)
        print("Temperature Distribution Results:")
        print(f"T11 = {T11:.2f} °C\nT12 = {T12:.2f} °C\nT21 = {T21:.2f} °C\nT22 = {T22:.2f} °C")
        print("=" * 46)

    # ----------------------------------------------------
    # Problem 7: LC Circuit Dynamics & Eigenvalues
    # ----------------------------------------------------
    def solve_lc_circuit_eigenvalues(self):
        """Solves generalized eigenvalue problem (K x = lambda M x) for LC ladder network."""
        def parse_param(d1, d2, d3, d4):
            return float(f"0.{d1}{d2}{d3}{d4}")

        L1 = parse_param(self.b, self.d, self.c, self.a)
        L2 = parse_param(self.c, self.d, self.a, self.b)
        L3 = parse_param(self.a, self.d, self.b, self.c)

        C1 = parse_param(self.d, self.c, self.b, self.a)
        C2 = parse_param(self.d, self.a, self.b, self.c)
        C3 = parse_param(self.b, self.c, self.d, self.a)

        print("\n--- Problem 7: LC Circuit Eigenvalue Solver ---")
        print(f"Inductances (H)  : L = [{L1}, {L2}, {L3}]")
        print(f"Capacitances (F) : C = [{C1}, {C2}, {C3}]")
        print("-" * 40)

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

        print("\nSystem Dynamics & Natural Frequencies:")
        for i in range(3):
            val = max(eigenvalues[i], 0)
            freq = np.sqrt(val)
            print(f"Mode {i+1}:")
            print(f"  Lambda (Eigenvalue): {val:.4f}")
            print(f"  Natural Frequency (omega): {freq:.4f} rad/s")
            print(f"  Eigenvector: {eigenvectors[:, i]}")
            print("-" * 30)
