"""
loops_vs_vectorization.py
==========================
TOPICS COVERED
- Python loops vs NumPy vectorization
- Performance comparison
- Why NumPy is faster

INTERVIEW QUESTIONS
1. Why are NumPy operations faster than Python loops?
2. What is vectorization?
3. How does C backend help NumPy?
4. When are loops unavoidable?

PRACTICE QUESTIONS
1. Compute square using loop and vectorization
2. Time both approaches
3. Increase data size and observe difference
"""

import numpy as np
import time

size = 1_000_000
arr = np.random.rand(size)

# Python loop
start = time.time()
result_loop = []
for x in arr:
    result_loop.append(x * x)
print("Loop Time:", time.time() - start)

# NumPy vectorization
start = time.time()
result_vec = arr * arr
print("Vectorized Time:", time.time() - start)
