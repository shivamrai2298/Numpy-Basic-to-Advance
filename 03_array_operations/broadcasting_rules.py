"""
broadcasting_rules.py
======================
TOPICS COVERED
- Broadcasting concept
- Shape alignment
- Row vs column broadcasting

INTERVIEW QUESTIONS
1. What is broadcasting in NumPy?
2. What are the broadcasting rules?
3. When does broadcasting fail?
4. Why is broadcasting memory efficient?

PRACTICE QUESTIONS
1. Add a 1D array to a 2D array
2. Normalize each row using broadcasting
3. Subtract column mean from matrix
"""

import numpy as np

# 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# 1D array
row = np.array([1, 2, 3])

# Broadcasting row-wise
print("Broadcasted Addition:\n", matrix + row)

# Column-wise broadcasting
col = np.array([[1], [2]])
print("\nColumn Broadcasting:\n", matrix + col)
