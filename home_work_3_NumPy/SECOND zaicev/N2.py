import random
import numpy as np

def ff(N, M):
    matrix = np.array([[random.randint(1, 20) for x in range(M)] for y in range(N)], dtype = float)
    
    maximum = np.max(matrix)
    minimum = np.min(matrix)
    
    for i in range(N):
        for j in range(M):
            matrix[i][j] = (matrix[i][j] - minimum) / (maximum - minimum)
            
    return matrix
    
N = int(input())
M = int(input())






