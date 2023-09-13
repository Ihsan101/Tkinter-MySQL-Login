from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os, sys
from sqlstuff import check, getdata, insertdata

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def signingup():
    username = user.get()
    e_mail = email.get()
    password = passw.get()
    conpassword = conpassw.get()
    global data_user, data_pass, data_email, data_admin
    if username in data_user:
        messagebox.showerror("Invalid", "Given username is already taken, please choose a new one.")
    elif password == conpassword:
        insertdata(username, password, e_mail)
        messagebox.showinfo("Congrats!", "You\'re account has been succesfully created. Please go back to the login page.")
        data_user, data_pass, data_email, data_admin = getdata()
    else:
        messagebox.showerror("Invalid", "Passwords do not match. Please recheck the password that you have entered.")



#Username Focusing
def userfocusing(e):
    user.delete(0, 'end')

def userunfocusing(e):
    if user.get() == '':
        user.insert(0, 'Username')

#Email Focusing
def emailfocusing(e):
    email.delete(0, 'end')

def emailunfocusing(e):
    if email.get() == '':
        email.insert(0, 'Email')

#Password Focusing
def passfocusing(e):
    passw.delete(0, 'end')

def passunfocusing(e):
    if passw.get() == '':
        passw.insert(0, 'Password')
        
#Confirm password focusing
def conpassfocusing(e):
    conpassw.delete(0, 'end')

def conpassunfocusing(e):
    if conpassw.get() == '':
        conpassw.insert(0, 'Confirm Password')
              

check()
data_user, data_pass, data_email, data_admin = getdata()

root2 = Tk()
root2.title("Sign up")
root2.geometry("925x500+300+200")
root2.config(bg = "#1c1c1c")
root2.resizable(False, False)

img = ImageTk.PhotoImage(file = resource_path('image2.png'))
Label(root2, image = img, bg = '#1c1c1c').place(x = 0, y = 40)

frame = Frame(root2, width = 350, height = 430, bg='#1c1c1c')
frame.place(x = 500, y = 50)

#Main Heading
heading = Label(frame, text = 'Sign up', fg = '#57a1f8', bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x = 135, y = 5)


#Username area

user = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
user.place(x = 50, y = 80 )
user.insert(0, 'Username')
user.bind('<FocusIn>', userfocusing)
user.bind('<FocusOut>', userunfocusing)

Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 107)

#Email area

email = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
email.place(x = 50, y = 140 )
email.insert(0, 'Email')
email.bind('<FocusIn>', emailfocusing)
email.bind('<FocusOut>', emailunfocusing)

Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 167)

#Password area

passw = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
passw.place(x = 50, y = 200 )
passw.insert(0, 'Password')
passw.bind('<FocusIn>', passfocusing)
passw.bind('<FocusOut>', passunfocusing)

Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 227)

#Confirm Password area

def conpassfocusing(e):
    conpassw.delete(0, 'end')

def conpassunfocusing(e):
    if conpassw.get() == '':
        conpassw.insert(0, 'Confirm Password')
        

conpassw = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
conpassw.place(x = 50, y = 260 )
conpassw.insert(0, 'Confirm Password')
conpassw.bind('<FocusIn>', conpassfocusing)
conpassw.bind('<FocusOut>', conpassunfocusing)

Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 287)

#Sign up Button
Button(frame, width = 39, pady = 7, text = 'Sign up', bg = '#57a1f8', fg = 'white', border = 0, command= signingup).place(x= 45, y= 314)


#Have an account sign in thing
signin_text = Label(frame, text = 'Have an account already?', fg = 'white',bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 9))
signin_text.place(x = 95, y = 370)

signin = Button(frame, width = 6, text = 'Sign in!', border = 0, fg = '#57a1f8', bg = '#1c1c1c', cursor='hand2', command = root2.destroy)
signin.place(x= 240, y = 366.25)



root2.mainloop()