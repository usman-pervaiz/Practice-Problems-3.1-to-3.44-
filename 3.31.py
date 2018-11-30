print("\t\t\t Practice Problem 3.31")
x = eval(input('Enter the X coordinates:'))
y = eval(input('Enter the Y coordinates:'))
r = 8

import math
calculation = math.sqrt(x**2 + y**2)

if calculation <= r:
    print('It is in!')
else:
    print('It is not in')
