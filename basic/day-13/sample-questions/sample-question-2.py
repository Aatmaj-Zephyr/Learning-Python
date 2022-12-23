print(
    "Please enter 'pop' for popping, 'push' for pushing, print to print and end to terminate the program....."
)
stack = []  #make a list named 'stack'
while (True):
    a = input("...")  #get input from the user
    if (a == 'push'):
        while True:  #To check if the input is a number or not
            a = input("Which number to push?... ")
            if (48 <= ord(a) <= 57):  #check
                stack.append(a)  #push the number
                break
#if the input is number, then terminate the nested while loop,
# else continue the loop until numeric value is obtained
            else:
                print("Please enter only numbers ")  #error return
    elif (a == 'pop'):
        print(stack.pop())  #pop, ie. remove and return
    elif (a == 'print'):
        print(stack)  #print the list
    elif (a == 'end'):
        break  #terminate the while loop
    else:
        print("Unknown command ")
print("Thank you")
