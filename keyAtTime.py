import pytest

class Map:
    def __init__(self) -> None:
        self._map: dict[int, list[list[int]]] = {}
        
    def set(self, key: int, time: int, value: int) -> None:
        if key not in self._map:
            self._map[key] = [[time, value]]
        else:
            self._map[key].append([time, value])

    def get(self, key: int, time: int) -> int:
        if not self._map[key]:
            return None
        values = self._map[key]
        print(values)
        for i in range(len(values) - 1, -1, -1):
            if values[i][0] <= time:
                return values[i][1]
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Map):
            return self._map == other._map
        return False
        

@pytest.fixture
def basic_Map() -> Map:
    tMap = Map()
    return tMap

@pytest.fixture
def empty_Map() -> Map:
    eMap = Map
    return eMap

def test_init(basic_Map):
    nMap = Map()
    assert nMap == basic_Map

def test_set(basic_Map, empty_Map):
    bMap = basic_Map
    bMap.set(1, 1, 1)
    assert bMap != empty_Map
    assert bMap._map == {1: [[1, 1]]}

def test_get(basic_Map):
    bMap = basic_Map
    bMap.set(1, 1, 1)
    bMap.set(1, 2, 2)
    assert bMap.get(1, 1) == 1
    assert bMap.get(1, 2) == 2

