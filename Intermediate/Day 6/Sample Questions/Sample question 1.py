def armstrong(x):
    a=str(x) #convert int to string to make it iteratable
    counter=0
    Sum=0
    for i in a:
        counter=counter+1

    for i in a:
        Sum=Sum+pow(int(i),counter)
    if(Sum==x):
        return True
    return False
print(armstrong(153))
print(armstrong(1723))
