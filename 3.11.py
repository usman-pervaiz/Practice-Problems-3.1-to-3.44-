print("\t\t\t Practice Problem 3.11")
def allEven(x):
    for num in x:
        if num % 2 != 0:
            return False
    return True
numbers = allEven([3,2,-8,-7,10])
print(numbers)
