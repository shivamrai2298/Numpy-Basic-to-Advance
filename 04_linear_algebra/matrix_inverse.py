"""
matrix_inverse.py
==================
TOPICS COVERED
- Matrix inverse
- Singular matrix
- Identity matrix
- Numerical stability

INTERVIEW QUESTIONS
1. What is a matrix inverse?
2. When does inverse not exist?
3. Difference between inverse and transpose?
4. Why is inverse avoided in ML?

PRACTICE QUESTIONS
1. Verify A * A_inv = I
2. Try inverse of singular matrix
3. Check determinant before inverse
"""

import numpy as np

A = np.array([[4, 7], [2, 6]])

A_inv = np.linalg.inv(A)
print("Inverse:\n", A_inv)

# Verify identity
identity = A @ A_inv
print("\nA * A_inv:\n", identity)

# Determinant
det = np.linalg.det(A)
print("\nDeterminant:", det)
