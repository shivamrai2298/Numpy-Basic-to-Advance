"""
solving_linear_equations.py
============================
TOPICS COVERED
- Solving Ax = b
- np.linalg.solve
- Why solve() is preferred over inverse

INTERVIEW QUESTIONS
1. How do you solve linear equations in NumPy?
2. Why is np.linalg.solve better than inverse?
3. What happens if system is underdetermined?
4. How is this used in regression?

PRACTICE QUESTIONS
1. Solve a 3x3 system
2. Compare inverse vs solve performance
3. Handle singular matrix error
"""

import numpy as np

A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Solve Ax = b
x = np.linalg.solve(A, b)

print("Solution x:", x)

# Verification
print("Ax:", A @ x)
