def reverseOrder(entry: str) -> str:
    return ' '.join(entry.split(' ')[::-1])


def test_reverse():
    assert reverseOrder('hello world here') == 'here world hello'
