def encode(aStr: str) -> str:
    nStr = ''
    lst = list(aStr)
    cnt = 1
    for i in range(len(lst)):
        if i != 0:
            if lst[i] == lst[i - 1]:
                cnt += 1
            else:
                nStr += str(cnt) + lst[i - 1]
                cnt = 1
        if i == len(lst) - 1:
            nStr += str(cnt) + lst[i - 1]
    return nStr

def decode(aStr: str) -> str:
    nStr = ''
    lst = list(aStr)
    for i in range(len(lst)):
        try:
            n = int(lst[i])
            while n != 0:
                n -= 1
                nStr += lst[i + 1]
        except:
            pass
    return nStr

def test_encode():
    assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"

def test_decode():
    assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"