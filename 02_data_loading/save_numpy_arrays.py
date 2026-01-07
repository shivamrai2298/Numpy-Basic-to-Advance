"""
save_numpy_arrays.py
=====================
TOPICS COVERED
- Saving NumPy arrays
- .npy vs .npz
- Loading saved arrays

INTERVIEW QUESTIONS
1. Difference between .npy and .npz?
2. Why is .npy faster than CSV?
3. Can NumPy save multiple arrays in one file?
4. Are .npy files human readable?

PRACTICE QUESTIONS
1. Save 2 arrays in a single .npz file
2. Load array and verify shape
3. Compress .npz file
"""

import numpy as np

arr1 = np.arange(10)
arr2 = np.random.rand(5, 3)

# Save single array
np.save("array1.npy", arr1)

# Save multiple arrays
np.savez("arrays.npz", first=arr1, second=arr2)

# Load arrays
loaded = np.load("arrays.npz")

print("Loaded Keys:", loaded.files)
print("First Array:", loaded["first"])
