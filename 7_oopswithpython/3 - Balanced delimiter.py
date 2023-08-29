def is_balanced_delimiters(input_str):
    stack = []
    opening_chars = "([{"
    closing_chars = ")]}"

    for char in input_str:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if not stack:
                return False
            if opening_chars.index(stack.pop()) != closing_chars.index(char):
                return False
    return not stack
    
input_str = input("Enter a string of delimiters: ")
result = is_balanced_delimiters(input_str)
print(result)
