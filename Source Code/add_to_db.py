from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("C:/Users/kshitinjay/Desktop/Store managment Software using Tkinter/Database/store.db")
c = conn.cursor()
result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self,master,*args,**kargs):
        self.master = master

        self.heading = Label(master,text="Add to database",font=("arial 40 bold"),fg='steelblue')
        self.heading.place(x=450,y=10)

        #labels for the window
        self.name_l = Label(master,text="Enter Product name",font=("arial 15 bold"))
        self.name_l.place(x=10,y=75)

        self.stock_l = Label(master,text="Enter Stocks",font=("arial 15 bold"))
        self.stock_l.place(x=10,y=135)

        self.cp_l = Label(master,text="Enter Cost Price",font=("arial 15 bold"))
        self.cp_l.place(x=10,y=195)

        self.sp_l = Label(master,text="Enter Selling Price",font=("arial 15 bold"))
        self.sp_l.place(x=10,y=255)

        self.vendor_l = Label(master,text="Enter Vendor Name",font=("arial 15 bold"))
        self.vendor_l.place(x=10,y=315)

        self.vendor_phone_l = Label(master,text="Enter Vendor Phone",font=("arial 15 bold"))
        self.vendor_phone_l.place(x=10,y=375)

        self.id_l = Label(master,text="Enter Product Id",font=("arial 15 bold"))
        self.id_l.place(x=10,y=430)

        self.previd_l = Label(master,text="Id has reached upto: "+str(id),font=("arial 15 bold"))
        self.previd_l.place(x=10,y=490)

        #entries for the window 
        self.name_e = Entry(master,width=25,font=("arial 15"))
        self.name_e.place(x=280,y=75)

        self.stock_e = Entry(master,width=25,font=("arial 15"))
        self.stock_e.place(x=280,y=135)

        self.cp_e = Entry(master,width=25,font=("arial 15"))
        self.cp_e.place(x=280,y=195)

        self.sp_e = Entry(master,width=25,font=("arial 15"))
        self.sp_e.place(x=280,y=255)

        self.vendor_e = Entry(master,width=25,font=("arial 15"))
        self.vendor_e.place(x=280,y=315)

        self.vendor_phone_e = Entry(master,width=25,font=("arial 15"))
        self.vendor_phone_e.place(x=280,y=375)

        self.id_e = Entry(master,width=25,font=("arial 15"))
        self.id_e.place(x=280,y=430)

        #button to add the above data to the database

        self.btn_add = Button(master,text="Add to database",width=25,height=2,bg='steelblue',fg='white',command=self.get_items)
        self.btn_add.place(x=320,y=550)

        self.btn_clear = Button(master,text="Reset",width=25,height=2,bg='steelblue',fg='white',command=self.clear_all)
        self.btn_clear.place(x=80,y=550)

        #text box to see the log

        self.tbox = Text(master,width=50,height=20)
        self.tbox.place(x=590,y=75)

        #getting data from the entries
    def get_items(self,*args,**kargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()
        
        #calculating the total cost of items in the bill
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        #check for the empty field
        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '' or self.vendor == '' or self.vendor_phone == '':
            tkinter.messagebox.showinfo("Details Error","Please enter all details to add the item to Stock!")
        else:
            sql = 'INSERT INTO inventory (name,stock,cp,sp,totalcp,totalsp,vendor,vendor_phone,assumed_profit) VALUES (?,?,?,?,?,?,?,?,?)'  
            c.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.vendor,self.vendor_phone,self.assumed_profit,)) 
            conn.commit()
            #textbox insertion
            self.tbox.insert(END,"\n\nInserted " + str(self.name) + " into Database with id " + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Successful","Stock Added")  

    #clearing the input fields
    def clear_all(self,*args,**kargs):
        #print("hey cleared")
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phone_e.delete(0,END)
        self.id_e.delete(0,END)

root = Tk()
b = Database(root)
root.geometry("1366x768")
root.title("Add to Database")
root.mainloop()