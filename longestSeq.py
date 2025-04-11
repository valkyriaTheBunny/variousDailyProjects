from random import randint
import big_o

def calcLongestSeq(nums: list[int]) -> int:
    count = 0
    gCount = 0
    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1] + 1:
            count += 1
        else:
            if count > gCount:
                gCount = count
            count = 0

    return gCount

def test_calc():
    assert calcLongestSeq([1, 4, 3, 7, 8, 9, 10, 18, 20, 1]) == 6

def main():
    def positive_int_generator(num):
        return [randint(1, 9000) for _ in range(num)]

    best = big_o.big_o(calcLongestSeq, positive_int_generator, n_repeats=50)[0]
    print(best)

if __name__ == "__main__":
    main()
