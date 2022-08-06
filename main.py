from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3
class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("Quan Ly Hoc Sinh")
        self.root.geometry("1370x700")
        self.idvar = StringVar()
        self.namevar = StringVar()
        self.emailvar = StringVar()
        self.gendervar = StringVar()
        self.contactvar = StringVar()
        self.dobvar = StringVar()
        self.addressvar = StringVar()
        self.searchbyvar = StringVar()
        self.searchvar = StringVar()

        quanli = Frame(self.root, bd=4, relief=RIDGE)
        quanli.place(x=20, y=100, width=450, height=560)
        id = Label(quanli, text="ID", fg="blue", font=('times new roman', 20, "bold"))
        id.grid(row=1, column=0, pady=10, padx=20)
        idtxt = Entry(quanli, textvariable=self.idvar, font=("times new roman", 15))
        idtxt.grid(row=1, column=1, pady=10, padx=20)

        name = Label(quanli, text="Name", fg="blue", font=('times new roman', 20, "bold"))
        name.grid(row=2, column=0, pady=10, padx=20)
        nametxt = Entry(quanli, textvariable=self.namevar, font=("times new roman", 15))
        nametxt.grid(row=2, column=1, pady=10, padx=20)

        email = Label(quanli, text="Email", fg="blue", font=('times new roman', 20, "bold"))
        email.grid(row=3, column=0, pady=10, padx=20)
        emailtxt = Entry(quanli, textvariable=self.emailvar, font=("times new roman", 15))
        emailtxt.grid(row=3, column=1, pady=10, padx=20)

        gender = Label(quanli, text="Gender", fg="blue", font=('times new roman', 20, "bold"))
        gender.grid(row=4, column=0, pady=10, padx=20)
        genderbox = ttk.Combobox(quanli, textvariable=self.gendervar, font=("times new roman", 13))
        genderbox['values'] = ('Male', 'Female', 'Other')
        genderbox.grid(row=4, column=1, pady=10, padx=20)

        sdt = Label(quanli, text="Phone number", fg="blue", font=('times new roman', 20, "bold"))
        sdt.grid(row=5, column=0, pady=10, padx=20)
        sdttxt = Entry(quanli, textvariable=self.contactvar, font=("times new roman", 15))
        sdttxt.grid(row=5, column=1, pady=10, padx=20)

        dob = Label(quanli, text="D-O-B", fg="blue", font=('times new roman', 20, "bold"))
        dob.grid(row=6, column=0, pady=10, padx=20)
        dobtxt = Entry(quanli, textvariable=self.dobvar, font=("times new roman", 15))
        dobtxt.grid(row=6, column=1, pady=10, padx=20)

        address = Label(quanli, text="Address", fg="blue", font=('times new roman', 20, "bold"))
        address.grid(row=7, column=0, pady=10, padx=20)
        addresstxt = Entry(quanli, textvariable=self.addressvar, font=("times new roman", 15))
        addresstxt.grid(row=7, column=1, pady=10, padx=20)
        buttonframe = Frame(quanli, bd=3, relief=RIDGE)
        buttonframe.place(x=15, y=455, width=420)
        add = Button(buttonframe, text="ADD", width=10, command=self.addstudent).grid(row=0, column=1, padx=10, pady=10)
        update = Button(buttonframe, text="UPDATE", width=10,command=self.updatedata).grid(row=0, column=2, padx=10, pady=10)
        delete = Button(buttonframe, text="DELETE", width=10,command=self.delete).grid(row=0, column=3, padx=10, pady=10)
        clear = Button(buttonframe, text="CLEAR", width=10,command=self.clear).grid(row=0, column=4, padx=10, pady=10)

        noidung = Frame(self.root, bd=4, relief=RIDGE)
        noidung.place(x=500, y=100, width=880, height=586)

        searchby = Label(noidung, text="Search By", fg="blue", font=("times new roman", 13), width=10)
        searchby.grid(row=0, column=0, pady=10, padx=20)
        searchbybox = ttk.Combobox(noidung, textvariable=self.searchbyvar, font=("times new roman", 10))
        searchbybox['values'] = ('ID','PhoneNumber')
        searchbybox.grid(row=0, column=1, pady=10, padx=10)
        searchtxt = Entry(noidung, textvariable=self.searchvar, font=("times new roman", 14), width=30)
        searchtxt.grid(row=0, column=2, pady=10, padx=20)
        search = Button(noidung, text="SEARCH", width=10, pady=5,command=self.search).grid(row=0, column=3, padx=10, pady=10)
        showall = Button(noidung, text="SHOW ALL", width=10, pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        tableframe = Frame(noidung, bd=4, relief=RIDGE)
        tableframe.place(x=10, y=70, width=760, height=500)
        scrollx = Scrollbar(tableframe, orient=HORIZONTAL)
        scrolly = Scrollbar(tableframe, orient=VERTICAL)
        self.studenttable = ttk.Treeview(tableframe,
                                         columns=("ID", "Name", "Email", "Gender", "Phone Number", "D-O-B", "Address"),
                                         xscrollcommand=scrollx, yscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config()
        scrolly.config()
        self.studenttable.heading("ID", text="ID")
        self.studenttable.heading("Name", text="Name")
        self.studenttable.heading("Email", text="Email")
        self.studenttable.heading("Gender", text="Gender")
        self.studenttable.heading("Phone Number", text="Phone Number")
        self.studenttable.heading("D-O-B", text="D-O-B")
        self.studenttable.heading("Address", text="Address")

        self.studenttable['show'] = 'headings'
        self.studenttable.column("ID", width=30)
        self.studenttable.column("Name", width=100)
        self.studenttable.column("Email", width=100)
        self.studenttable.column("Gender", width=100)
        self.studenttable.column("Phone Number", width=100)
        self.studenttable.column("D-O-B", width=100)
        self.studenttable.column("Address", width=150)
        self.studenttable.pack(fill=BOTH, expand=1)
        self.studenttable.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()






    def addstudent(self):
        if self.idvar.get()==""or self.namevar.get()=="":
            messagebox.showerror("Lỗi", "Cần điền đầy đủ")
        elif self.gendervar.get() == "" or self.emailvar.get() == "":
            messagebox.showerror("Lỗi", "Cần điền đầy đủ")
        elif self.dobvar.get() == "" or self.addressvar.get() == "":
            messagebox.showerror("Lỗi", "Cần điền đầy đủ")
        else:
            con = sqlite3.connect("quanlihocsinh.db")
            cur = con.cursor()
            cur.execute("insert into hocsinh values(:id, :name , :email , :gender , :contact , :dob , :address) ", {
                'id': self.idvar.get(),
                'name': self.namevar.get(),
                'email': self.emailvar.get(),
                'gender': self.gendervar.get(),
                'contact': self.contactvar.get(),
                'dob': self.dobvar.get(),
                'address': self.addressvar.get()

            })
            con.commit()
            self.clear()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Hoàn thành", "Nhập học sinh thành công ")

    def fetch_data(self):
        con = sqlite3.connect("quanlihocsinh.db")
        cur = con.cursor()
        cur.execute("Select * from hocsinh")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.studenttable.delete(*self.studenttable.get_children())
            for row in rows:
                self.studenttable.insert('', END, values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        cursoror_row= self.studenttable.focus()
        content= self.studenttable.item(cursoror_row)
        row=content['values']
        self.idvar.set(row[0])
        self.namevar.set(row[1])
        self.emailvar.set(row[2])
        self.gendervar.set(row[3])
        self.contactvar.set(row[4])
        self.dobvar.set(row[5])
        self.addressvar.set(row[6])

    def updatedata(self):
        con=sqlite3.connect("quanlihocsinh.db")
        cursor=con.cursor()
        cursor.execute("UPDATE hocsinh SET id='" +
                       self.idvar.get() + "', name='" +
                       self.namevar.get() + "', email='" +
                       self.emailvar.get() + "', gender='" +
                       self.gendervar.get() + "', contact='" +
                       self.contactvar.get() + "' WHERE id='" +
                       self.idvar.get() + "' ")


        con.commit()
        con.close()
        self.clear()
        self.fetch_data()
        messagebox.showinfo("Hoàn thành", "Update thành công ")

    def clear(self):
        self.idvar.set("")
        self.namevar.set("")
        self.emailvar.set("")
        self.gendervar.set("")
        self.contactvar.set("")
        self.dobvar.set("")
        self.idvar.set("")
        self.addressvar.set("")
    def delete(self):
        con=sqlite3.connect("quanlihocsinh.db")
        cursor=con.cursor()
        cursor.execute("DELETE FROM hocsinh where id =  "+str(self.idvar.get()))
        con.commit()
        con.close()
        self.clear()
        self.fetch_data()



    def search(self):
        con = sqlite3.connect("quanlihocsinh.db")
        cur = con.cursor()
        if self.searchbyvar.get()=="ID":
            cur.execute("select * from hocsinh where id="+str(self.searchvar.get()))
            rows=cur.fetchall()
            if len(rows) != 0:
                self.studenttable.delete(*self.studenttable.get_children())
                for row in rows:
                    self.studenttable.insert('', END, values=row)
                con.commit()
        if self.searchbyvar.get() == "PhoneNumber":
            cur.execute("select * from hocsinh where contact="+ str(self.searchvar.get()))
            rows = cur.fetchall()
            if len(rows) != 0:
                self.studenttable.delete(*self.studenttable.get_children())
                for row in rows:
                    self.studenttable.insert('', END, values=row)
                con.commit()

        con.close()

class Student():
    root=Tk()
    obj=Student(root)
    root.mainloop()


