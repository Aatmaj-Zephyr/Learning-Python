print(
    "Please enter 'Add' for Adding, 'Remove' for removing, print to print and end to terminate the program....."
)
stack = []  #make a list named 'stack'
while (True):
    a = input("...")  #get input from the user
    if (a == 'Add'):
        while True:  #To check if the input is a number or not
            a = input("Which number to Add?... ")
            if (48 <= ord(a) <= 57):  #check
                stack.append(a)  #Add the number
                break
#if the input is number, then terminate the nested while loop,
# else continue the loop until numeric value is obtained
            else:
                print("Please enter only numbers ")  #error return
    elif (a == 'Remove'):
        if (len(stack) != 0):
            print(stack[0])  #remove and return
            stack.remove(stack[0])
        else:
            print("Cannot Remove from an empty list ")
    elif (a == 'print'):
        print(stack)  #print the list
    elif (a == 'end'):
        break  #terminate the while loop
    else:
        print("Unknown command ")
print("Thank you")
