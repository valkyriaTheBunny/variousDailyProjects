import itertools

def genSeq(start: int, entries: int) -> list[int]:
    seq = []

    x = str(start)
    for _ in range(entries):
        seq.append(int(x))
        x = ''.join(str(len(list(g)))+k for k, g in itertools.groupby(x))

    return seq

def getSeqAtPos(pos: int) -> int:
    return genSeq(1, pos)[-1]

def test_getSeq():
    assert getSeqAtPos(4) == 1211
