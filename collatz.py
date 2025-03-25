def collatzSeq(num: int) -> tuple[int, int]:
    newNum = int(num)
    count = 0
    try:
        while newNum != 1:
            if newNum % 2 == 0:
                newNum = int(newNum / 2)
            elif newNum % 2 == 1:
                newNum = int(3 * newNum + 1)
            count += 1
        return (newNum, count)
    except Exception as e:
        print(e)

def main():
    max = float('-inf')
    maxI = 0
    for i in range(2, 1000001):
        if collatzSeq(i)[1] > max:
            max = collatzSeq(i)[1]
            maxI = i
        print(f"Result: {collatzSeq(i)[0]}, Loops: {collatzSeq(i)[1]}")
    print(f"Number resulting in max runs: {maxI}, Max runs: {max}")

if __name__ == '__main__':
    main()
