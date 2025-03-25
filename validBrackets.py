def is_valid_brackets(s):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
        else:
            return False

    return not stack

string1 = "([])[]({})"
string2 = "([)]"
string3 = "((()"

print(is_valid_brackets(string1))
print(is_valid_brackets(string2))  
print(is_valid_brackets(string3))  
