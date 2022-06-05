from tkinter import *
root = Tk()
root.wm_geometry("500x300")
def getvals():
    print("ACCEPTED")
#heading
Label(root, text="Registration form", font="calligraphy 15 bold").grid(row=0,column=4)
#Field  Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
payment = Label(root, text="Payment")
# Packing Feilds
name.grid(row= 1, column=2)
phone.grid(row=2 , column=2)
gender.grid(row=3 , column=2)
payment.grid(row=4 , column=2)
#variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar
# creating entry feild
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
paymententry= Entry(root, textvariable=paymentvalue)

# packing entry feilds
nameentry.grid(row=1 ,column=4)
phoneentry.grid(row=2,column=4)
genderentry.grid(row=3,column=4)
paymententry.grid(row=4,column=4)
# creating checkbox
checkbtn = Checkbutton(text="remember me!", variable = checkvalue)
checkbtn.grid(row=7,column= 4)
#Submit button
Button(text="Submit", command=getvals).grid(row=8,column=4)
root.mainloop()
