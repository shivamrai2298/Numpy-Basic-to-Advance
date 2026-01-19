"""
monte_carlo_intro.py
=====================
TOPICS COVERED
- Monte Carlo simulation
- Estimation using randomness
- Pi estimation

INTERVIEW QUESTIONS
1. What is Monte Carlo simulation?
2. Why does it work?
3. Where is Monte Carlo used?
4. Trade-off between accuracy and computation?

PRACTICE QUESTIONS
1. Estimate Pi using random sampling
2. Increase iterations and observe accuracy
3. Simulate random walk
"""

import numpy as np

# Monte Carlo estimation of Pi
num_samples = 100000

x = np.random.rand(num_samples)
y = np.random.rand(num_samples)

inside_circle = (x**2 + y**2) <= 1
pi_estimate = 4 * np.mean(inside_circle)

print("Estimated Pi:", pi_estimate)
