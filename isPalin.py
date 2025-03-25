def is_palindrome(num):
    if num < 0:
        return False

    original_num = num
    reversed_num = 0

    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10

    return original_num == reversed_num

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(888) == True
    assert is_palindrome(678) == False
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False
