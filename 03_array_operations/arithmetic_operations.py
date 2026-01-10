"""
arithmetic_operations.py
========================
TOPICS COVERED
- Element-wise arithmetic
- Scalar operations
- Power, modulo
- Order of operations

INTERVIEW QUESTIONS
1. Are NumPy arithmetic operations element-wise by default?
2. Difference between * and dot()?
3. How does NumPy handle scalar operations?
4. What happens if array shapes mismatch?

PRACTICE QUESTIONS
1. Add two arrays of shape (5,)
2. Multiply matrix by scalar
3. Compute square of all elements
"""

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", b / a)
print("Power:", a ** 2)

# Scalar operation
print("Scalar Multiply:", a * 5)
