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

        self.heading = Label(master,text="Update database",font=("arial 40 bold"),fg='steelblue')
        self.heading.place(x=450,y=0)

        #labels for the window

        self.id_l = Label(master,text="Enter id to Update: ",font=("arial 15 bold"))
        self.id_l.place(x=10,y=100)

        self.name_l = Label(master,text="Enter Product name",font=("arial 15 bold"))
        self.name_l.place(x=10,y=150)

        self.stock_l = Label(master,text="Enter Stocks",font=("arial 15 bold"))
        self.stock_l.place(x=10,y=200)

        self.cp_l = Label(master,text="Enter Cost Price",font=("arial 15 bold"))
        self.cp_l.place(x=10,y=250)

        self.sp_l = Label(master,text="Enter Selling Price",font=("arial 15 bold"))
        self.sp_l.place(x=10,y=300)

        self.totalcp_l = Label(master,text="Enter Total Cost Price",font=("arial 15 bold"))
        self.totalcp_l.place(x=10,y=350)

        self.totalsp_l = Label(master,text="Enter Total Selling Price",font=("arial 15 bold"))
        self.totalsp_l.place(x=10,y=400)

        self.vendor_l = Label(master,text="Enter Vendor Name",font=("arial 15 bold"))
        self.vendor_l.place(x=10,y=450)

        self.vendor_phone_l = Label(master,text="Enter Vendor Phone",font=("arial 15 bold"))
        self.vendor_phone_l.place(x=10,y=500)

        #entries for the window
        self.id_e = Entry(master,width=10,font=("arial 15"))
        self.id_e.place(x=280,y=100)

        self.name_e = Entry(master,width=25,font=("arial 15"))
        self.name_e.place(x=280,y=150)

        self.stock_e = Entry(master,width=25,font=("arial 15"))
        self.stock_e.place(x=280,y=200)

        self.cp_e = Entry(master,width=25,font=("arial 15"))
        self.cp_e.place(x=280,y=250)

        self.sp_e = Entry(master,width=25,font=("arial 15"))
        self.sp_e.place(x=280,y=300)

        self.totalcp_e = Entry(master,width=25,font=("arial 15"))
        self.totalcp_e.place(x=280,y=350)

        self.totalsp_e = Entry(master,width=25,font=("arial 15"))
        self.totalsp_e.place(x=280,y=400)

        self.vendor_e = Entry(master,width=25,font=("arial 15"))
        self.vendor_e.place(x=280,y=450)

        self.vendor_phone_e = Entry(master,width=25,font=("arial 15"))
        self.vendor_phone_e.place(x=280,y=500)

        #button to add,update,search the above data to the database

        self.btn_add = Button(master,text="Update database",width=25,height=2,bg='steelblue',fg='white',command=self.update)
        self.btn_add.place(x=320,y=550)

        self.btn_clear = Button(master,text="Reset",width=25,height=2,bg='steelblue',fg='white',command=self.clear_all)
        self.btn_clear.place(x=80,y=550)

        self.btn_search = Button(master,text="Search",width=10,height=1,bg='red',fg='white',command=self.search)
        self.btn_search.place(x=420,y=100)

        #text box to see the log

        self.tbox = Text(master,width=40,height=20)
        self.tbox.place(x=590,y=100)

     #clearing the input fields
    def clear_all(self,*args,**kargs):
        #print("hey cleared")
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.totalcp_e.delete(0,END)
        self.totalsp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phone_e.delete(0,END)
        self.id_e.delete(0,END)

    def search(self,*args,**kargs):
        sql = 'SELECT * FROM inventory where id=?'
        result = c.execute(sql, (self.id_e.get(), ))
        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
        conn.commit()

        #show entries into the entry boxes to update
        self.name_e.delete(0,END) #to clear the previous entry
        self.name_e.insert(0,str(self.n1))

        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))

        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n3))

        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n4))

        self.totalcp_e.delete(0,END)
        self.totalcp_e.insert(0,str(self.n5))

        self.totalsp_e.delete(0,END)
        self.totalsp_e.insert(0,str(self.n6))

        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n7))

        self.vendor_phone_e.delete(0,END)
        self.vendor_phone_e.insert(0,str(self.n8))

    def update(self,*args,**kargs):
        print("Updated")
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_e.get()
        query = 'UPDATE inventory SET name=?,stock=?,cp=?,sp=?,totalcp=?,totalsp=?,vendor=?,vendor_phone=? WHERE id=?'
        c.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,self.id_e.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Updated","Data is Updated")


root = Tk()
b = Database(root)

root.geometry("1366x768")
root.title("Add to Database")
root.mainloop()
