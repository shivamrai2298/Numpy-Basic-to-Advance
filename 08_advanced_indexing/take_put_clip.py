"""
take_put_clip.py
=================
TOPICS COVERED
- np.take
- np.put
- np.clip

INTERVIEW QUESTIONS
1. What is np.take?
2. Difference between take and fancy indexing?
3. What does np.clip do?
4. Real-world use cases of clip?

PRACTICE QUESTIONS
1. Limit values within range
2. Replace elements at given indices
3. Apply clipping on noisy data
"""

import numpy as np

arr = np.array([5, 15, 25, 35, 45])

# take
taken = np.take(arr, [0, 2, 4])
print("Taken Elements:", taken)

# put
np.put(arr, [1, 3], [100, 200])
print("After Put:", arr)

# clip
clipped = np.clip(arr, 10, 50)
print("Clipped Array:", clipped)
