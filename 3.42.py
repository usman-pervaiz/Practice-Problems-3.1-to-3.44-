print("\t\t\t Practice Problem 3.42")
def avg(numbers):
    for i in numbers:
        b = [sum(i)/(len(i))]
        print(*b)
    
x = avg([[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]])
print(x)
