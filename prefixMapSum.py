class PrefixMapSum:
    def __init__(self) -> None:
        self.__values = {}

    def insert(self, key: str, value: int) -> None:
        self.__values[key] = value

    def sum(self, prefix: str) -> int:
        total = 0

        for key, val in self.__values.items():
            if key[:len(prefix)] == prefix:
                total += val

        return total

    def __eq__(self, value: object) -> bool:
        return value == self.__values

def test_class_init() -> None:
    tMap = PrefixMapSum()
    assert tMap == {}

def test_class_insert() -> None:
    tMap = PrefixMapSum()
    tMap.insert("columnar", 3)
    assert tMap == {"columnar": 3}

def test_class_sum_one_value() -> None:
    tMap = PrefixMapSum()
    tMap.insert("columnar", 3)
    assert tMap.sum("col") == 3

def test_class_sum_two_values() -> None:
    tMap = PrefixMapSum()
    tMap.insert("columnar", 3)
    tMap.insert("column", 2)
    assert tMap.sum("col") == 5
