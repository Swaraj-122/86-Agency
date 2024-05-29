def is_balanced(exp):
    # Dictionary to hold matching pairs of brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    for char in exp:
        if char in matching_bracket.values():
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in matching_bracket.keys():
            # If the character is a closing bracket, check for matching opening bracket
            if stack == [] or matching_bracket[char] != stack.pop():
                return "Not Balanced"
    
    # Check if stack is empty at the end
    if stack == []:
        return "Balanced"
    else:
        return "Not Balanced"

# Test cases
exp1 = "[()]{}{[()()]()}"
exp2 = "[(])"

print(is_balanced(exp1))  # Output: Balanced
print(is_balanced(exp2))  # Output: Not Balanced
