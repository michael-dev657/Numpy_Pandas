import numpy as np # type: ignore
a = np.array([10, 20, 30, 40, 50]) # type: ignore
b = np.array([5, 4, 3, 2, 1]) # type: ignore
print(a + b) # type: ignore
print(a - b) # type: ignore
print(a * b) # type: ignore
print(a / b) # type: ignore
print(a.max())
print(a.min())
print(a.mean())
print(np.dot(a, b)) # type: ignore