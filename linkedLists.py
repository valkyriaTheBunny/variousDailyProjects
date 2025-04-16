from __future__ import annotations
from typing import Optional
class Node:
    def __init__(self, val: any):
        self.__val = val
        self.__next : Node = None

    def getValue(self) -> any:
        return self.__val

    def getNext(self) -> Node:
        return self.__next

    def setNext(self, val: any):
        if isinstance(val, None):
            return
        if not isinstance(val, Node):
            newNode = Node(val)
            self.__next = newNode
        else:
            self.__next = val

class LinkedList:
    def __init__(self):
        self.__head : Node = None
        self.__length = 0

    def setHead(self, head: any) -> None:
        if not isinstance(head, Node):
            newNode = Node(head)
            self.__head = newNode
        else:
            self.__head = head
        self.__length = 1

    def getHead(self) -> Node:
        return self.__head

    def append(self, val: any, i: int) -> None:
        if i > self.__length:
            return

        if not isinstance(val, Node):
            val = Node(val)

        count = 0
        currNode = self.__head
        while currNode.getNext() and count < i:
            currNode = currNode.getNext()
            count += 1

        if i < self.__length:
            nextNode = currNode.getNext()
            currNode.setNext(val)
            val.setNext(nextNode)
        else:
            currNode.setNext(val)

        self.__length += 1

    def pop(self, i: int) -> Optional[Node]:
        if i > self.__length:
            return

        count = 0
        currNode = self.__head
        while currNode and count < i - 1:
            currNode = currNode.getNext()
            count += 1

        if i < self.__length:
            nextNode = currNode.getNext().getNext()
            temp = currNode.getNext()
            currNode.setNext(nextNode)
        else:
            temp = currNode.getNext()
            currNode.setNext(None)

        self.__length -= 1
        return temp

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> str:
        bldr = "["
        currNode = self.__head
        while currNode:
            bldr += str(currNode.getValue())
            if currNode.getNext():
                bldr += ", "
            currNode = currNode.getNext()
        bldr += "]"
        return bldr

    def __repr__(self) -> str:
        bldr = "["
        currNode = self.__head
        while currNode:
            bldr += str(currNode.getValue())
            if currNode.getNext():
                bldr += ", "
            currNode = currNode.getNext()
        bldr += "]"
        return bldr
