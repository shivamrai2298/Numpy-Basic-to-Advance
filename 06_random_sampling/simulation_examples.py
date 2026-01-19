"""
simulation_examples.py
=======================
TOPICS COVERED
- Real-world simulations
- Law of large numbers
- Expected value

INTERVIEW QUESTIONS
1. What is a simulation?
2. What is law of large numbers?
3. Why are simulations useful?
4. Where are simulations used in business?

PRACTICE QUESTIONS
1. Simulate dice rolls
2. Estimate probability of event
3. Increase sample size and observe stability
"""

import numpy as np

# Dice roll simulation
dice_rolls = np.random.randint(1, 7, size=10000)

# Probability of rolling a 6
prob_six = np.mean(dice_rolls == 6)

print("Probability of rolling 6:", prob_six)
