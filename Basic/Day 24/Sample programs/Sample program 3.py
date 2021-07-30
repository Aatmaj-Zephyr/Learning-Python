print("\n****** slicing of strings *****\n")

st = "Python Fundamentals"
print(st, "\t\tLength = ", len(st))

s1= st[2:8]
print("st[2:8]".ljust(20), s1)


s1= st[0:len(st)]
print("st[0:len(st)]".ljust(20), s1)

s1= st[0:4]
print("st[0:4]".ljust(20), s1)

s1= st[4:len(st)]           
print("st[4:len(st)]".ljust(20), s1)

s1= st[3:-5]            
print("st[3:-5]".ljust(20), s1)

s1= st[4:0]         
print("st[4:0]".ljust(20), s1)

s1= st[4:]          
print("st[4:]".ljust(20), s1)

s1= st[8:-1]
print("st[8:-1]".ljust(20), s1)

s1= st[8:-3]
print("st[8:-3]".ljust(20), s1)
