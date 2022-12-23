def ChangeLabel():
    if(bold.get() == 1 and italics.get() == 0):
        label.config(text='bold',font=('Helvetica', 18, 'bold'))
    elif(bold.get() ==0 and italics.get() == 1):
        label.config(text='italics',font=('Helvetica', 18, 'italic'))
    elif(bold.get() ==1 and italics.get() == 1):
        label.config(text='bold and italics',font=('Helvetica', 18, 'bold italic'))
    else:
        label.config(text='text',font=('Helvetica', 18, ''))

bold= BooleanVar()
italics= BooleanVar()
