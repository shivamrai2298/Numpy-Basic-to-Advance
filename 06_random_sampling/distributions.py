"""
distributions.py
=================
TOPICS COVERED
- Common probability distributions
- Normal, Binomial, Poisson

INTERVIEW QUESTIONS
1. When is binomial distribution used?
2. Difference between binomial and poisson?
3. Where is normal distribution used in ML?
4. What does lambda represent in Poisson?

PRACTICE QUESTIONS
1. Simulate coin toss using binomial
2. Generate Poisson distributed data
3. Compare mean of distributions
"""

import numpy as np

# Normal distribution
normal = np.random.normal(loc=50, scale=10, size=1000)

# Binomial distribution
binomial = np.random.binomial(n=10, p=0.5, size=1000)

# Poisson distribution
poisson = np.random.poisson(lam=5, size=1000)

print("Normal Mean:", np.mean(normal))
print("Binomial Mean:", np.mean(binomial))
print("Poisson Mean:", np.mean(poisson))
