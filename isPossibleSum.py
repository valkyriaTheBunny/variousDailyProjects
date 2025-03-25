from itertools import combinations

def isPossibleSum(numList: list, k: int) -> bool:
    sumList = [sum(comb) for comb in combinations(numList, 2)]
    return k in sumList

def main() -> None:
    numsList = [[10, 15, 3, 7], [5, 9, 12, 20, 7, 19, 6, 3], [7, 15, 9, 24, 10, 1, 50, 22, 11], 
                [13, 49, 34, 6, 56, 3, 7, 11, 90, 8, 4], [12, 13, 4, 67, 21, 39, 5, 45, 3, 2, 7, 9, 28, 32, 15],
                [9, 17, 32, 84, 3, 65, 57, 8, 23, 25, 40, 2, 7, 10, 43, 78, 4, 49, 11, 15]]
    sumsList = [17, 39, 49, 139, 60, 72]

    for i in range(len(numsList)):
        lst = numsList[i]
        e = sumsList[i]
        print(f'Number list: {lst}, Sum: {e}, Is the sum possible: {isPossibleSum(lst, e)}')

if __name__ == "__main__":
    main()