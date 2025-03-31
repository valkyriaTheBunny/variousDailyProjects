class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item: any, stack_num: int) -> None:
        if stack_num > 3 or stack_num < 1:
            return

        index = stack_num - 1

        while index < len(self.__stack) and self.__stack[index] is not None:
            index += 3

        while len(self.__stack) <= index:
            self.__stack.append(None)

        self.__stack[index] = item


    def pop(self, stack_num: int) -> any:
        if stack_num > 3 or stack_num < 1:
            return None

        index =  stack_num - 1
        lastValid = -1

        while index < len(self.__stack):
            if self.__stack[index] is not None:
                lastValid = index
            index += 3

        if lastValid != -1:
            item = self.__stack[lastValid]
            self.__stack[lastValid] = None
            return item
        
        return None

    def __eq__(self, obj: any) -> bool:
        return self.__stack == obj

def test_stack_creation():
    tStack = Stack()
    assert tStack == []

def test_stack_push_first_stack():
    tStack2 = Stack()
    tStack2.push(9, 1)
    assert tStack2 == [9]

def test_stack_push_second_stack():
    tStack3 = Stack()
    tStack3.push(9, 2)
    assert tStack3 == [None, 9]

def test_stack_push_third_stack():
    tStack3 = Stack()
    tStack3.push(9, 3)
    assert tStack3 == [None, None, 9]

def test_stack_push_stacks_with_existing():
    tStack4 = Stack()
    tStack4.push(9, 3)
    tStack4.push(8, 2)
    assert tStack4 == [None, 8, 9]

def test_stack_push_stacks_with_existing_at_index():
    tStack4 = Stack()
    tStack4.push(9, 3)
    tStack4.push(8, 3)
    assert tStack4 == [None, None, 9, None, None, 8]

def test_stack_pop_stacks_with_multiple_at_index():
    tStack4 = Stack()
    tStack4.push(9, 3)
    tStack4.push(8, 3)
    assert tStack4.pop(3) == 8
