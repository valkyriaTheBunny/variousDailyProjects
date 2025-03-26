class Stack:
    def __init__(self):
        self.__stack = []
        self.__lastIndex = 0

    def push(self, item: any, stack_num: int) -> None:
        if stack_num > 3 and stack_num < 1:
            return

        if self.__lastIndex > stack_num:
            index = stack_num
            while self.__stack[index] != None and index < len(self.__stack):
                index += stack_num
            if index < len(self.__stack):
                self.__stack.insert(index, item)
        elif self.__lastIndex % stack_num != 0:
            while self.__lastIndex % stack_num != 0:
                self.__stack.append(None)
                self.__lastIndex += 1
            self.__stack.append(item)
            self.__lastIndex += 1
        else:
            self.__stack.append(item)
            self.__lastIndex += 1

    def pop(self, stack_num: int) -> any:
        if self.__lastIndex % stack_num == 0:
            return self.__stack.pop()
        else:
            index = self.__lastIndex
            while index % stack_num != 0:
                index -= 1
            return self.__stack.pop(index)

def test_stack_creation():
    pass
