st="Learning Python Course"
# :: and -ve index to reverse the string
s1= st[4::-1]
print("st[4::-1]".ljust(20), s1)

s1= st[8::-2]
print("st[8::-2]".ljust(20), s1)

s1= st[::-1]
print("st[::-1]".ljust(20), s1)

s1= st[::-2]
print("st[::-2]".ljust(20), s1)

s1= st[1::-1]
print("st[1::-1]".ljust(20), s1)

s1= st[5:10][::-1]
print("st[5:10][::-1]".ljust(20), s1)

s1= st[4::3]
print("st[4::3]".ljust(20), s1)
