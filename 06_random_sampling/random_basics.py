"""
random_basics.py
=================
TOPICS COVERED
- Random number generation
- Uniform vs normal distribution
- Reproducibility using seed

INTERVIEW QUESTIONS
1. Why do we use random seed?
2. Difference between uniform and normal distribution?
3. Is NumPy random truly random?
4. Why is reproducibility important in ML?

PRACTICE QUESTIONS
1. Generate 100 random numbers between 0 and 1
2. Generate random integers between 10 and 50
3. Reproduce same random output using seed
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Uniform distribution
uniform_random = np.random.rand(5)
print("Uniform Random:", uniform_random)

# Normal distribution
normal_random = np.random.randn(5)
print("Normal Random:", normal_random)

# Random integers
rand_int = np.random.randint(10, 50, size=5)
print("Random Integers:", rand_int)
