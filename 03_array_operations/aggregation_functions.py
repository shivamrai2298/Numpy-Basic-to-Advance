"""
aggregation_functions.py
=========================
TOPICS COVERED
- sum, mean, std, var
- min, max
- axis parameter
- nan-safe aggregations

INTERVIEW QUESTIONS
1. Difference between mean and nanmean?
2. What does axis=0 vs axis=1 mean?
3. Why are aggregations vectorized?
4. How does NumPy handle NaN in sum?

PRACTICE QUESTIONS
1. Calculate column-wise mean
2. Find row with max sum
3. Normalize data using mean and std
"""

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, np.nan]
])

print("Sum:", np.sum(data))
print("Mean (NaN included):", np.mean(data))
print("Mean (NaN ignored):", np.nanmean(data))

print("\nColumn-wise Sum:", np.nansum(data, axis=0))
print("Row-wise Mean:", np.nanmean(data, axis=1))
