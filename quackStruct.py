class Quack:
    def __init__(self):
        self.__left = []
        self.__right = []
        self.__temp = []

    def push(self, val: any) -> None:
        self.__left.append(val)

    def pop(self) -> any:
        if not self.__left:
            self.__rebalance(self.__right, self.__left)
        if self.__left:
            return self.__left.pop()
        raise IndexError()

    def pull(self) -> any:
        if not self.__right:
            self.__rebalance(self.__left, self.__right)
        if self.__right:
            return self.__right.pop()
        raise IndexError()

    def __rebalance(self, src: list[any], dest: list[any]) -> None:
        if not src:
            return
        n = len(src)
        for _ in range(n // 2):
            self.__temp.append(src.pop())
        while src:
            dest.append(src.pop())
        while self.__temp:
            src.append(self.__temp.pop())

q = Quack()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pull())
print(q.pop())
