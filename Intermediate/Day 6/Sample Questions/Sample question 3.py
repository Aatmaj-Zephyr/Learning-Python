def power(x, y):      
    if (y == 0):
        return 1
    if (y % 2 == 0):
        return power(x, y // 2) * power(x, y // 2)      
    return x * power(x, y // 2) * power(x, y // 2)
print(power(2,3))
print(pow(2,3))
