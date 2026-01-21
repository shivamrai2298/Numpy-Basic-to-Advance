"""
fancy_indexing.py
==================
TOPICS COVERED
- Fancy indexing using index arrays
- Non-contiguous selection
- Copy vs view behavior

INTERVIEW QUESTIONS
1. What is fancy indexing?
2. Does fancy indexing return a view or copy?
3. Difference between slicing and fancy indexing?
4. When is fancy indexing useful?

PRACTICE QUESTIONS
1. Select alternate rows using index list
2. Reorder array using index array
3. Modify selected elements
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

indices = [0, 2, 4]
selected = arr[indices]

print("Selected Elements:", selected)

# Modification does NOT affect original
selected[0] = 999
print("Modified Selected:", selected)
print("Original Array:", arr)
