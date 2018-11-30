print("\t\t\t Practice Problem 3.40")
def partition(names):
    return[firstname for firstname in names
           if firstname[0].lower() in 'abhcdefgun']

x = partition(['Usman','Hamza','Sohaib','Talha','Nahum'])
x.sort()
print(*x,sep = '\n')
