print("\t\t\t Practice Problem 3.43")
def hit(x1,y1,r1,x2,y2):
    import math
    dist = ((x2 - x1)**2 + (y1 - y2)**2)
    if dist <= (r1**2):
        return True
    else:
        return False
x = hit(0,0,3,0,0)
print(x)

x2 = hit(0,0,3,4,0)
print(x2)
