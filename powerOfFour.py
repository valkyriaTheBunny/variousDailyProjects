from random import randint
import big_o
def isPowerOfFour(n: int) -> bool:
    return (n > 0) and ((n & (n - 1)) == 0) and ((n & 0x55555555) != 0)

def test_isPowerOfFour():
    assert isPowerOfFour(1024) == True

def main():
    def positive_int_generator(num):
        return randint(1, 10000)

    best = big_o.big_o(isPowerOfFour, positive_int_generator, n_repeats=1000)[0]
    print(best)

if __name__ == "__main__":
    main()
