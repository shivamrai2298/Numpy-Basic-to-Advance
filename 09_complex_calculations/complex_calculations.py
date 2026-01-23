"""
09_complex_calculations.py
Complex NumPy Calculations – Real-World, Business & Interview-Level Use Cases
"""

import numpy as np

# =========================
# FINANCIAL CALCULATIONS
# =========================
# Monthly revenue from 3 products over 6 months
revenue = np.array([
    [12000, 15000, 18000, 20000, 22000, 25000],
    [8000,  9000,  9500,  11000, 13000, 15000],
    [5000,  7000,  8500,  9000,  10000, 12000]
])

print("Total Revenue:", np.sum(revenue))
print("Revenue per Product:", np.sum(revenue, axis=1))
print("Revenue per Month:", np.sum(revenue, axis=0))

# =========================
# GROWTH RATE CALCULATION
# =========================
# Month-over-month growth
mom_growth = (revenue[:, 1:] - revenue[:, :-1]) / revenue[:, :-1]
print("Month-over-Month Growth:\n", mom_growth)

# =========================
# PROFIT & MARGIN ANALYSIS
# =========================
cost = revenue * 0.65  # 65% cost assumption
profit = revenue - cost
profit_margin = profit / revenue

print("Profit:\n", profit)
print("Profit Margin:\n", profit_margin)

# =========================
# RISK & VARIANCE ANALYSIS
# =========================
# Variability in revenue
variance = np.var(revenue, axis=1)
std_dev = np.std(revenue, axis=1)

print("Revenue Variance:", variance)
print("Revenue Std Dev:", std_dev)

# =========================
# WEIGHTED SCORE MODEL
# =========================
# Product performance scoring
scores = np.array([[80, 75, 90],
                   [70, 85, 88],
                   [60, 65, 70]])
weights = np.array([0.4, 0.35, 0.25])

weighted_score = scores @ weights
print("Weighted Performance Score:", weighted_score)

# =========================
# NORMALIZATION & SCALING
# =========================
mean = np.mean(revenue, axis=1, keepdims=True)
std = np.std(revenue, axis=1, keepdims=True)

z_score = (revenue - mean) / std
print("Z-Score Normalized Revenue:\n", z_score)

# =========================
# CONDITIONAL COMPLEX LOGIC
# =========================
# Flag months where revenue exceeds average
flags = revenue > np.mean(revenue, axis=1, keepdims=True)
print("Above Average Flags:\n", flags)

# =========================
# INTERVIEW QUESTIONS
# =========================
"""
1. Why is axis handling critical in business calculations?
2. Difference between variance and standard deviation?
3. When should weighted averages be used?
4. How does NumPy avoid loops in complex calculations?
5. Explain numerical stability in financial computations.
"""

# =========================
# PRACTICE QUESTIONS
# =========================
"""
1. Calculate CAGR using NumPy.
2. Detect outliers using z-score.
3. Compute rolling average without loops.
4. Build a customer lifetime value (CLV) model.
5. Simulate profit under different cost assumptions.
"""

# =========================
# MINI EXERCISE – CLV SIMULATION
# =========================
monthly_spend = np.array([500, 700, 900, 1100])
retention_rate = 0.85
months = np.arange(1, 13)

clv = np.sum(monthly_spend.mean() * (retention_rate ** months))
print("Estimated Customer Lifetime Value:", clv)
