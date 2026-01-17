"""
descriptive_stats.py
=====================
TOPICS COVERED
- Mean, median, mode
- Variance, standard deviation
- Outlier intuition

INTERVIEW QUESTIONS
1. Difference between mean and median?
2. Why is standard deviation preferred over variance?
3. How do outliers affect mean and median?
4. When should you use median instead of mean?

PRACTICE QUESTIONS
1. Compute stats for skewed data
2. Identify which measure is robust to outliers
3. Compare population vs sample std
"""

import numpy as np

data = np.array([10, 12, 15, 18, 100])  # outlier present

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))
