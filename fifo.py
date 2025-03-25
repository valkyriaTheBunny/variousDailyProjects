import pytest

class Queue:
    def __init__(self) -> None:
        self._queue1 = []
        self._queue2 = []

    def enqueue(self, item: any):
        self._queue1.append(item)

    def dequeue(self) -> any:
        if not self._queue1 and not self._queue2:
            raise IndexError('Queue is empty')
        if not self._queue2:
            while self._queue1:
                self._queue2.append(self._queue1.pop())
        return self._queue2.pop()
    
    def __str__(self) -> str:
        return f'Stack 1: {self._queue1}, Stack 2: {self._queue2}'

    def __repr__(self) -> str:
        return f'Stack 1: {self._queue1}, Stack 2: {self._queue2}'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, list):
            return self._queue1 + self._queue2 == other
        elif isinstance(other, Queue):
            return self._queue1 + self._queue2 == other._queue1 + other._queue2
        return False

@pytest.fixture
def myQueue():
    tQueue = Queue()    
    return tQueue 

@pytest.fixture
def preQueued():
    tQueue = Queue()
    tQueue.enqueue(0)
    return tQueue

def test_enqueue(myQueue):
    myQueue.enqueue(0)
    assert myQueue == [0]

def test_dequeue(preQueued):
    preQueued.dequeue()
    assert preQueued == []

def test_return(preQueued):
    assert preQueued.dequeue() == 0