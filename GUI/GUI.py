"""
Name: Muntaha Binte Alam
Email:muntaha.alam@tuni.fi
Student ID: 150448389
The program works with the billing system of any restaurant.
The prices of different foods are pre-defined, so when you enter the quantity it calculates the total of the price.
It also produces an error message if you enter an invalid input such as strings
It also takes care of the sales-tax and tax , first it shows the sub-total without tax and then it shows the total bill
There are 4 buttons in the GUI.
Total: when clicked, it shows the total bill.
Save : when clicked it creates a file in the project directory and saves the data in text file with billing reference number.
Reset: resets everything as fresh
Exit:  exists the program

About considering the GUI as an elementary or advanced GUI , I will leave it to the person evaluating the program

"""





from tkinter import *  #tkinter is used for making gui apps in python
import random #random package is used similarly as the randomize function in c
import time #time package is used for accessing time values to display

root = Tk() #iniitalizing window component
root.geometry("1600x8000") #dimensions
root.title("Restaurant Management") #title bar

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

#time display
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="ALAM RESTAURANT", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0) #app label

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0) #time label

lblInfo2 = Label(Tops, font=('arial', 20, 'bold'), text='', fg="Red", bd=10, anchor='w')
lblInfo2.grid(row=2, column=0) #error label only shown when error is generated



def Ref(): #function used for calculation of bill
    global randomRef, CoFries, CostofFries, CoNoodles, CostofNoodles, CoSoup, CostofSoup, CoBurger, CostBurger
    global CoSandwich, CostSandwich, CoD, CostofDrinks, TotalCost, Ser_Charge, PayTax, TotalCost, AllCost

    #global declaration of variables to access them in other blocks of code

    #reference number generation
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    try:
        #try block
        if (Fries.get() == ""):  #if user doesnt enter a quantity of fooditem it will be as 0
            CoFries = 0
        else:
            CoFries = float(Fries.get()) #else it attains the provided value

        if (Noodles.get() == ""):
            CoNoodles = 0
        else:
            CoNoodles = float(Noodles.get())

        if (Soup.get() == ""):
            CoSoup = 0
        else:
            CoSoup = float(Soup.get())

        if (Burger.get() == ""):
            CoBurger = 0
        else:
            CoBurger = float(Burger.get())

        if (Sandwich.get() == ""):
            CoSandwich = 0
        else:
            CoSandwich = float(Sandwich.get())

        if (Drinks.get() == ""):
            CoD = 0
        else:
            CoD = float(Drinks.get())

    except ValueError: #the exception for cactching value error occured
        lblInfo2.config(text="Invalid values, please re-enter")

    # The price of the different kinds of food is fixed here

    CostofFries = CoFries * 140 #calculation of costs of food items and other calculations based on it
    CostofDrinks = CoD * 65
    CostofNoodles = CoNoodles * 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger * 260
    CostSandwich = CoSandwich * 300

    CostofMeal = "Tk", str(
        '%.2f' % (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich))

    PayTax = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) * 0.15)

    TotalCost = (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) * 0.15)

    Ser = "TK", str('%.2f' % Ser_Charge)

    OverAllCost = "TK", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "TK", str('%.2f' % PayTax)

    AllCost = PayTax + TotalCost + Ser_Charge

    Se_Charge.set(Ser) #attaining values to suitable labels
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def saveData():
    #function using file handling to write data of bill generated by applicaiton in a text file

    with open("restaurant.txt", "a") as f:
        f.write('\nBill reference number = ' + randomRef)
        f.write('\nFries * %.2f = Tk %.2f' %(CoFries,CostofFries))
        f.write('\nNoodles * %.2f = Tk %.2f' %(CoNoodles,CostofNoodles))
        f.write('\nSoup * %.2f = Tk %.2f' %(CoSoup,CostofSoup))
        f.write('\nBurger * %.2f = Tk %.2f' %(CoBurger,CostBurger))
        f.write('\nSandwich * %.2f = Tk %.2f' %(CoSandwich,CostSandwich))
        f.write('\nDrinks * %.2f = Tk %.2f' %(CoD,CostofDrinks))
        f.write('\nCost of Meal = Tk %.2f' %TotalCost)
        f.write('\nservice_charge = Tk %.2f' %Ser_Charge)
        f.write('\nTax = Tk %.2f' %PayTax)
        f.write('\nSub Total = Tk %.2f' %TotalCost)
        f.write('\nTotal Cost = Tk %.2f' %AllCost)
        f.write('\n')




def qExit(): #function for exiting app
    root.destroy()


def Reset(): #function for clearing entries{textboxes}
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Se_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
    lblInfo2.config(text='')


#info left
rand = StringVar()
Fries = StringVar()
Noodles = StringVar()
Soup = StringVar()
SubTotal = StringVar()
Total = StringVar()
Se_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Burger = StringVar()
Sandwich = StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Fries", bd=16, anchor="w")
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue",
                 justify='right')
txtFries.grid(row=1, column=1)

lblNoodles = Label(f1, font=('arial', 16, 'bold'), text="Noodles", bd=16, anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtNoodles.grid(row=2, column=1)

lblSoup = Label(f1, font=('arial', 16, 'bold'), text="Soup", bd=16, anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup = Entry(f1, font=('arial', 16, 'bold'), textvariable=Soup, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtSoup.grid(row=3, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtBurger.grid(row=4, column=1)

lblSandwich = Label(f1, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich = Entry(f1, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSandwich.grid(row=5, column=1)


#info right
lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtCost.grid(row=1, column=3)

lblSer = Label(f1, font=('arial', 16, 'bold'), text="service_charge ", bd=16, anchor="w")
lblSer.grid(row=2, column=2)
txtSer = Entry(f1, font=('arial', 16, 'bold'), textvariable=Se_Charge, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtSer.grid(row=2, column=3)

lblTx = Label(f1, font=('arial', 16, 'bold'), text="Tax", bd=16, anchor="w")
lblTx.grid(row=3, column=2)
txtTx = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtTx.grid(row=3, column=3)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtTotalCost.grid(row=5, column=3)

# buttons
btnTotal = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="grey", command=Ref).grid(row=7, column=1)

btnSave = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Save",
                  bg="green", command=saveData).grid(row=7, column=2)

btnReset = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="orange", command=Reset).grid(row=7, column=3)

btnExit = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",
                 bg="red", command=qExit).grid(row=7, column=4)

root.mainloop()
