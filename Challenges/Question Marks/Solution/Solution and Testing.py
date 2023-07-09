
def QuestionsMarks(str):
    # Initialize variables
    num1 = None
    count = 0
    result = False

    for char in str:
        if char.isdigit():
            if num1 is not None and int(char) + num1 == 10:
                if count != 3:
                    return "false"
                result = True
            num1 = int(char)
            count = 0
        elif char == "?":
            count += 1

    return "true" if result else "false"

# Testing

print(QuestionsMarks("arrb6???4xxbl5???eee5"))  # Output: true
print(QuestionsMarks("aa6?9"))  # Output: false
print(QuestionsMarks("acc?7??sss?3rr1??????5"))  # Output: true
