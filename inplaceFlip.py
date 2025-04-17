from linkedLists import LinkedList

def reverseInPlace(lst: LinkedList) -> LinkedList:
    prev = None
    current = lst.getHead()

    while current is not None:
        next_node = current.getNext()
        current.setNext(prev)
        prev = current
        current = next_node

    reversed = LinkedList(prev)
    return reversed

def main():
    head = LinkedList()
    head.setHead(1)
    head.append(2, 1)
    head.append(3, 2)
    head.append(4, 3)
    head.append(5, 4)
    print(head)

    reversed_head = reverseInPlace(head)
    print(reversed_head)

if __name__ == "__main__":
    main()

def test_inplace():
    head = LinkedList()
    head.setHead(1)
    head.append(2, 1)
    head.append(3, 2)
    head.append(4, 3)
    head.append(5, 4)

    assert head == [1, 2, 3, 4, 5]
    assert reverseInPlace(head) == [5, 4, 3, 2, 1]
