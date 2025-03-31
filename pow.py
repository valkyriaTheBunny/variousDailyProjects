import big_o
def no_pow(entry) -> int:
    num = entry[0]
    power = entry[1]
    return num ** power

def niave(entry) -> int:
    num = entry[0]
    power = entry[1]

    for _ in range(power):
        num *= num
    return num

def test_no_pow():
    assert no_pow(2, 2) == 4
    assert no_pow(3, 5) == 243

def main():
    lstOfNums = [798, 665, 260, 554, 1001, 778, 850, 11985, 587, 1405, 5408]
    lstOfPows = [62, 56, 78, 50, 89, 45, 100, 53, 69, 88, 132]

    def dataGrab(n: int):
        try:
            return (lstOfNums[n], lstOfPows[n])
        except IndexError:
            raise ValueError(f"Index out of bounds: {n}")

    best = big_o.big_o(no_pow, dataGrab, min_n=1, max_n=len(lstOfNums) - 1, n_repeats=100)[0]
    print(best)

    best1 = big_o.big_o(niave, dataGrab, min_n=1, max_n=len(lstOfNums) - 1, n_repeats=100)[0]
    print(best1)

if __name__ == "__main__":
    main()
