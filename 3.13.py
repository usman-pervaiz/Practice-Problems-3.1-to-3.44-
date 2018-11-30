print("\t\t\t Practice Problem 3.13")
def average(x, y):
    return(x+y)/2
    
help(average)


def negatives(number):
    neg_num = []
    for i in number:
        if i < 0:
            neg_num.append(i)
    return neg_num

help(negatives)
