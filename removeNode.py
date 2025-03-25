class Node:
    def __init__(self, data: any):
        self.__data = data
        self.__next = None

    def setNext(self, node: any):
        if isinstance(node, Node):
            self.__next = node
        else:
            self.__next = Node(node)

    def getData(self) -> any:
        return self.__data

    def getNext(self):
        return self.__next

    def __str__(self) -> str:
        return str(self.__data)


class LinkedList:
    def __init__(self, head: any):
        if isinstance(head, Node):
            self.__head = head
        else:
            self.__head = Node(head)

    def setNext(self, node: any):
        current = self.__head
        while current.getNext() is not None:
            current = current.getNext()

        if isinstance(node, Node):
            current.setNext(node)
        else:
            current.setNext(Node(node))

    def getHead(self) -> Node:
        return self.__head

    def removeNode(self, k: int) -> Node:
        dummy = Node(0)  # Create a dummy node
        dummy.setNext(self.__head)

        slow = dummy
        fast = dummy

        # Move fast k steps ahead
        for _ in range(k):
            fast = fast.getNext()
            if fast is None:
                raise ValueError("k is larger than the length of the list")

        # Move both pointers until fast reaches the end
        while fast.getNext() is not None:
            slow = slow.getNext()
            fast = fast.getNext()

        # Remove the k-th node from the end
        slow.setNext(slow.getNext().getNext())

        # Return the new head of the list
        return dummy.getNext()

    def __str__(self) -> str:
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.getData()))
            current = current.getNext()
        return " -> ".join(result)


def main():
    # Create a linked list: 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14
    test = LinkedList(5)
    for i in range(6, 15):
        test.setNext(i)

    print("Original List:")
    print(test)

    # Remove the 4th node from the end (which is 10)
    test.removeNode(4)

    print("List after removing the 4th node from the end:")
    print(test)


if __name__ == '__main__':
    main()
