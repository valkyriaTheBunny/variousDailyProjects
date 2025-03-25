class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def kthLast(node, k):
    prev, kth, end = node.val
    for _ in range(k):
        end =  end.next
    while end != None:
        prev = kth
        end = end.next
        kth = kth.next
    prev.next = kth.next
    kth = None
    