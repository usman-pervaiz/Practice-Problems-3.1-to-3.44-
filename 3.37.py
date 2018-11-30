print("\t\t\t Practice Problem 3.37")
def points(x1,y1,x2,y2):
    import math
    d = math.sqrt(((x2 - x1)**2) +((y2 - y1)**2))
    if x2 == 0:
        print('The slope is infinity' + ' ' + 'and the distance is',d)
    else:
        s = ((y2 - y1) / (x2- x1))
        print('The slope is',s,'and the distance is',d)
coordinates = points(4,3,0,1)
print(coordinates)

coordinates2 = points(6,7,8,9)
print(coordinates2)
