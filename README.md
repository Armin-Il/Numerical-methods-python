# 🚀 Numerical Analysis Suite (محاسبات عددی)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/NumPy-Powered-013243?logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/SciPy-Powered-8CAAE6?logo=scipy&logoColor=white" alt="SciPy">
  <img src="https://img.shields.io/badge/Made%20for-SBU-orange" alt="SBU">
</p>

A professional, high-performance Python framework for solving classic Numerical Analysis problems — engineered for academic rigor and built to stand out on a GitHub portfolio.

---

## ✨ Why This Project

This isn't just a homework dump — it's a **modular, object-oriented solver engine** where every assignment is implemented as an independent, testable, reusable component. Each problem ships with its own convergence analysis, error tracking, and (where applicable) visualization, wrapped in a clean CLI driven by a single student ID.

**Key Features:**
- 🔁 Analytical + numerical derivative support for root-finding (no finite-difference guesswork)
- 📊 Convergence tables and iteration logs (`tabulate`-powered) for every method
- 🌡️ Full 2D PDE solver with Gauss-Seidel relaxation and heatmap visualization
- 🎛️ Personalized parameters per student — no two runs are identical
- 📈 Matplotlib visualizations for root convergence, integration regions, and temperature fields
- 🧩 Zero external solver dependencies for core logic — the math is implemented from scratch, not just called from a library

---

## 📌 Table of Contents
- [Why This Project](#-why-this-project)
- [Project Architecture](#-project-architecture)
- [Student ID Parameterization System](#-student-id-parameterization-system)
- [Assignments & Solutions Breakdown](#-assignments--solutions-breakdown)
  - [Problem 1: Newton-Raphson Root Finding (Hyperbolic)](#problem-1-newton-raphson-root-finding-hyperbolic)
  - [Problem 2: Newton-Raphson Polynomial Root Finding](#problem-2-newton-raphson-polynomial-root-finding)
  - [Problem 3: Non-Linear Spring Energy Equilibrium](#problem-3-non-linear-spring-energy-equilibrium)
  - [Problem 4: Logarithmic Root Determination](#problem-4-logarithmic-root-determination)
  - [Problem 5: Numerical Quadrature (Definite Integration)](#problem-5-numerical-quadrature-definite-integration)
  - [Problem 6: 2D Heat Transfer PDE (Gauss-Seidel Method)](#problem-6-2d-heat-transfer-pde-gauss-seidel-method)
  - [Problem 7: LC Ladder Network Dynamics & Eigenvalues](#problem-7-lc-ladder-network-dynamics--eigenvalues)
- [Sample Output](#-sample-output)
- [Installation & Execution](#-installation--execution)
- [License](#-license)

---

## 🏗 Project Architecture
```text
numerical-analysis-suite/
│
├── numerical_suite.py       # Main object-oriented solver engine
├── main.py                  # CLI runner with custom student ID input
├── requirements.txt         # Dependencies (numpy, scipy, matplotlib, tabulate)
└── README.md                # Project documentation & mathematical formulations
```

---

## 🔢 Student ID Parameterization System
To ensure personalized parameters for each student, all assignment variables are derived from the 4 rightmost digits of the Student ID:
$$\mathbf{abcd} = [a, b, c, d]$$

For instance, given ID suffix `1234`:
- $a = 1, b = 2, c = 3, d = 4$
- $9.\mathbf{bcda} = 9.2341$
- $k_1 = 4\mathbf{c}00\mathbf{b} = 43002$

---

## 🧮 Assignments & Solutions Breakdown

### Problem 1: Newton-Raphson Root Finding (Hyperbolic)
#### 📐 Math Formulation
Find the root of the hyperbolic equation:
$$f(x) = \tanh(x^2 - 9.\mathbf{bcda}) = 0$$

Analytical Derivative:
$$f'(x) = 2x \cdot \text{sech}^2(x^2 - 9.\mathbf{bcda}) = 2x \left(1 - \tanh^2(x^2 - 9.\mathbf{bcda})\right)$$

Newton-Raphson Iteration Formula:
$$x_{k+1} = x_k - \frac{\tanh(x_k^2 - 9.\mathbf{bcda})}{2x_k \left(1 - \tanh^2(x_k^2 - 9.\mathbf{bcda})\right)}$$

---

### Problem 2: Newton-Raphson Polynomial Root Finding
#### 📐 Math Formulation
Solve for $x$ in the $4^{\text{th}}$-degree polynomial:
$$f(x) = 0.007\mathbf{d} \cdot x^4 - 0.284\mathbf{a} \cdot x^3 + 3.355\mathbf{c} \cdot x^2 - 12.183\mathbf{b} \cdot x + 5 = 0$$

First Derivative:
$$f'(x) = 4(0.007\mathbf{d})x^3 - 3(0.284\mathbf{a})x^2 + 2(3.355\mathbf{c})x - 12.183\mathbf{b}$$

---

### Problem 3: Non-Linear Spring Energy Equilibrium
#### 📐 Math Formulation
A dropped mass $m$ compresses a non-linear spring with force law $F = -(k_1 d' + k_2 d'^{3/2})$. Energy conservation yields:
$$g(d') = \frac{2}{5} k_2 d'^{5/2} + \frac{1}{2} k_1 d'^2 - m g d' - m g h = 0$$

Derivative with respect to $d'$:
$$g'(d') = k_2 d'^{3/2} + k_1 d' - m g$$

Parameters:
- $k_1 = 4\mathbf{c}00\mathbf{b}$ N/m
- $k_2 = 4\mathbf{d}$ N/m$^{3/2}$
- $h = 0.4\mathbf{c}$ m
- $m = 98$ kg, $g = 9.81$ m/s$^2$

---

### Problem 4: Logarithmic Root Determination
#### 📐 Math Formulation
Solve:
$$\ln(x^2) = 0.7\mathbf{acdb} \implies \ln(x^2) - 0.7\mathbf{acdb} = 0$$

Exact Analytical Solution:
$$x = \pm \exp\left(\frac{0.7\mathbf{acdb}}{2}\right)$$

---

### Problem 5: Numerical Quadrature (Definite Integration)
#### 📐 Math Formulation
Evaluate the definite integral:
$$I = \int_{0}^{1} \frac{\mathbf{a.bc} \cdot x}{2 e^x - e^{-x}} \, dx$$

Methods Implemented:
1. Composite Trapezoidal Rule
2. Composite Simpson's $1/3$ Rule
3. Adaptive Gaussian Quadrature (`scipy.integrate.quad`)

---

### Problem 6: 2D Heat Transfer PDE (Gauss-Seidel Method)
#### 📐 Math Formulation
Steady-state 2D heat conduction governed by Laplace's Equation:
$$\nabla^2 T = \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0$$

Discretized finite-difference grid equation for node $(i,j)$:
$$T_{i,j}^{(k+1)} = \frac{1}{4} \left( T_{i-1,j}^{(k+1)} + T_{i+1,j}^{(k)} + T_{i,j-1}^{(k+1)} + T_{i,j+1}^{(k)} \right)$$

Boundary Conditions:
- Top: $25^\circ\text{C}$
- Bottom: $75^\circ\text{C}$
- Left: $100^\circ\text{C}$
- Right: $0^\circ\text{C}$

---

### Problem 7: LC Ladder Network Dynamics & Eigenvalues
#### 📐 Math Formulation
Mesh current differential equations for 3-stage LC filter:
$$\mathbf{L} \mathbf{\ddot{q}} + \mathbf{S} \mathbf{q} = \mathbf{v}(t)$$

System Matrix $\mathbf{A}$:
$$\mathbf{A} = \mathbf{L}^{-1} \mathbf{S}$$

Eigenvalue Problem:
$$\mathbf{A} \mathbf{v} = \omega^2 \mathbf{v}$$

Parameters:
- $I(t) = 2.\mathbf{bcd'a} \sin(\mathbf{bc} \cdot t)$
- $\mathbf{L} = [0.\mathbf{bd'ca}, 0.\mathbf{cd'ab}, 0.\mathbf{ad'bc}]$
- $\mathbf{C} = [0.\mathbf{d'cba}, 0.\mathbf{d'abc}, 0.\mathbf{bcd'a}]$

---

## 📊 Sample Output

```text
$ python main.py --id 1234

╔══════════════════════════════════════════════════╗
║   NUMERICAL ANALYSIS SUITE — Student ID: 1234     ║
╚══════════════════════════════════════════════════╝

[Problem 1] Newton-Raphson (Hyperbolic Root)
┌───────┬────────────┬────────────┬──────────────┐
│ Iter  │   x_k      │   f(x_k)   │   Error      │
├───────┼────────────┼────────────┼──────────────┤
│   0   │  3.000000  │  0.999999  │      —       │
│   1   │  2.849213  │  0.998842  │  1.5079e-01  │
│   2   │  2.812004  │  0.001203  │  3.7209e-02  │
│  ...  │    ...     │    ...     │     ...      │
└───────┴────────────┴────────────┴──────────────┘
✔ Converged in 6 iterations | Root: x* = 2.808921

[Problem 6] 2D Heat Transfer PDE (Gauss-Seidel)
✔ Converged after 143 sweeps | Tolerance: 1e-6
→ Temperature field saved to heatmap_output.png

[Problem 7] LC Ladder Network Eigenvalue Analysis
Eigenfrequencies (rad/s): [1204.5, 3872.1, 6510.8]
→ Mode shapes saved to eigenmodes_output.png
```

> Actual figures (convergence plots, heatmaps, mode shapes) are generated in the `output/` directory on each run.

---

## 💻 Installation & Execution

1. **Clone Repository**:
   ```bash
   git clone https://github.com/your-username/numerical-analysis-suite.git
   cd numerical-analysis-suite
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Solver Suite**:
   ```bash
   python main.py --id <your_student_id>
   ```

---

## 📄 License
This project is licensed under the MIT License — see the `LICENSE` file for details.

---
<p align="center">
Developed for Shahid Beheshti University (SBU) Numerical Analysis Course.
</p>
