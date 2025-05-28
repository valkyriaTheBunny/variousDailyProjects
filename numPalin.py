#Daily Coding Problem 491
''' Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string. '''

def is_palin(num: int) -> bool:
    if num < 0:
        return False

    og = num
    rev = 0
    while og > 0:
        digit = og % 10
        rev = (rev * 10) +  digit
        og = og // 10

    return rev == num

def test_is_palin():
    assert is_palin(121) == True
    assert is_palin(-121) == False
    assert is_palin(678) == False

def main():
    print(is_palin(121))

if __name__ == "__main__":
    main()
