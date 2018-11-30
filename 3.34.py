print("\t\t\t Practice Problem 3.34")
def pay(hourly,hours):
    print('hourly wage:',hourly,'hr')
    print('hourly pay:','10$')
    if hours >= 40:
        sal = 40*hourly 
        O_time = sal + hourly *(hours - 40) * 1.5
        return O_time
    else:
        Not_Otime = hours * hourly
        return Not_Otime
        
salary = pay(10,35)
print(salary)

salary2 = pay(10,45)
print(salary2)
