"""
load_json_like.py
==================
TOPICS COVERED
- Loading structured data (JSON-like)
- NumPy structured arrays
- Named columns

INTERVIEW QUESTIONS
1. What is a structured array?
2. When should you use structured arrays?
3. Difference between structured array and Pandas DataFrame?
4. Are structured arrays memory efficient?

PRACTICE QUESTIONS
1. Access only salary column
2. Filter rows with salary > 55000
3. Convert structured array to normal ndarray
"""

import numpy as np

data = [
    (1, 25, 50000),
    (2, 30, 60000),
    (3, 28, 58000)
]

dtype = [('id', 'i4'), ('age', 'i4'), ('salary', 'f4')]

arr = np.array(data, dtype=dtype)

print("Structured Array:\n", arr)
print("Salaries:", arr['salary'])
