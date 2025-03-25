class Queue:
    __inQueue = []
    __outQueue = []

    def __init__(self):
        pass

    def enqueue(self, obj: any) -> None:
        self.__inQueue.append(obj)
        self.__merger("in")

    def dequeue(self) -> any:
        obj = self.__outQueue.pop()
        self.__merger("out")
        return obj

    def __merger(self, caller: str) -> None:
        if caller == "in":
            self.__outQueue = self.__inQueue.copy()
        if caller == "out":
            self.__inQueue = self.__outQueue.copy()

def testQueue():
    tQueue = Queue()
    tQueue.enqueue("t")
    assert "t" == tQueue.dequeue()
