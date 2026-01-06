"""
reshaping_basics.py
====================
TOPICS COVERED
- reshape
- flatten vs ravel
- transpose
- expand_dims

INTERVIEW QUESTIONS
1. Difference between reshape, flatten, and ravel?
2. When does reshape fail?
3. Why is transpose cheap in NumPy?
4. How is reshape used in ML pipelines?
5. Difference between row vector and column vector?

PRACTICE QUESTIONS
1. Convert 1D array into column vector
2. Flatten a 3D array
3. Swap axes of a matrix
"""

import numpy as np

arr = np.arange(12)
print("Original Array:", arr)

# Reshape
reshaped = arr.reshape(3, 4)
print("\nReshaped (3x4):\n", reshaped)

# Flatten (creates copy)
flat_copy = reshaped.flatten()
flat_copy[0] = 999
print("\nFlattened Copy:", flat_copy)
print("Original after flatten:\n", reshaped)

# Ravel (view)
flat_view = reshaped.ravel()
flat_view[0] = 555
print("\nRavel View:", flat_view)
print("Original after ravel:\n", reshaped)

# Transpose
print("\nTransposed:\n", reshaped.T)

# Expand dimensions
expanded = np.expand_dims(arr, axis=0)
print("\nExpanded Shape:", expanded.shape)
