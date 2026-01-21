"""
where_select.py
================
TOPICS COVERED
- np.where
- Conditional selection
- Ternary operations

INTERVIEW QUESTIONS
1. Difference between np.where and boolean masking?
2. What does np.where return?
3. How is np.where used as ternary operator?
4. When should you prefer np.where?

PRACTICE QUESTIONS
1. Replace values based on condition
2. Find indices where condition is true
3. Categorize data using where
"""

import numpy as np

arr = np.array([10, 25, 40, 15, 5])

# Ternary operation
labels = np.where(arr >= 20, "High", "Low")
print("Labels:", labels)

# Indices
indices = np.where(arr < 10)
print("Indices where arr < 10:", indices)
