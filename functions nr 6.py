def list_of_tuples(n):
    l = []
    for x in range(1,n):
        t = (x, x*x, x*x*x)
        l.append(t)
    return 1

n = int(input("Enter an ending value:"))
print(list_of_tuples(n+1))
