from tkinter import *

root = Tk()
root.geometry('500x300')


def getVals():
    print('Accepted')


# heading
Label(root, text='Vanja\'s Registration Form',
      font='arial 15 bold').grid(row=0, column=3)

# field name
name = Label(root, text='Name')
phone = Label(root, text='Phone')
gender = Label(root, text='Gender')
emergency = Label(root, text='Emergency')
paymentmood = Label(root, text='Payment Mood')

# packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# variables for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

# creating entry fields
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentmoodvalue)

# packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# checkbox
checkBtn = Checkbutton(text='Remember me?', variable=checkvalue)
checkBtn.grid(row=6, column=3)

# submit button
Button(text='Submit', command=getVals).grid(row=7, column=3)


root.mainloop()
