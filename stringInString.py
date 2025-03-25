from typing import Union

def finder(text: str, pattern: str) -> Union[bool, int]:
    n = len(text)
    k = len(pattern)

    lps = [0] * k
    j = 0

    for i in range(1, k):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        lps[i] = j

    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == k:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False

def test_finder():
    assert finder("this", "is") == 2
