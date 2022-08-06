from tkinter import *
from tkinter import messagebox
import sqlite3
ws=Tk()
ws.title("Register Form")
ws.config(bg='#9cf0e1')
f= ('Times',14)
var=StringVar()
var.set('male')
countries=[]
variable = StringVar()

right_frame=Frame(ws,bd=2,bg='#CCCCCC',relief=SOLID ,padx=10,pady=10)
Label(
    right_frame,text= "Họ tên:",bg='#CCCCCC', font=f
).grid(row=0,column=0,sticky=W,pady=10)
Label(
    right_frame,text= "Email:",bg='#CCCCCC', font=f
).grid(row=1,column=0,sticky=W,pady=10)
Label(
    right_frame,text= "Điện Thoại:",bg='#CCCCCC', font=f
).grid(row=2,column=0,sticky=W,pady=10)
Label(
    right_frame,text= "Giới tính:",bg='#CCCCCC', font=f
).grid(row=3,column=0,sticky=W,pady=10)
Label(
    right_frame,text= "Quốc Gia:",bg='#CCCCCC', font=f
).grid(row=4,column=0,sticky=W,pady=10)
Label(
    right_frame,text= "Password:",bg='#CCCCCC', font=f
).grid(row=5,column=0,sticky=W,pady=10)
Label(
    right_frame,text= "Re-Enter Password:",bg='#CCCCCC', font=f
).grid(row=6,column=0,sticky=W,pady=10)
gender_frame = LabelFrame(right_frame,bg='#CCCCCC',padx=10,pady=10)
txtName= Entry(right_frame,font=f)
txtEmail= Entry(right_frame,font=f)
txtMobile= Entry(right_frame,font=f)
male_rb= Radiobutton(gender_frame,text='Nam',bg='#CCCCCC',variable=var,value='male',font=('Times',10))
female_rb= Radiobutton(gender_frame,text='Nữ',bg='#CCCCCC',variable=var,value='female',font=('Times',10))
other_rb= Radiobutton(gender_frame,text='Khác',bg='#CCCCCC',variable=var,value='others',font=('Times',10))
txtCountry= Entry (right_frame,font=f)
txtPassword= Entry (right_frame,font=f,show='*')
txtconfirmpassword=Entry(right_frame,font=f,show='*')
def savedatabase():
    con=sqlite3.connect("account.db")
    cur = con.cursor()
    con.execute("insert into accounts values(:name,:email,:phone,:gender,:country,:password)",{
        'name': txtName.get(),
        'email': txtEmail.get(),
        'phone': txtMobile.get(),
        'gender': var.get(),
        'country':txtCountry.get(),
        'password': txtPassword.get()
    })
    con.commit()
def login():
    ws.destroy()
    import login

def validateform():
    if txtName.get() =="" or txtEmail.get()=="":
        messagebox.showerror("Lỗi","Bạn cần nhập đầy đủ")
        return
    elif txtMobile.get() =="" or  txtCountry.get() =="":
        messagebox.showerror("Lỗi","Bạn cần nhập đầy đủ")
        return
    elif txtPassword.get() =="" or txtconfirmpassword.get()=="":
        messagebox.showerror("Lỗi","Bạn cần nhập đầy đủ")
        return
    elif txtPassword.get() != txtconfirmpassword.get():
        messagebox.showerror("Lỗi","Mật khẩu không khớp nhau")
        txtPassword.focus_set()
        return
    else:
        messagebox.showinfo('Success',"Đăng kí tài khoản thành công!")
        savedatabase()
        login()
login_button= Button (right_frame,width=15, text='Login',font=f,relief=SOLID,cursor='hand2',command=login)
register_button= Button (right_frame,width=15, text='Register',font=f,relief=SOLID,cursor='hand2',command=validateform)
txtName.grid (row=0, column=1, pady=10,padx=20)
txtEmail.grid (row=1, column=1, pady=10,padx=20)
txtMobile.grid (row=2, column=1, pady=10,padx=20)
txtPassword.grid (row=5, column=1, pady=10,padx=20)
txtconfirmpassword.grid (row=6, column=1, pady=10,padx=20)
register_button.grid(row=7, column=1, pady=10,padx=20)
login_button.grid(row=7, column=0, pady=10,padx=20)

right_frame.pack()
gender_frame.grid(row=3, column=1, pady=10,padx=20)
txtCountry.grid(row=4, column=1, pady=10,padx=20)

male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
other_rb.pack(expand=True, side=LEFT)
ws.mainloop()







