def findNearestSparseInt(num: int) -> int:
    binary = format(num, 'b')
    isSparse = True

    for i in range(1, len(binary)):
        prevChar = binary[i - 1]
        currChar = binary[i]

        if int(prevChar) == 1 and int(currChar) == 1:
            isSparse = False
            break

    if isSparse:
        return num
    else:
        return findNearestSparseInt(num + 1)

print(findNearestSparseInt(22))
