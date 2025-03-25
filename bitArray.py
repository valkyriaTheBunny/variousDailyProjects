class BitArray:
    def __init__(self, size: int) -> None:
        self.array = [None] * size

    def set(self, i: int, val: int) -> None:
        if val != 0 and val != 1:
            raise ValueError
        self.array[i] = val

    def get(self, i: int) -> int:
        return self.array[i]
