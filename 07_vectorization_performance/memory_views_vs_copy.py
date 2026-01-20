"""
memory_views_vs_copy.py
=======================
TOPICS COVERED
- Views vs copies
- Memory sharing
- Performance impact

INTERVIEW QUESTIONS
1. What is a NumPy view?
2. How do you check if memory is shared?
3. Why are views faster?
4. When should you force a copy?

PRACTICE QUESTIONS
1. Modify view and observe original
2. Compare ravel vs flatten
3. Detect memory sharing
"""

import numpy as np

arr = np.arange(10)

# View
view = arr[2:6]
view[0] = 999

print("View:", view)
print("Original after view change:", arr)

# Copy
copy = arr[2:6].copy()
copy[0] = 111

print("\nCopy:", copy)
print("Original after copy change:", arr)

# Memory check
print("\nView shares memory:", np.shares_memory(arr, view))
print("Copy shares memory:", np.shares_memory(arr, copy))
