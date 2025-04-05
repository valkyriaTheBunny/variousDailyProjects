from __future__ import annotations
class Node:
    def __init__(self, val: any):
        self.__val = val
        self.__next : Node = None

    def getValue(self) -> any:
        return self.__val

    def getNext(self) -> Node:
        return self.__next

    def setNext(self, val: any) -> None:
        if not isinstance(val, Node):
            newNode = Node(val)
            self.__next = newNode
        else:
            self.__next = val

    def __repr__(self):
        currNode = self
        values = []

        while currNode:
            values.append(currNode.getValue())
            currNode = currNode.getNext()

        nValues = [0] * len(values)
        for i in range(len(values)):
            k = len(values) - i - 1
            nValues[i] = str(values[k])
        return ''.join(nValues)

    def __str__(self):
        currNode = self
        values = []

        while currNode:
            values.append(currNode.getValue())
            currNode = currNode.getNext()

        nValues = [0] * len(values)
        for i in range(len(values)):
            k = len(values) - i - 1
            nValues[i] = str(values[k])
        return ''.join(nValues)

    def __eq__(self, value: Node):
        if not isinstance(value, Node):
            return False
        return int(self.__repr__()) == int(value.__repr__())

def sumLinkedLists(linkedList0: Node[int], linkedList1: Node[int]) -> Node[int]:
    valueOne = int(linkedList0.__repr__())
    valueTwo = int(linkedList1.__repr__())

    total = str(valueOne + valueTwo).split()[::-1]

    currNode = Node(int(total[0]))
    origin = currNode
    for n in range(1, len(total)):
        currNode.setNext(Node(total[n]))
        currNode = currNode.getNext()

    return origin

def test_sumLinkedList():
    linkedList0 = Node(9)
    linkedList0.setNext(Node(9))

    linkedList1 = Node(5)
    linkedList1.setNext(Node(2))

    linkedListSum = Node(4)
    linkedListSum.setNext(Node(2))
    linkedListSum.getNext().setNext(Node(1))

    assert sumLinkedLists(linkedList0, linkedList1) == linkedListSum
