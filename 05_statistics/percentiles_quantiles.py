"""
percentiles_quantiles.py
=========================
TOPICS COVERED
- Percentiles
- Quantiles
- IQR (Interquartile Range)

INTERVIEW QUESTIONS
1. Difference between percentile and quantile?
2. What is IQR?
3. Why is IQR robust to outliers?
4. How are percentiles used in salary analysis?

PRACTICE QUESTIONS
1. Compute 25th, 50th, 75th percentiles
2. Detect outliers using IQR
3. Compare percentile vs mean
"""

import numpy as np

data = np.array([10, 12, 15, 18, 20, 22, 100])

p25, p50, p75 = np.percentile(data, [25, 50, 75])
iqr = p75 - p25

print("25th percentile:", p25)
print("50th percentile (median):", p50)
print("75th percentile:", p75)
print("IQR:", iqr)
