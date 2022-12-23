a=['A','t','m','a','j','zephyr']
print(a)
a.insert(1,'a')
#insert a at second position
a.insert(len(a)-1,'-')
#insert '-' at the second last position
print(a)
a.remove('zephyr')
#remove first occurance of 'zephyr'
print(a)
a.pop()
#removes the last value.
#Pop is opposite of append
#pop also returns the last value.
b=a.pop()
print(b)
#We can also give value to pop to remove the element.
print(a)
print(a.pop(3))
print(a)
