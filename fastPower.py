def pow2B(x, y):
    if (y < 2):
        return y if y else 1
    if (y & 1):
        return x * pow2B(x, y & 0x7FFFFFFE)
    p = pow2B(x, y >> 1)
    return p * p;
