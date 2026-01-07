"""
missing_values_handling.py
===========================
TOPICS COVERED
- NaN handling
- isnull / isnan
- Replacing missing values
- Mean imputation

INTERVIEW QUESTIONS
1. Why does NumPy use NaN?
2. Difference between NaN and None?
3. How does NaN affect calculations?
4. Why is mean imputation risky?

PRACTICE QUESTIONS
1. Replace NaN with median
2. Remove rows with NaN
3. Count missing values per column
"""

import numpy as np

data = np.array([
    [25, 50000],
    [30, np.nan],
    [28, 58000],
    [np.nan, 60000]
])

print("Original Data:\n", data)

# Detect missing values
print("\nNaN Mask:\n", np.isnan(data))

# Column mean ignoring NaN
col_mean = np.nanmean(data, axis=0)
print("\nColumn Mean:", col_mean)

# Replace NaN with column mean
inds = np.where(np.isnan(data))
data[inds] = np.take(col_mean, inds[1])

print("\nData after imputation:\n", data)
