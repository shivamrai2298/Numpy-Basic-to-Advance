"""
boolean_masking.py
===================
TOPICS COVERED
- Boolean masks
- Conditional filtering
- Vectorized filtering

INTERVIEW QUESTIONS
1. What is boolean masking?
2. Why is boolean masking faster than loops?
3. Difference between mask and fancy indexing?
4. Can boolean masking modify data?

PRACTICE QUESTIONS
1. Filter values above mean
2. Replace negative values with zero
3. Count values satisfying condition
"""

import numpy as np

arr = np.array([10, 20, -5, 30, -2, 40])

mask = arr > 0
print("Mask:", mask)
print("Positive Values:", arr[mask])

# Modify using mask
arr[arr < 0] = 0
print("After Replacement:", arr)
