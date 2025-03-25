def nextInt(num: int) -> int:
    strNum = '{0:08b}'.format(num)
    cntOnes = 0

    for let in strNum:
        if let == '1':
            cntOnes += 1

    num2 = num
    while True:
        num2 += 1
        strNum2 = '{0:08b}'.format(num2)
        secondCnt = 0

        for let in strNum2:
            if let == '1':
                secondCnt += 1

        if secondCnt == cntOnes:
            return num2

def test_nextInt():
    assert nextInt(6) == 9
