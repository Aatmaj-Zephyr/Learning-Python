a=['a','b','c','1','2'] 
print(a)
a.append(2) 
#add 2 at the end
a.append('c')
print(a.count('c'))
#here we are asking how many times the character c is in the list.
#so answer must be 2
print(a.count(2)) 
#here we are asking how many times int 2 is in the list
print(a.index('1'))
#returns the index at the first occurrence of the element
b=['z','e']
a.extend(b)
#Adds the entire list to a
print(a)
