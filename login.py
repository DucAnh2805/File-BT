from tkinter import *
import sqlite3
from tkinter import messagebox
ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#0B5A81')

f = ('Times', 14)
def afterlogin():
    ws.destroy()
    import main

def register():
    ws.destroy()
    import register
def log():
    con=sqlite3.connect("account.db")
    cursor=con.cursor()
    cursor.execute("select * from accounts where email=? and password=?",(email_input.get(),password_input.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('Info','Đăng nhập thành công')
        afterlogin()
    else:
        messagebox.showerror('Info','Tài khoản hoặc mật khẩu không hợp lệ')
    con.commit()
    con.close()




login = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
    )

Label(
    login,
    text="Enter Email",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    login,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)
email_input=StringVar()
password_input=StringVar()
email_tf = Entry(
    login,
    font=f,
    textvariable=email_input

    )
pwd_tf = Entry(
    login,
    font=f,
    show='*',
    textvariable=password_input
    )
login_btn = Button(
    login,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=log
    )
Register_btn=Button(
    login,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=register
    )


email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
Register_btn.grid(row=2, column=0, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)

login.pack()


ws.mainloop()