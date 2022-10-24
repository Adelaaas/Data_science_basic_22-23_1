import random
import numpy as np

def ff():
    count_maximums = 0
    arr = np.array([random.randint(1, 20) for x in range(10)])

    for i in range(len(arr)):
        if i == 0:
            if arr[i] > arr[i + 1]:
                print(arr[i])
                count_maximums += 1

        if i > 0 and i < len(arr) - 1:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                print(arr[i])
                count_maximums += 1

        if i == len(arr):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                print(arr[i])
                count_maximums += 1

    return count_maximums

