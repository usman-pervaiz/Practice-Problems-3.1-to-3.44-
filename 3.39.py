print("\t\t\t Practice Problem 3.39")
def collision(x1,y1,r1,x2,y2,r2):
    import math
    c_dist =((x2 - x1)**2 + (y1 - y2)**2)
    if c_dist <= (r1+r2)**2:
        return True
    else:
        return False
    
x = collision(0,0,1.4,2,2,1.4)
print(x)

x2 = collision(0,0,3,0,5,3)
print(x2)

