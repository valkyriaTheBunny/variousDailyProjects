def highestProduct(numList: list[int]) -> int:
    temp = numList.copy()
    temp = sorted(temp)
    
    highThree = temp[-1] * temp[-2] * temp[-3]
    lowTwoHighOne = temp[0] * temp[1] * temp[-1]
    return max(highThree, lowTwoHighOne)

def main():
    print(highestProduct([-5, -2, -1, 0, 1, 1, 5]))
    print(highestProduct([-10, -10, 5, 2]))

if __name__ == "__main__":
    main()