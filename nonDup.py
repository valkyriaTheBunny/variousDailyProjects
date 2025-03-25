from big_o import big_o
import numpy as np

def findNonDuplicatedElement(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    seen = [0] * (max(arr) + 1)
    for index, num in enumerate(arr):
        seen[num] += 1
    return seen.index(1)

data = [[0], [6, 1, 3, 3, 3, 6, 6], [0, 0, 9,  4, 9, 13, 13, 4, 12], [13, 19, 13, 13], 
        [1, 2, 2, 4, 5, 6, 1, 2, 5, 6, 7, 9, 7], [20, 3, 20, 1, 3, 4, 1], 
        [9, 1, 3, 2, 2, 3, 1, 13, 13], [6, 5, 4, 6, 1, 4, 3, 5], 
        [3, 3, 4, 4, 5, 3, 4, 6, 6], [13, 12, 13, 5, 12, 5, 6], 
        [8, 8, 9, 4, 4, 7, 7, 16, 16], [6, 7, 6, 8, 7], 
        [10, 10, 10, 12, 12, 11, 14, 14, 13, 11, 20, 20],
        [10, 10, 3, 3, 5, 10, 9, 5], [5, 6, 5, 4, 6], [9, 9, 8, 7, 9, 7], 
        [0], [2, 2, 1, 4, 1, 4, 1, 5, 6, 5, 5, 1, 6, 7], [10, 13, 13, 10, 9, 8, 9],
        [54, 54, 54, 34, 32, 32, 1, 34, 1, 5], 
        [5, 5, 5, 4, 5, 4, 3, 2, 2, 7, 5, 7, 6, 6]]

def dataGrab(n):
    try:
        return data[n]
    except IndexError:
        raise ValueError(f"Index out of bounds: {n}")

result = big_o(findNonDuplicatedElement, dataGrab, min_n=1, max_n=len(data) - 1)[0]
print(result)
