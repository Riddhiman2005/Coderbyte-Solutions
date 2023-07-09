
def FindIntersection(strArr):
    # Split the input string into two lists of numbers
    list1 = set(map(int, strArr[0].replace(" ", "").split(",")))
    list2 = set(map(int, strArr[1].replace(" ", "").split(",")))

    # Find the intersection of the two lists
    intersection = sorted(list1.intersection(list2))

    if len(intersection) == 0:
        return "false"

    # Convert the intersection numbers to strings and join them with commas
    return ",".join(map(str, intersection))

# Testing the Function with Example Inputs

print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))  # Output: 1,4,13
print(FindIntersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]))  # Output: 1,9,10
