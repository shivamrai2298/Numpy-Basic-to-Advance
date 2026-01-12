"""
comparison_boolean_ops.py
==========================
TOPICS COVERED
- Comparison operators
- Boolean arrays
- Logical operations
- Filtering data

INTERVIEW QUESTIONS
1. What is a boolean mask?
2. Difference between & and and?
3. How does NumPy filter data?
4. Why can't we use Python 'and'?

PRACTICE QUESTIONS
1. Filter values greater than mean
2. Replace values less than threshold
3. Count elements satisfying condition
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

mask = arr > 30
print("Mask:", mask)
print("Filtered:", arr[mask])

# Multiple conditions
condition = (arr > 20) & (arr < 50)
print("Between 20 and 50:", arr[condition])

# Replace values
arr[arr < 30] = 0
print("After Replacement:", arr)
