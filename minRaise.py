def minRaiseCalc(employeeCodeLines: list[int]) -> list[int]:
    length = len(employeeCodeLines)
    minRaises = [1] * length

    for i in range(1, length):
        if employeeCodeLines[i] > employeeCodeLines[i - 1]:
            minRaises[i] = minRaises[i - 1] + 1

    for i in range(length - 2, -1, -1):
        if employeeCodeLines[i] > employeeCodeLines[i + 1]:
            minRaises[i] = max(minRaises[i], minRaises[i + 1] + 1)

    return minRaises

def test_minRaiseCalc() -> None:
    assert minRaiseCalc([10, 40, 200, 1000, 60, 30]) == [1, 2, 3, 4, 2, 1]


def main() -> None:
    print(minRaiseCalc([10, 40, 200, 1000, 60, 30]))

if __name__ == "__main__":
    main()
