import numpy as np

def ff():
  maxtrix_1 = np.array([[3, 5],
                        [2, 1]])
  maxtrix_2 = np.array([[8, 2, 3], # На эту матрицу умножаем
                        [1, 7, 2]])
  result_maxtrix = np.zeros(shape = (2, 3))

  value = 0
  for i in range(2):
      for j in range(3):
          for k in range(2):
              value += maxtrix_1[i][k] * maxtrix_2[k][j]
          result_maxtrix[i][j] = value
          value = 0

  return result_maxtrix

