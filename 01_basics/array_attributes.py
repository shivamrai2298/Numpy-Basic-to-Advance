"""
array_attributes.py
====================
TOPICS COVERED
- shape
- ndim
- size
- itemsize
- nbytes

INTERVIEW QUESTIONS
1. Difference between shape and size?
2. What does ndim represent?
3. How is nbytes calculated?
4. Does reshape change memory?
5. How does NumPy calculate memory usage?

PRACTICE QUESTIONS
1. Create a 3D array and print all attributes
2. Manually calculate memory using formula
3. Reshape a (4,3) array into (2,6)
"""

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Array:\n", arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Total Elements:", arr.size)
print("Item Size (bytes):", arr.itemsize)
print("Total Memory (bytes):", arr.nbytes)

# Reshape example
reshaped = arr.reshape(3, 2)
print("\nReshaped Array:\n", reshaped)
print("New Shape:", reshaped.shape)
