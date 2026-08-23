"""
CLI Command-Line Interface Runner
Executes Numerical Analysis Suite problems sequentially or interactively.
"""

from numerical_suite import NumericalSuite


def main():
    print("=" * 60)
    print("    NUMERICAL ANALYSIS SUITE - INTERACTIVE SOLVER")
    print("=" * 60)

    student_id = input("Enter Student ID (Press Enter for default '1234'): ").strip()
    if not student_id:
        student_id = "1234"

    solver = NumericalSuite(student_id=student_id)

    while True:
        print("\nSelect an algorithm to run:")
        print("1. Problem 1: Newton-Raphson Hyperbolic Solver")
        print("2. Problem 2: Polynomial Root Finder")
        print("3. Problem 3: Non-Linear Spring Equilibrium")
        print("4. Problem 4: Logarithmic Equation Solver")
        print("5. Problem 5: Simpson's 1/3 Integration Rule")
        print("6. Problem 6: 2D Heat Conduction (Gauss-Seidel)")
        print("7. Problem 7: LC Circuit Dynamics & Eigenvalues")
        print("8. Run ALL Solvers")
        print("0. Exit")

        choice = input("\nEnter choice (0-8): ").strip()

        if choice == "1":
            solver.solve_hyperbolic_newton()
        elif choice == "2":
            solver.solve_polynomial_newton()
        elif choice == "3":
            solver.solve_spring_equilibrium()
        elif choice == "4":
            solver.solve_logarithmic_newton()
        elif choice == "5":
            solver.integrate_simpson()
        elif choice == "6":
            solver.solve_heat_transfer_gauss_seidel()
        elif choice == "7":
            solver.solve_lc_circuit_eigenvalues()
        elif choice == "8":
            solver.solve_hyperbolic_newton()
            solver.solve_polynomial_newton()
            solver.solve_spring_equilibrium()
            solver.solve_logarithmic_newton()
            solver.integrate_simpson()
            solver.solve_heat_transfer_gauss_seidel()
            solver.solve_lc_circuit_eigenvalues()
        elif choice == "0":
            print("\nExiting Numerical Suite. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 8.")


if __name__ == "__main__":
    main()
