"""
data_types.py
--------------
Covers:
- NumPy dtypes
- Why dtype matters
- Type casting
- Memory implications

Interview Focus:
- dtype vs Python types
- Why NumPy is faster
"""

import numpy as np

# Default dtype (int64 or int32 depending on system)
arr_int = np.array([1, 2, 3])
print("Array:", arr_int)
print("Dtype:", arr_int.dtype)

# Float dtype
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

# Memory comparison
print("\nMemory (bytes):")
print("int64:", arr_int.nbytes)
print("float32:", arr_float.nbytes)
