"""
load_txt_csv.py
================
TOPICS COVERED
- Loading TXT and CSV files using NumPy
- delimiter, skiprows, usecols
- Handling missing values

INTERVIEW QUESTIONS
1. How is NumPy different from Pandas for CSV loading?
2. What happens if data types are inconsistent?
3. What is the use of delimiter?
4. How does NumPy handle missing values?
5. When should you avoid using NumPy for CSV loading?

PRACTICE QUESTIONS
1. Load only 2 columns from a CSV
2. Skip header row while loading data
3. Replace missing values with column mean
"""

import numpy as np

# Sample CSV simulation using StringIO
from io import StringIO

data = StringIO("""
id,age,salary
1,25,50000
2,30,60000
3,,55000
4,28,58000
""")

# Load CSV
arr = np.genfromtxt(
    data,
    delimiter=",",
    skip_header=1,
    filling_values=np.nan
)

print("Loaded Data:\n", arr)
print("Dtype:", arr.dtype)
