from copy import deepcopy as dpc
from copy import copy

def permutation(originArray: list[any], permutationArrray: list[int]) -> list[any]:
    tempArr = dpc(originArray)
    tempPerms = copy(permutationArrray)

    for i, index in enumerate(tempPerms):
        temp = tempArr[index]
        tempArr[index] = tempArr[i]
        tempArr[i] = temp
        del tempPerms[index]

    return tempArr

def testPerm():
    origin = ["a", "b", "c"]
    indices = [2, 1, 0]
    assert permutation(origin, indices) == ["c", "b", "a"]
