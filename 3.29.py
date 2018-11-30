print("\t\t\t Practice Problem 3.29")
n = eval(input('Enter the positive integer:'))
for i in range(1,n+1):
    if (n % i == 0):
        print(i)
