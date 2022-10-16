import numpy as np

start = int(input())
stop = int(input())
n = int(input())

print(np.array([f'{start + x * (stop - start) / n:.3f}' for x in range(1, n)]))


