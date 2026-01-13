"""
eigen_values_vectors.py
=======================
TOPICS COVERED
- Eigenvalues
- Eigenvectors
- Geometric interpretation
- PCA foundation

INTERVIEW QUESTIONS
1. What is an eigenvalue?
2. Why are eigenvectors important in ML?
3. What does PCA use eigenvalues for?
4. Can eigenvalues be complex?

PRACTICE QUESTIONS
1. Verify A * v = λ * v
2. Sort eigenvalues in descending order
3. Interpret eigenvector direction
"""

import numpy as np

A = np.array([[2, 1], [1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

# Verification
v = eigenvectors[:, 0]
lambda_val = eigenvalues[0]

print("\nA*v:", A @ v)
print("λ*v:", lambda_val * v)
