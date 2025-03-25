def lowestPositive(lst: list[int]) -> int:
    m = max(lst)

    if m < 1:
        return 1

    if len(lst) == 1:
        if lst[0] == 1:
            return 2
        else:
            return 1

    l = [0] * m

    for i in range(len(lst)):
        if lst[i] > 0:
            if l[lst[i] - 1] != 1:
                l[lst[i] - 1] = 1

    for i in range(len(l)):
        if l[i] == 0:
            return i + 1
    return i + 2

def runner() -> None:
    lstLst = [[3, 4, -1, 1], [1, 2, 0]]
    ansLst = [2, 3]

    for i in range(len(lstLst)):
        print(f'Number list: {lstLst[i]}, Generated answer: {lowestPositive(lstLst[i])}, True answer: {ansLst[i]}')

runner()
