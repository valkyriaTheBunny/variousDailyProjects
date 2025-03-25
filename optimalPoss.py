def findOptimalPossition(num_ppl: int, start: int) -> int:
    last_visited = 0

    for i in range(2, num_ppl + 1):
        last_visited = (last_visited + start) % i

    return last_visited + 1

def test_optPoss():
    assert findOptimalPossition(5, 2) == 3
