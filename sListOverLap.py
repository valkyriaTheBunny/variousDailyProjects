from __future__ import annotations
import pytest

class Node:
    def __init__(self, val: any):
        self.__value = val
        self.__next = None

    def getValue(self) -> any:
        return self.__value

    def setNext(self, nextNode: Node):
        self.__next = nextNode

    def getNext(self) -> Node:
        return self.__next

class LinkedList:
    __head = None
    __length = 0

    def __init__(self):
        pass

    def getHead(self):
        return self.__head

    def insert(self, data: any, index: int = 0):
        newNode = Node(data)

        if index > self.__length:
            raise IndexError("Index out of bounds")

        if index == 0:
            if self.__head is None and index == 0:
                self.__head = newNode
                self.__length += 1
                return
            newNode.setNext(self.__head)
            self.__head = newNode
            self.__length += 1
            return
        elif index < self.__length:
            pos = 1
            currNode = self.__head

            while currNode is not None and pos < index:
                pos += 1
                currNode = currNode.getNext()

            if currNode is not None:
                newNode.setNext(currNode.getNext())
                currNode.setNext(newNode)
                self.__length += 1
                return
            else:
                raise IndexError("Index out of bounds")
        else:
            currNode = self.__head
            while currNode.getNext():
                currNode = currNode.getNext()
            currNode.setNext(newNode)
            self.__length += 1
            return

    def remove(self, index: int = 0) -> any:
        if index > self.__length:
            raise IndexError("Index out of bounds")

        if self.__head is None:
            return None
        if index == 0:
            if self.__head.getNext() is None:
                temp = self.__head.getValue()
                self.__head = None
                self.__length -= 1
                return temp
            temp = self.__head.getValue()
            self.__head = self.__head.getNext()
            self.__length -= 1
            return temp
        elif index < self.__length:
            currNode = self.__head
            pos = 1

            while (currNode is not None
                   and currNode.getNext() is not None
                   and pos < index):
                pos += 1
                currNode = currNode.getNext()

            if currNode is not None:
                temp = currNode.getNext().getValue()
                if currNode.getNext() is not None:
                    currNode.setNext(currNode.getNext().getNext())
                return temp
            else:
                raise IndexError("Index out of bounds")
        elif index == self.length:
            currNode = self.__head
            while currNode.getNext().getNext():
                currNode = currNode.getNext()
            temp = currNode.getNext().getValue()
            currNode.setNext(None)
            return temp

    def length(self) -> int:
        return self.__length

    def __repr__(self) -> str:
        bldr = "["
        currNode = self.__head
        pos = 0

        while currNode:
            if pos < self.__length - 1:
                bldr += str(currNode.getValue()) + ","
            else:
                bldr += str(currNode.getValue()) + "]"
            pos += 1
            currNode = currNode.getNext()
        return bldr

    def __str__(self) -> str:
        bldr = "["
        currNode = self.__head
        pos = 0

        while currNode:
            if pos < self.__length - 1:
                bldr += str(currNode.getValue()) + ","
            else:
                bldr += str(currNode.getValue()) + "]"
            pos += 1
            currNode = currNode.getNext()
        return bldr

def overlap(lListOne: LinkedList, lListTwo: LinkedList) -> any:
    seenNodes = set()

    currNodeOne = lListOne.getHead()
    while currNodeOne is not None:
        seenNodes.add(currNodeOne.getValue())
        currNodeOne = currNodeOne.getNext()

    currNodeTwo = lListTwo.getHead()
    while currNodeTwo is not None:
        if currNodeTwo.getValue() in seenNodes:
            return currNodeTwo.getValue()
        currNodeTwo = currNodeTwo.getNext()

    return None

@pytest.fixture
def intersectingLists():
    common = Node(8)
    common.setNext(Node(10))

    listOne = LinkedList()
    listOne.insert(3)
    listOne.insert(7, listOne.length())
    listOne.insert(8, listOne.length())
    listOne.insert(10, listOne.length())

    listTwo = LinkedList()
    listTwo.insert(99)
    listTwo.insert(1, listTwo.length())
    listTwo.insert(8, listTwo.length())
    listTwo.insert(10, listTwo.length())

    return listOne, listTwo

def test_overlap(intersectingLists):
    listOne, listTwo = intersectingLists
    assert overlap(listOne, listTwo) == 8
