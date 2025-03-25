def multiplyItems(numLst: list[int]) -> list[int]:
    rtnLst = [1] * len(numLst)
    for i in range(len(rtnLst)):
        for j in range(len(numLst)):
            if i != j:
                rtnLst[i] *= numLst[j]
    return rtnLst

def runner() -> None:
    lstLst = [[1, 2, 3, 4, 5], [3, 2, 1]]
    ansLst = [[120, 60, 40, 30, 24], [2, 3, 6]]

    for i in range(len(lstLst)):
        ans = ansLst[i]
        tAns = multiplyItems(lstLst[i])
        print(f'Numbers to multiply: {lstLst[i]}, Test answer: {tAns}, Actual answer: {ans}')

runner()