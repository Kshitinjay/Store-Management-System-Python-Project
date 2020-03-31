#main billing window
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect("C:/Users/kshitinjay/Desktop/Store managment Software using Tkinter/Database/store.db")
c = conn.cursor()

date = datetime.datetime.now()
x = date.strftime("%d-%m-%Y %H:%M:%S %p")
dt = datetime.datetime.now().date()

products_list = []
product_quantity = []
product_price = []
product_id = []
# this below list will contain all the labels of right panel
labels_list = []

class Application:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        #left panel
        self.left = Frame(master,width=800,height=768,bg='white')
        self.left.pack(side=LEFT)

        #right panel
        self.right = Frame(master,width=566,height=768,bg='lightblue')
        self.right.pack(side=RIGHT)

        #Matter on left Panel
        self.heading = Label(self.left,text="Billing Software",font=("arial 30 bold"),bg='white')
        self.heading.place(x=270,y=10)

        self.heading = Label(self.left,text="*******************************************************************",font=("arial 15 bold"),bg='white')
        self.heading.place(x=140,y=60)

        self.enterid = Label(self.left,text="Enter Product Id:",font=("arial 15 bold"),bg='white')
        self.enterid.place(x=10,y=130)

        self.enteride = Entry(self.left,width=25,font=("arial 15 bold"),bg='lightblue')
        self.enteride.place(x=280,y=130)
        self.enteride.focus()

        #added button to search in the stock
        self.search_btn = Button(self.left,text=("Search"),width=15,height=2,bg='orange',font=("arial 8 bold"),command=self.ajax)
        self.search_btn.place(x=280,y=165)

        #label which shows product name and detais after clicked on search
        self.pro = Label(self.left,text="Product Name:",font=("arial 15 bold"),bg='white',fg='black')
        self.pro.place(x=10,y=220)

        #this label will be filled after the search is clicked
        self.productname = Label(self.left,text="",font=("arial 15 bold"),bg='white',fg='steelblue')
        self.productname.place(x=280,y=220)

        self.pri = Label(self.left,text="Product Price:",font=("arial 15 bold"),bg='white',fg='black')
        self.pri.place(x=10,y=260)
        #this label will be filled after the search is clicked
        self.pprice = Label(self.left,text="",font=("arial 15 bold"),bg='white',fg='steelblue')
        self.pprice.place(x=280,y=260)


        #Matter on right Panel
        self.date_l = Label(self.right,text="Time of bill " + str(x),font=("arial 10 bold"),fg='black',bg='lightblue')
        self.date_l.place(x=10,y=5)

        self.tproduct = Label(self.right,text="Products",font=("arial 15 bold"),bg='lightblue',fg='black')
        self.tproduct.place(x=10,y=35)

        self.tquantity = Label(self.right,text="Quantity",font=("arial 15 bold"),bg='lightblue',fg='black')
        self.tquantity.place(x=250,y=35)

        self.tamount = Label(self.right,text="Amount",font=("arial 15 bold"),bg='lightblue',fg='black')
        self.tamount.place(x=450,y=35)

        self.total_l = Label(self.right,text="Total ",font=("arial 15 bold"),bg='lightblue',fg='black')
        self.total_l.place(x=10,y=650)


    def ajax(self,*args,**kwargs):
        #fetching id from above
        self.get_id = self.enteride.get()
        #this function shows the detail of the product on left panel
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query,(self.get_id,))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
        self.productname.configure(text="" +str(self.get_name))  
        self.pprice.configure(text="" +str(self.get_price))  

        #quantity and discount label
        self.quantity_l = Label(self.left,text="Enter the Quantity:",font=("arial 15 bold"),bg='white')
        self.quantity_l.place(x=10,y=310)

        self.quantity_e = Entry(self.left,width=25,font=("arial 15 bold"),bg='lightblue')
        self.quantity_e.place(x=280,y=310)
        self.quantity_e.focus()

        self.discount_l = Label(self.left,text="Enter the Discount:",font=("arial 15 bold"),bg='white')
        self.discount_l.place(x=10,y=350)

        self.discount_e = Entry(self.left,width=25,font=("arial 15 bold"),bg='lightblue')
        self.discount_e.place(x=280,y=350)
        self.discount_e.insert(END,0)

        #button to add the items to cart
        self.add_to_cart_btn = Button(self.left,text=("Add to Cart"),width=15,height=2,bg='orange',font=("arial 8 bold"),command=self.add_to_cart)
        self.add_to_cart_btn.place(x=280,y=400)

        #field for amount given by the user
        self.change_l = Label(self.left,text="Given Amount:",font=("arial 15 bold"),bg='white')
        self.change_l.place(x=10,y=460)

        self.change_e = Entry(self.left,width=25,font=("arial 15 bold"),bg='lightblue')
        self.change_e.place(x=280,y=460)

        #button to calculate the amount to return to the customer
        self.change_btn = Button(self.left,text=("Calculate Change"),width=20,height=2,bg='orange',font=("arial 8 bold"),command=self.change_func)
        self.change_btn.place(x=280,y=500)

        #button to Generate the bill
        self.bill_btn = Button(self.left,text=("Generate Bill"),width=20,height=2,bg='red',font=("arial 8 bold"),command=self.generate_bill)
        self.bill_btn.place(x=280,y=550)

        #binding the file to run exe
        self.master.bind("<Return>",self.ajax)
        self.master.bind("<Up>",self.add_to_cart)
        self.master.bind("<space>",self.generate_bill)

    def add_to_cart(self,*args,**kwargs):
        #this function will add items to right cart
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > float(self.get_stock):
            tkinter.messagebox.showinfo("Cart Warning","Sorry we dont have that much of item!")
        else:
            #here adding products and there data to the list for the below calculations
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)   
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            #self.x_index = 0
            self.y_index = 80
            self.counter = 0

            #this loop is used to display the e bill on right panel
            for self.p in products_list:
                self.tempname = Label(self.right,text=str(products_list[self.counter]),font=("arial 9 bold"),bg='lightblue',fg='black')
                self.tempname.place(x=10,y=self.y_index)
                labels_list.append(self.tempname) #adding label to list to clear it after billing

                self.tempqt = Label(self.right,text=str(product_quantity[self.counter]),font=("arial 9 bold"),bg='lightblue',fg='black')
                self.tempqt.place(x=255,y=self.y_index)
                labels_list.append(self.tempqt) #adding label to list to clear it after billing

                self.tempprice = Label(self.right,text=str(product_price[self.counter]),font=("arial 9 bold"),bg='lightblue',fg='black')
                self.tempprice.place(x=455,y=self.y_index)
                labels_list.append(self.tempprice) #adding label to list to clear it after billing

                self.y_index +=25
                self.counter +=1

                #this label is used to give total on the screen
                self.total_l.configure(text="Total Rs:" + str(sum(product_price)))

                #vanishes all label and entries after add to cart is clicked
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.place_forget()
                self.enteride.focus()
                self.enteride.delete(0,END)

    def change_func(self,*args,**kwargs):
        #Calculating the amount to return
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))
        self.to_give = self.amount_given - self.our_total

        #printing the amount to be return to the customer
        self.change_to_give = Label(self.left,text="Return Rs: " + str(self.to_give),font=("arial 15 bold"),bg='white',fg='red')
        self.change_to_give.place(x=450,y=505)

    #this function will generate the bill and minus the stock
    def generate_bill(self,*args,**kwargs):
        # Here we are creating bill before the table updating
        directory = "C:/Users/kshitinjay/Desktop/Store managment Software using Tkinter/" + str(dt) + "/"
        # here we are making the forlder if it is not present
        if not os.path.exists(directory):
            os.makedirs(directory)
        #generating random number to print on the bill for identification
        ran_no = str(random.randrange(5000, 10000))
        # Now making the bill Template
        company = "\t\t\t\t   Kumar Industries"
        address = "\n\t\t\t\t\tAllahabad"
        phone = "\n\t\t\t\t\t8687316641"
        sample = "\n\t\t\t\t\tInvoice " + str(ran_no)
        dta = "\n\t\t\t\t" + str(x)
        header = "\n\n\t\t\t-----------------------------------\n\t\t\tSn.\tProducts\tQuantity\tAmount\t\t\t\t\t"
        final = company + address + phone + sample + dta + "\n" + header

        #now open a file to make the template
        
        file_name = str(directory) + ran_no + ".rtf"   
        f = open(file_name,'w')
        f.write(final)
        r = 1
        i = 0
        for t in products_list:
            f.write("\n\t\t\t" + str(r) + "\t" + str(products_list[i] + ".....")[:7] + "\t" + str(product_quantity[i]) + "\t\t" + str(product_price[i]))
            i += 1
            r += 1 
        f.write("\n\n\n\t\t\t\t\t\t" + "Total Bill: " + str(sum(product_price)))      
        #os.startfile(file_name,"print")    
        f.close()



        self.a = 0
        initial = 'SELECT * FROM inventory WHERE id=?'
        result = c.execute(initial,(product_id[self.a], ))
        for i in products_list:
            for r in result:
                self.old_stock = r[2]

            self.new_stock = int(self.get_stock) - int(product_quantity[self.a])

        #     #updating the table after the item is added to the cart
            sql = 'UPDATE inventory SET stock=? WHERE id=?'
            c.execute(sql,(self.new_stock,product_id[self.a]))
            conn.commit()

        #     #below code will insert  transactions into transaction table
            sql2 = 'INSERT INTO transactions (product_name,quantity,amount,date) VALUES(?,?,?,?)'
            c.execute(sql2,(products_list[self.a],product_quantity[self.a],product_price[self.a],x))
            conn.commit()
            self.a +=1
        #this loop is destroying right panel list after billing is done
        for i in labels_list:
            i.destroy()
        del(products_list[:])
        del(product_quantity[:])
        del(product_price[:])
        del(product_id[:])    
        self.total_l.configure(text="Total:")
        self.change_to_give.configure(text="")
        self.discount_e.delete(0,END)
        self.change_e.delete(0,END)

        tkinter.messagebox.showinfo("Success","Transaction Successful")

root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.mainloop()