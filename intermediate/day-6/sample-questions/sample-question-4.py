def power(a, b):
    temp=a
    for i in range(1,b):
        temp=temp*a
    return temp
print(power(3,4))
print(pow(3,4))
