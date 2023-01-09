import numpy as np

def ff(start, stop, n):
  return np.array([f'{start + x * (stop - start) / n:.3f}' for x in range(1, n)])

sta = int(input())
sto = int(input())
nn = int(input())



