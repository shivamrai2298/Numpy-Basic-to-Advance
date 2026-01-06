"""
data_types.py
================
TOPICS COVERED
- NumPy dtypes
- Fixed-size memory
- Type casting
- Memory efficiency

INTERVIEW QUESTIONS
1. What is dtype in NumPy?
2. Why does NumPy use fixed-size data types?
3. Difference between float32 and float64?
4. Why is NumPy faster than Python lists?
5. How does dtype affect memory and performance?

PRACTICE QUESTIONS
1. Create an array of 100 zeros with dtype int8
2. Convert a float array to integers
3. Compare memory usage of int32 vs int64
"""

import numpy as np

# Default dtype
arr_int = np.array([1, 2, 3])
print("Array:", arr_int)
print("Dtype:", arr_int.dtype)

# Explicit float dtype
arr_float = np.array([1, 2, 3], dtype=np.float32)
print("\nFloat Array:", arr_float)
print("Dtype:", arr_float.dtype)

# Boolean dtype
arr_bool = np.array([True, False, True])
print("\nBoolean Array:", arr_bool)
print("Dtype:", arr_bool.dtype)

# String dtype
arr_str = np.array(["apple", "banana", "cherry"])
print("\nString Array:", arr_str)
print("Dtype:", arr_str.dtype)

# Type casting
arr_cast = arr_int.astype(np.float64)
print("\nCasted Array:", arr_cast)
print("New Dtype:", arr_cast.dtype)

# Memory usage
print("\nMemory Usage (bytes)")
print("int64:", arr_int.nbytes)
print("float32:", arr_float.nbytes)
