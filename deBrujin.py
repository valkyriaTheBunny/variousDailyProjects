def constDeBrujinSeq(k, n):
    a = [0] * n * k
    sequence = []

    def db(t, p):
        if t > k:
            if k % p == 0:
                sequence.extend(a[1:p+1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, n):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return ''.join(str(x) for x in sequence) + ''.join(str(x) for x in sequence[:k-1])

def main() -> None:
    print(constDeBrujinSeq(3, 2))

if __name__ == "__main__":
    main()
