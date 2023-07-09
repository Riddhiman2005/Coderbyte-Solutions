
def BracketMatcher(str):
    stack = []

    for char in str:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return 0
            stack.pop()

    return 1 if len(stack) == 0 else 0

# Testing 

print(BracketMatcher("(hello (world))"))  # Output: 1
print(BracketMatcher("((hello (world))"))  # Output: 0
print(BracketMatcher("(coder)(byte))"))  # Output: 0
print(BracketMatcher("(c(oder)) b(yte)"))  # Output: 1
