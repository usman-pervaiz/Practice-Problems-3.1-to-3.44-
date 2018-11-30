print("\t\t\t Practice Problem 3.12")
def negatives(number):
    neg_num = []
    for i in number:
        if i < 0:
            neg_num.append(i)
    return neg_num

x = negatives([1,3,-9,-10,-6,-8])
print(*x, sep ="\n")
