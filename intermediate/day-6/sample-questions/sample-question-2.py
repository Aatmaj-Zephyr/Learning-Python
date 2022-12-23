def armstrong(x):
    n = 0
    i=x
    while (i != 0):
        n = n + 1
        i = i // 10
    temp = x
    Sum = 0
    while (temp != 0):
        r = temp % 10
        Sum = Sum + pow(r, n)
        temp = temp // 10
    return (Sum == x) #shorthand for if Sum==x return True else return False
print(armstrong(153))
print(armstrong(1723))
