from tkinter import *
master= Tk()
master.title("Color Demo...")
master.configure(bg='pINk') # Not case sensative
master.geometry("300x200")


v = IntVar()
v.set(-1) #initializing the choice, i.e. no default choice
colors = ["Blue","Green","Red","Yellow"]
# making an array to choose the colors from


# text to display in the label

def showchoice(): # function to display the result
     ResultLabel.config(text=colors[v.get()],bg=colors[v.get()],fg="Orange") # set the font color to Orange.


ResultLabel=Label(master,font=('Helvetica', 18, 'bold '), bg="Pink", text="...")
# Make the label                  
ResultLabel.pack()

#Set the radiobuttons
Radiobutton1=Radiobutton(master,text=colors[0],variable=v,command=showchoice, fg=colors[0], bg="Pink", value=0)
Radiobutton2=Radiobutton(master,text=colors[1],variable=v,command=showchoice, fg=colors[1], bg="Pink", value=1)
Radiobutton3=Radiobutton(master,text=colors[2],variable=v,command=showchoice, fg=colors[2], bg="Pink", value=2)
Radiobutton4=Radiobutton(master,text=colors[3],variable=v,command=showchoice, fg=colors[3], bg="Pink", value=3)

Radiobutton1.pack()
Radiobutton2.pack()
Radiobutton3.pack()
Radiobutton4.pack()                

master.mainloop()   
