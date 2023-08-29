def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or pairs[char] != stack.pop():
                return False
    return not stack

print(is_balanced("([{}])"))  # Output: True