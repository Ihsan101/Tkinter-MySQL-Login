from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os, sys
from sqlstuff import check, getdata, insertdata, updatepass
import random
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def userfocusing(e):
    user.delete(0, 'end')

def userunfocusing(e):
    if user.get() == '':
        user.insert(0, 'Username')

def passfocusing(e):
    passw.delete(0, 'end')

def passunfocusing(e):
    if passw.get() == '':
        passw.insert(0, 'Password')

def signingup():
        username = user2.get()
        e_mail = email.get()
        password = passw2.get()
        conpassword = conpassw.get()
        global data_user, data_pass, data_email, data_admin
        if username in data_user:
            messagebox.showerror("Invalid", "Given username is already taken, please choose a new one.")
        elif e_mail in data_email:
            messagebox.showerror("Invalid", "Given email is already being used, please choose a new one.")
        elif password == conpassword:
            insertdata(username, password, e_mail)
            messagebox.showinfo("Congrats!", "Your account has been succesfully created.")
            data_user, data_pass, data_email, data_admin = getdata()
            root2.destroy()
        else:
            messagebox.showerror("Invalid", "Passwords do not match. Please recheck the password that you have entered.")

#######------------------------------------------------SIGNING UP SYSTEM----------------------------------------------------------
def gosignup():

    #Username Focusing
    def user2focusing(e):
        user2.delete(0, 'end')

    def user2unfocusing(e):
        if user2.get() == '':
            user2.insert(0, 'Username')

    #Email Focusing
    def emailfocusing(e):
        email.delete(0, 'end')

    def emailunfocusing(e):
        if email.get() == '':
            email.insert(0, 'Email')

    #Password Focusing
    def pass2focusing(e):
        passw2.delete(0, 'end')

    def pass2unfocusing(e):
        if passw2.get() == '':
            passw2.insert(0, 'Password')
            
    #Confirm password focusing
    def conpassfocusing(e):
        conpassw.delete(0, 'end')

    def conpassunfocusing(e):
        if conpassw.get() == '':
            conpassw.insert(0, 'Confirm Password')
                


    global data_user, data_pass, data_admin, data_email, user2, email, passw2, conpassw, root2
    check()
    root2 = Toplevel(root)
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

    user2 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
    user2.place(x = 50, y = 80 )
    user2.insert(0, 'Username')
    user2.bind('<FocusIn>', user2focusing)
    user2.bind('<FocusOut>', user2unfocusing)

    Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 107)

    #Email area

    email = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
    email.place(x = 50, y = 140 )
    email.insert(0, 'Email')
    email.bind('<FocusIn>', emailfocusing)
    email.bind('<FocusOut>', emailunfocusing)

    Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 167)

    #Password area

    passw2 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
    passw2.place(x = 50, y = 200 )
    passw2.insert(0, 'Password')
    passw2.bind('<FocusIn>', pass2focusing)
    passw2.bind('<FocusOut>', pass2unfocusing)

    Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 227)

    #Confirm Password area

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
##################################################################################################################################
#######------------------------------------------------FORGOT PASSWORD SYSTEM------------------------------------------------------
def forgotpass():

    def passotpcheck():
        username = user3.get()
        password = passw3.get()
        data_pos = data_user.index(username)
        e_mail = data_email[data_pos]
        otpvalue = otp.get()
        if otpc == int(otpvalue):
            updatepass(username, password)
            messagebox.showinfo("NEW EMAIL", f"To {e_mail}, Your password has been updated")
            time.sleep(5)
            root3.destroy()
        else:
            messagebox.showerror("Invalid", "The OTP you provided is incorrect.")  
            time.sleep(5)
            root3.destroy()

        
    def otpcheck():
        global otp, otpc
        username = user3.get()
        data_pos = data_user.index(username)
        e_mail = data_email[data_pos]
        otpc = random.randint(1, 99999)
        messagebox.showinfo("NEW EMAIL", f"To {e_mail}, You have requested a password change. Your OTP is: {otpc}")
        root4 = Toplevel(root3)
        root4.title("OTP")
        root4.geometry("300x300+575+200")
        root4.config(bg = "#1c1c1c")
        root4.resizable(False, False)
        frame4 = Frame(root4, width = 300, height = 300, bg='#1c1c1c')
        frame4.place(x = 0, y = 0)
        
        #Main Heading
        heading = Label(frame4, text = 'Enter the OTP', fg = '#57a1f8', bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x = 50, y = 20)

        #OTP Check
        otp = Entry(frame4, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
        otp.place(x = 60, y = 130 )
        Frame(frame4, width = 200, height = 2, bg = 'white').place(x = 55, y = 157)

        #Button
        Button(frame4, width = 20, pady = 7, text = 'Check OTP', bg = '#57a1f8', fg = 'white', border = 0, command=passotpcheck).place(x= 80, y= 200)

        root4.mainloop()




    def passchange():
        username = user3.get()
        password = passw3.get()
        conpassword = conpassw3.get()
        if username in data_user:
            data_pos = data_user.index(username)
            if data_admin[data_pos] == 1:
                messagebox.showerror("Invalid", "You are an admin, you cannot change your password.")
            else:
                if password == conpassword:
                    data_pos = data_user.index(username)
                    if password != data_pass[data_pos]:
                        otpcheck()
                    else:
                        messagebox.showerror("Invalid", "You cannot enter a password that you have used previously, please type a new password.")
                else:
                    messagebox.showerror("Invalid", "The passwords you have provided do not match, please recheck your password.")


    root3 = Toplevel(root)
    root3.title("Forgot Password")
    root3.geometry("400x500+575+200")
    root3.config(bg = "#1c1c1c")
    root3.resizable(False, False)

    frame = Frame(root3, width = 400, height = 500, bg='#1c1c1c')
    frame.place(x = 0, y = 0)

    #Main Heading
    heading = Label(frame, text = 'Forgot Password?', fg = '#57a1f8', bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x = 65, y = 20)


    #Username area

    #Username Focusing
    def user3focusing(e):
        user3.delete(0, 'end')

    def user3unfocusing(e):
        if user3.get() == '':
            user3.insert(0, 'Username')
    user3 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
    user3.place(x = 50, y = 130 )
    user3.insert(0, 'Username')
    user3.bind('<FocusIn>', user3focusing)
    user3.bind('<FocusOut>', user3unfocusing)

    Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 157)

    #Password area
    #Password Focusing
    def pass3focusing(e):
        passw3.delete(0, 'end')

    def pass3unfocusing(e):
        if passw3.get() == '':
            passw3.insert(0, 'New password')

    passw3 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
    passw3.place(x = 50, y = 200 )
    passw3.insert(0, 'New password')
    passw3.bind('<FocusIn>', pass3focusing)
    passw3.bind('<FocusOut>', pass3unfocusing)

    Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 227)

    #Confirm Password area

    def conpass3focusing(e):
        conpassw3.delete(0, 'end')

    def conpass3unfocusing(e):
        if conpassw3.get() == '':
            conpassw3.insert(0, 'Confirm Password')
            

    conpassw3 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
    conpassw3.place(x = 50, y = 260 )
    conpassw3.insert(0, 'Confirm Password')
    conpassw3.bind('<FocusIn>', conpass3focusing)
    conpassw3.bind('<FocusOut>', conpass3unfocusing)

    Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 287)

    #Reset Password Button
    Button(frame, width = 39, pady = 7, text = 'Reset Password*', bg = '#57a1f8', fg = 'white', border = 0, command=passchange).place(x= 45, y= 314)

    forgotpass_text = Label(frame, text = '*An OTP will be sent to your registered email.', fg = 'white',bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 9))
    forgotpass_text.place(x = 73, y = 365)

    root3.mainloop()
##################################################################################################################################

def signin():
    username = user.get()
    password = passw.get()
    if username not in data_user:
        messagebox.showerror("Invalid", "Given username is not stored in database. Please register first.")
    elif username in data_user:
        data_pos = data_user.index(username)
        if password == data_pass[data_pos]:
            window = Toplevel(root)
            window.title = 'Logged In!'
            window.geometry("1300x500+100+200")
            window.config(bg = "#1c1c1c")
            Label(window, text = 'Congrats!, You\'ve succesfully signed in!', bg = '#1c1c1c', font =('Calibri(Body)', 50 , 'bold')).pack(expand=True)
        else:
           messagebox.showerror("Invalid", "Incorrect password.") 
    else:
        messagebox.showerror("Invalid", "Incorrect username or password.")



check()
data_user, data_pass, data_email, data_admin = getdata()


root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.config(bg = "#1c1c1c")
root.resizable(False, False)


img = ImageTk.PhotoImage(file = resource_path('image.png'))
Label(root, image = img, bg = '#1c1c1c').place(x = 50, y = 50)

frame = Frame(root, width = 350, height = 350, bg='#1c1c1c')
frame.place(x = 480, y = 70)


#Main Heading
heading = Label(frame, text = 'Sign in', fg = '#57a1f8', bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x = 135, y = 5)

#Username area

user = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
user.place(x = 50, y = 80 )
user.insert(0, 'Username')
user.bind('<FocusIn>', userfocusing)
user.bind('<FocusOut>', userunfocusing)

Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 107)

#Password area

passw = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))
passw.place(x = 50, y = 150 )
passw.insert(0, 'Password')
passw.bind('<FocusIn>', passfocusing)
passw.bind('<FocusOut>', passunfocusing)
passw_text = Button(frame, width = 17, text = 'Forgot Password?', border = 0, fg = '#57a1f8', bg = '#1c1c1c', cursor='hand2', command = forgotpass, font = ('Microsoft YaHei UI Light', 8))
passw_text.place(x= 250, y = 180)

Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 177)

#Sign in Button
Button(frame, width = 39, pady = 7, text = 'Sign in', bg = '#57a1f8', fg = 'white', border = 0, command = signin).place(x= 45, y= 214)

#Dont have an account sign up thing
signup_text = Label(frame, text = 'Don\'t have an account?', fg = 'white',bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 9))
signup_text.place(x = 95, y = 280)

signup = Button(frame, width = 6, text = 'Sign up!', border = 0, fg = '#57a1f8', bg = '#1c1c1c', cursor='hand2', command = gosignup)
signup.place(x= 235, y = 276.25)

root.mainloop()
