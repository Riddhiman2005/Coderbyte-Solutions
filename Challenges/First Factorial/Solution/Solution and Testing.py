
def FirstFactorial(num):
    factorial = 1

    # Calculate factorial
    for i in range(1, num + 1):
        factorial *= i

    return factorial

# Testing

print(FirstFactorial(4))  # Output: 24
print(FirstFactorial(8))  # Output: 40320
