"""
performance_timing.py
======================
TOPICS COVERED
- Time measurement
- np.vectorize vs true vectorization
- Performance pitfalls

INTERVIEW QUESTIONS
1. Is np.vectorize actually vectorized?
2. Why is broadcasting faster?
3. How do cache and SIMD help NumPy?
4. Common performance mistakes?

PRACTICE QUESTIONS
1. Compare np.vectorize vs pure NumPy
2. Try broadcasting instead of loops
3. Optimize slow code
"""

import numpy as np
import time

def python_func(x):
    return x ** 2 + 2 * x + 1

arr = np.random.rand(1_000_000)

# np.vectorize (NOT true vectorization)
vec_func = np.vectorize(python_func)

start = time.time()
vec_func(arr)
print("np.vectorize Time:", time.time() - start)

# True vectorization
start = time.time()
arr ** 2 + 2 * arr + 1
print("True Vectorized Time:", time.time() - start)
