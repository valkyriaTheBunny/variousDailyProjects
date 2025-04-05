from __future__ import annotations
class Node:
    def __init__(self, val: any):
        self.__val = val
        self.left : Node = None
        self.right  : Node = None

    def getValue(self) -> any:
        return self.__val

    def __eq__(self, value: Node):
        if not isinstance(value, Node):
            return False
        return self.__val == value.getValue()

    def __str__(self):
        return str(self.__val)

    def __repr__(self):
        return str(self.__val)

def insert(self, root: Node, newVal: any):
    if root is None:
        root = Node(newVal)
        return root

    if newVal < root.getValue():
        root.left = insert(root.left, newVal)
    else:
        root.right = insert(root.right, newVal)
    return root

def findNodesWithSum(root: Node[int], value: int) -> list[Node[int]]:
    def inorder(node: Node, vals: list) -> None:
        if not node:
            return
        inorder(node.left, vals)
        vals.append(node)
        inorder(node.right, vals)

    nodes: list[Node] = []
    inorder(root, nodes)

    left, right = 0, len(nodes) - 1
    while left < right:
        total = nodes[left].getValue() + nodes[right].getValue()
        if total == value:
            return (nodes[left], nodes[right])
        elif total < value:
            left += 1
        else:
            right -= 1

    return None

def test_nodesWithSum():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(11)
    root.right.right = Node(19)

    assert findNodesWithSum(root, 20) == (Node(5), Node(15))
