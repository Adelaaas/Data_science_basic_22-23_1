#Задача 10.


#Дан двумерный массив. Найти все различные строки.
import numpy as np
a = np.array([[1, 2], [1, 2], [5, 6]], float)

print( np.unique(a, axis=0))