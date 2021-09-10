from tkinter import *
master= Tk()
master.title("RadioButton Demo...")
master.geometry("300x200")
v = IntVar()
v.set(-1) #initializing the choice, i.e. no default choice

languages = ["Python","Java","Swift","JavaScript"]
# making an array to choose the programming languages from

Stringlbl="My Favourite programming language is.... "
# text to display in the label

def showchoice(): # function to display the result
     ResultLabel.config(text= Stringlbl +languages[v.get()])

ResultLabel=Label(master,text=Stringlbl)
# Make the label                  
ResultLabel.pack()

#Set the radiobuttons
Radiobutton1=Radiobutton(master,text=languages[0],variable=v,command=showchoice, value=0)
Radiobutton2=Radiobutton(master,text=languages[1],variable=v,command=showchoice, value=1)
Radiobutton3=Radiobutton(master,text=languages[2],variable=v,command=showchoice, value=2)
Radiobutton4=Radiobutton(master,text=languages[3],variable=v,command=showchoice, value=3)

Radiobutton1.pack()
Radiobutton2.pack()
Radiobutton3.pack()
Radiobutton4.pack()                

master.mainloop()  
