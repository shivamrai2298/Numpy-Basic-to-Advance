"""
dot_matmul.py
==============
TOPICS COVERED
- np.dot
- np.matmul
- @ operator
- Vector vs Matrix multiplication

INTERVIEW QUESTIONS
1. Difference between dot() and matmul()?
2. When does dot perform inner product?
3. Why is @ preferred for matrix multiplication?
4. What happens if shapes are incompatible?

PRACTICE QUESTIONS
1. Compute dot product of two vectors
2. Multiply two matrices using @
3. Multiply matrix with vector
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vector dot product
print("Dot Product:", np.dot(a, b))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print("\nMatrix Multiply (matmul):\n", np.matmul(A, B))
print("\nMatrix Multiply (@):\n", A @ B)
