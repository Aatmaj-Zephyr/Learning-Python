import math
def asinh(a):
    return math.log(a+math.sqrt(pow(a,2)+1),math.e)
print(asinh(2))
print(math.asinh(2))
