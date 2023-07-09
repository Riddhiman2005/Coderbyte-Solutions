
def BracketCombinations(num):
    def backtrack(open_count, close_count):
        # Base case: all parentheses are placed
        if open_count == 0 and close_count == 0:
            return 1

        total = 0

        # Place an open parenthesis if there are any remaining
        if open_count > 0:
            total += backtrack(open_count - 1, close_count + 1)

        # Place a closing parenthesis if there are any remaining
        if close_count > 0:
            total += backtrack(open_count, close_count - 1)

        return total

    # Call the backtrack function with the initial counts
    return backtrack(num, 0)


# Testing the function with different inputs

print(BracketCombinations(3))  # Output: 5
print(BracketCombinations(4))  # Output: 14
print(BracketCombinations(5))  # Output: 42
