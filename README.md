**COMPUTER SCIENCE PROJECT DOCUMENTATION**

![](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.001.png)

|![Raised hand with solid fill]|<p>*The given project documentation goes through the overview of the Python program created by our team to provide a login portal for users to easily Sign up, sign in and interact with the GUI of the program, while storing all details into a MySQL database.* </p><p></p>|
| - | :- |

# **INDEX**

|||
| :-: | :- |

|**Sn No.**|**CONTENT**|**Page No.**|
| :- | :- | :- |
|***1.***|*System Requirements*|*1*|
|***2.***|*Introduction*|*2*|
|***3.***|*Source Code*|*4*|
|***4.***|*Output*|*16*|
|***5.***|*References*|*18*|
|***6.***|*Conclusion*|*18*|

|||
| :-: | :- |
|||
|||
# **SYSTEM REQUIREMENTS**

|![Raised hand with solid fill]|<p>*The basic system requirements to run our program are given below, including OS Version, Modules to be downloaded, etc.* </p><p></p>|
| :-: | :- |

|**	|<p>**Minimum System**</p><p>**Requirements**</p>|**Recommended System Requirements**|
| :- | :-: | :-: |
|**Processor**|1 GHz Clock speed|1\.5 – 2 GHz Clock speed|
|**Disk Space/Storage**|1 GB|2-3 GB|
|**Memory**|1 GB|2 GB|
|**OS**|<p>Windows: 7+</p><p>MacOS: 10.11 or higher, 64-bit</p><p>Linux: RHEL 6/7 64-bit</p>||
|**Modules**|tkinter, MySQL-Connector, os, sys, pillow, random, time \*||

**\*The following modules must be installed using pip before the running of the project to ensure no module errors can arise during runtime**











# **INTRODUCTION**

|![Raised hand with solid fill]|*The given computer science project uses tkinter to create a basic GUI containing a login, sign up and forgot password system. Account data is then stored in a database created in MySQL.*|
| :-: | :- |

The program consists of 2 .py files, splitting the main GUI code into main.py and containing all database related connections into the sqlstuff.py files. The program uses:

- The **tkinter** module for the basic GUI, 

- The **mysql.connector** module provides a connection between the python program and MySQL Database. 

- The **PIL** module helps process and display PNG files properly.

- The **os** and **sys** module to help retrieve the exact location of the PNG file to be displayed in the GUI.

- The **random** module to generate a random 5-digit number as an OTP for the “Forgot Password” function. 

- The time module is primarily used to make the program sleep for a while, to provide a delay between individual functions being run. 

All of these modules work together to create a memory efficient, low runtime program which is able to provide a basic interface for a login portal. 


|![Raised hand with solid fill]|*Development*|
| :-: | :- |

This project has seen multiple draft copies. Primarily, it was a console driven menu program, with all user data being stored in a dictionary in python itself. This caused the deletion of data the moment the program was closed, so it was heavily unoptimized for general use in real life scenarios. 

The second draft incorporated mysql.connector to help store the user data in a database, so that users information can be securely stored in an external database. In a proper scenario, the directory for this database would be an external server, however since that is out of the scope of this project, databases created shall be stored in the computer running the program. 

Finally, we incorporated tkinter to provide a simple but user-friendly GUI so that all features of our project can be easily accessed by anyone who wants to use our program. 

|![Raised hand with solid fill]|*Flowchart*|
| :-: | :- |

![](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.003.png)

















# **SOURCE CODE**
The following image contains the directory of our computer science project. The project can be downloaded from this GitHub Link: <https://github.com/Ihsan101/Tkinter-MySQL-Login>

This is what the directory of our project looks like:

![](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.004.png)

|![Raised hand with solid fill]|*This is the contents of **main.py**:*|
| :-: | :- |

from tkinter import \*

from tkinter import messagebox

from PIL import ImageTk, Image

import os, sys

from sqlstuff import check, getdata, insertdata, updatepass

import random

import time

def resource\_path(relative\_path):

`    `try:

`        `base\_path = sys.\_MEIPASS

`    `except Exception:

`        `base\_path = os.path.dirname(os.path.abspath(\_\_file\_\_))

`    `return os.path.join(base\_path, relative\_path)

def userfocusing(e):

`    `user.delete(0, 'end')

def userunfocusing(e):

`    `if user.get() == '':

`        `user.insert(0, 'Username')

def passfocusing(e):

`    `passw.delete(0, 'end')

def passunfocusing(e):

`    `if passw.get() == '':

`        `passw.insert(0, 'Password')

def signingup():

`        `username = user2.get()

`        `e\_mail = email.get()

`        `password = passw2.get()

`        `conpassword = conpassw.get()

`        `global data\_user, data\_pass, data\_email, data\_admin

`        `if username in data\_user:

`            `messagebox.showerror("Invalid", "Given username is already taken, please choose a new one.")

`        `elif e\_mail in data\_email:

`            `messagebox.showerror("Invalid", "Given email is already being used, please choose a new one.")

`        `elif password == conpassword:

`            `insertdata(username, password, e\_mail)

`            `messagebox.showinfo("Congrats!", "Your account has been succesfully created.")

`            `data\_user, data\_pass, data\_email, data\_admin = getdata()

`            `root2.destroy()

`        `else:

`            `messagebox.showerror("Invalid", "Passwords do not match. Please recheck the password that you have entered.")

#######------------------------------------------------SIGNING UP SYSTEM----------------------------------------------------------

def gosignup():

`    `#Username Focusing

`    `def user2focusing(e):

`        `user2.delete(0, 'end')

`    `def user2unfocusing(e):

`        `if user2.get() == '':

`            `user2.insert(0, 'Username')

`    `#Email Focusing

`    `def emailfocusing(e):

`        `email.delete(0, 'end')

`    `def emailunfocusing(e):

`        `if email.get() == '':

`            `email.insert(0, 'Email')

`    `#Password Focusing

`    `def pass2focusing(e):

`        `passw2.delete(0, 'end')

`    `def pass2unfocusing(e):

`        `if passw2.get() == '':

`            `passw2.insert(0, 'Password')



`    `#Confirm password focusing

`    `def conpassfocusing(e):

`        `conpassw.delete(0, 'end')

`    `def conpassunfocusing(e):

`        `if conpassw.get() == '':

`            `conpassw.insert(0, 'Confirm Password')



`    `global data\_user, data\_pass, data\_admin, data\_email, user2, email, passw2, conpassw, root2

`    `check()

`    `root2 = Toplevel(root)

`    `root2.title("Sign up")

`    `root2.geometry("925x500+300+200")

`    `root2.config(bg = "#1c1c1c")

`    `root2.resizable(False, False)

`    `img = ImageTk.PhotoImage(file = resource\_path('image2.png'))

`    `Label(root2, image = img, bg = '#1c1c1c').place(x = 0, y = 40)

`    `frame = Frame(root2, width = 350, height = 430, bg='#1c1c1c')

`    `frame.place(x = 500, y = 50)

`    `#Main Heading

`    `heading = Label(frame, text = 'Sign up', fg = '#57a1f8', bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 23, 'bold'))

`    `heading.place(x = 135, y = 5)

`    `#Username area

`    `user2 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`    `user2.place(x = 50, y = 80 )

`    `user2.insert(0, 'Username')

`    `user2.bind('<FocusIn>', user2focusing)

`    `user2.bind('<FocusOut>', user2unfocusing)

`    `Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 107)

`    `#Email area

`    `email = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`    `email.place(x = 50, y = 140 )

`    `email.insert(0, 'Email')

`    `email.bind('<FocusIn>', emailfocusing)

`    `email.bind('<FocusOut>', emailunfocusing)

`    `Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 167)

`    `#Password area

`    `passw2 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`    `passw2.place(x = 50, y = 200 )

`    `passw2.insert(0, 'Password')

`    `passw2.bind('<FocusIn>', pass2focusing)

`    `passw2.bind('<FocusOut>', pass2unfocusing)

`    `Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 227)

`    `#Confirm Password area

`    `conpassw = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`    `conpassw.place(x = 50, y = 260 )

`    `conpassw.insert(0, 'Confirm Password')

`    `conpassw.bind('<FocusIn>', conpassfocusing)

`    `conpassw.bind('<FocusOut>', conpassunfocusing)

`    `Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 287)

`    `#Sign up Button

`    `Button(frame, width = 39, pady = 7, text = 'Sign up', bg = '#57a1f8', fg = 'white', border = 0, command= signingup).place(x= 45, y= 314)

`    `#Have an account sign in thing

`    `signin\_text = Label(frame, text = 'Have an account already?', fg = 'white',bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 9))

`    `signin\_text.place(x = 95, y = 370)

`    `signin = Button(frame, width = 6, text = 'Sign in!', border = 0, fg = '#57a1f8', bg = '#1c1c1c', cursor='hand2', command = root2.destroy)

`    `signin.place(x= 240, y = 366.25)




`    `root2.mainloop()

##################################################################################################################################

#######------------------------------------------------FORGOT PASSWORD SYSTEM------------------------------------------------------

def forgotpass():

`    `def passotpcheck():

`        `username = user3.get()

`        `password = passw3.get()

`        `data\_pos = data\_user.index(username)

`        `e\_mail = data\_email[data\_pos]

`        `otpvalue = otp.get()

`        `if otpc == int(otpvalue):

`            `updatepass(username, password)

`            `messagebox.showinfo("NEW EMAIL", f"To {e\_mail}, Your password has been updated")

`            `time.sleep(5)

`            `root3.destroy()

`        `else:

`            `messagebox.showerror("Invalid", "The OTP you provided is incorrect.")  

`            `time.sleep(5)

`            `root3.destroy()



`    `def otpcheck():

`        `global otp, otpc

`        `username = user3.get()

`        `data\_pos = data\_user.index(username)

`        `e\_mail = data\_email[data\_pos]

`        `otpc = random.randint(1, 99999)

`        `messagebox.showinfo("NEW EMAIL", f"To {e\_mail}, You have requested a password change. Your OTP is: {otpc}")

`        `root4 = Toplevel(root3)

`        `root4.title("OTP")

`        `root4.geometry("300x300+575+200")

`        `root4.config(bg = "#1c1c1c")

`        `root4.resizable(False, False)

`        `frame4 = Frame(root4, width = 300, height = 300, bg='#1c1c1c')

`        `frame4.place(x = 0, y = 0)



`        `#Main Heading

`        `heading = Label(frame4, text = 'Enter the OTP', fg = '#57a1f8', bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 23, 'bold'))

`        `heading.place(x = 50, y = 20)

`        `#OTP Check

`        `otp = Entry(frame4, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`        `otp.place(x = 60, y = 130 )

`        `Frame(frame4, width = 200, height = 2, bg = 'white').place(x = 55, y = 157)

`        `#Button

`        `Button(frame4, width = 20, pady = 7, text = 'Check OTP', bg = '#57a1f8', fg = 'white', border = 0, command=passotpcheck).place(x= 80, y= 200)

`        `root4.mainloop()





`    `def passchange():

`        `username = user3.get()

`        `password = passw3.get()

`        `conpassword = conpassw3.get()

`        `if username in data\_user:

`            `data\_pos = data\_user.index(username)

`            `if data\_admin[data\_pos] == 1:

`                `messagebox.showerror("Invalid", "You are an admin, you cannot change your password.")

`            `else:

`                `if password == conpassword:

`                    `data\_pos = data\_user.index(username)

`                    `if password != data\_pass[data\_pos]:

`                        `otpcheck()

`                    `else:

`                        `messagebox.showerror("Invalid", "You cannot enter a password that you have used previously, please type a new password.")

`                `else:

`                    `messagebox.showerror("Invalid", "The passwords you have provided do not match, please recheck your password.")

`        `else:

`            `messagebox.showerror("Invalid", "The given username does not exist in the database!")

`    `root3 = Toplevel(root)

`    `root3.title("Forgot Password")

`    `root3.geometry("400x500+575+200")

`    `root3.config(bg = "#1c1c1c")

`    `root3.resizable(False, False)

`    `frame = Frame(root3, width = 400, height = 500, bg='#1c1c1c')

`    `frame.place(x = 0, y = 0)

`    `#Main Heading

`    `heading = Label(frame, text = 'Forgot Password?', fg = '#57a1f8', bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 23, 'bold'))

`    `heading.place(x = 65, y = 20)

`    `#Username area

`    `#Username Focusing

`    `def user3focusing(e):

`        `user3.delete(0, 'end')

`    `def user3unfocusing(e):

`        `if user3.get() == '':

`            `user3.insert(0, 'Username')

`    `user3 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`    `user3.place(x = 50, y = 130 )

`    `user3.insert(0, 'Username')

`    `user3.bind('<FocusIn>', user3focusing)

`    `user3.bind('<FocusOut>', user3unfocusing)

`    `Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 157)

`    `#Password area

`    `#Password Focusing

`    `def pass3focusing(e):

`        `passw3.delete(0, 'end')

`    `def pass3unfocusing(e):

`        `if passw3.get() == '':

`            `passw3.insert(0, 'New password')

`    `passw3 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`    `passw3.place(x = 50, y = 200 )

`    `passw3.insert(0, 'New password')

`    `passw3.bind('<FocusIn>', pass3focusing)

`    `passw3.bind('<FocusOut>', pass3unfocusing)

`    `Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 227)

`    `#Confirm Password area

`    `def conpass3focusing(e):

`        `conpassw3.delete(0, 'end')

`    `def conpass3unfocusing(e):

`        `if conpassw3.get() == '':

`            `conpassw3.insert(0, 'Confirm Password')



`    `conpassw3 = Entry(frame, width = 25, fg = 'white', border = 0, bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 11))

`    `conpassw3.place(x = 50, y = 260 )

`    `conpassw3.insert(0, 'Confirm Password')

`    `conpassw3.bind('<FocusIn>', conpass3focusing)

`    `conpassw3.bind('<FocusOut>', conpass3unfocusing)

`    `Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 287)

`    `#Reset Password Button

`    `Button(frame, width = 39, pady = 7, text = 'Reset Password\*', bg = '#57a1f8', fg = 'white', border = 0, command=passchange).place(x= 45, y= 314)

`    `forgotpass\_text = Label(frame, text = '\*An OTP will be sent to your registered email.', fg = 'white',bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 9))

`    `forgotpass\_text.place(x = 73, y = 365)

`    `root3.mainloop()

##################################################################################################################################

def signin():

`    `username = user.get()

`    `password = passw.get()

`    `if username not in data\_user:

`        `messagebox.showerror("Invalid", "Given username is not stored in database. Please register first.")

`    `elif username in data\_user:

`        `data\_pos = data\_user.index(username)

`        `if password == data\_pass[data\_pos]:

`            `window = Toplevel(root)

`            `window.title = 'Logged In!'

`            `window.geometry("1300x500+100+200")

`            `window.config(bg = "#1c1c1c")

`            `Label(window, text = 'Congrats!, You\'ve succesfully signed in!', bg = '#1c1c1c', font =('Calibri(Body)', 50 , 'bold')).pack(expand=True)

`        `else:

`           `messagebox.showerror("Invalid", "Incorrect password.") 

`    `else:

`        `messagebox.showerror("Invalid", "Incorrect username or password.")




check()

data\_user, data\_pass, data\_email, data\_admin = getdata()

root = Tk()

root.title("Login")

root.geometry("925x500+300+200")

root.config(bg = "#1c1c1c")

root.resizable(False, False)

img = ImageTk.PhotoImage(file = resource\_path('image.png'))

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

passw\_text = Button(frame, width = 17, text = 'Forgot Password?', border = 0, fg = '#57a1f8', bg = '#1c1c1c', cursor='hand2', command = forgotpass, font = ('Microsoft YaHei UI Light', 8))

passw\_text.place(x= 250, y = 180)

Frame(frame, width = 305, height = 2, bg = 'white').place(x = 45, y = 177)

#Sign in Button

Button(frame, width = 39, pady = 7, text = 'Sign in', bg = '#57a1f8', fg = 'white', border = 0, command = signin).place(x= 45, y= 214)

#Dont have an account sign up thing

signup\_text = Label(frame, text = 'Don\'t have an account?', fg = 'white',bg = '#1c1c1c', font = ('Microsoft YaHei UI Light', 9))

signup\_text.place(x = 95, y = 280)

signup = Button(frame, width = 6, text = 'Sign up!', border = 0, fg = '#57a1f8', bg = '#1c1c1c', cursor='hand2', command = gosignup)

signup.place(x= 235, y = 276.25)

root.mainloop()


|![Raised hand with solid fill]|*This is the contents of **sqlstuff.py**:*|
| :-: | :- |

import mysql.connector as sql

def check():

`    `con = sql.connect(host = "localhost", user = "root", passwd = "1234")

`    `cur = con.cursor()

`    `cur.execute("CREATE DATABASE IF NOT EXISTS school")

`    `cur.execute("USE school")

`    `cur.execute("SHOW TABLES")

`    `results = cur.fetchall()

`    `results\_list = [item[0] for item in results]

`    `con.commit()

`    `if "ihsanproj" not in results\_list:

`        `cur.execute('''USE school''')

`        `cur.execute('''CREATE TABLE ihsanproj (user VARCHAR(25) PRIMARY KEY,

`    `pass VARCHAR(50) NOT NULL,

`    `email VARCHAR(50) NOT NULL UNIQUE,

`    `admin INT(1) NOT NULL DEFAULT 0)''')

`        `con.commit()

`        `cur.execute('''INSERT INTO ihsanproj VALUES("Ihsan", "2006!!!", "ihsanhashir@gmail.com", 1)''')

`        `cur.execute('''INSERT INTO ihsanproj VALUES("CPS", "cps@123", "chavaraschool@gmail.com", 1)''')

`        `cur.execute('''INSERT INTO ihsanproj VALUES("Guy1", "Guy1Pass", "guy1@gmail.com", 0)''')

`        `cur.execute('''INSERT INTO ihsanproj VALUES("Guy2", "Guy2Pass", "guy2@gmail.com", 0)''')

`    `con.commit()

`    `cur.close()

`    `con.close()

def getdata():

`    `con = sql.connect(host = "localhost", user = "root", passwd = "1234", database = 'school')

`    `cur = con.cursor()

`    `cur.execute("SELECT \* FROM ihsanproj")

`    `data = cur.fetchall()

`    `data\_user = [item[0] for item in data]

`    `data\_pass = [item[1] for item in data]

`    `data\_email = [item[2] for item in data]

`    `data\_admin = [item[3] for item in data]

`    `cur.close()

`    `con.close()

`    `return data\_user, data\_pass, data\_email, data\_admin



def insertdata(x, y, z):

`    `con = sql.connect(host = "localhost", user = "root", passwd = "1234", database = 'school')

`    `cur = con.cursor(buffered=True)

`    `cur.execute(f'''INSERT INTO ihsanproj VALUES(%s, %s, %s, 0)''', [x, y, z])

`    `con.commit()

`    `cur.close()

`    `con.close()

def updatepass(x, y):

`    `con = sql.connect(host = "localhost", user = "root", passwd = "1234", database = 'school')

`    `cur = con.cursor(buffered=True)

`    `cur.execute("UPDATE ihsanproj SET pass = %s WHERE user = %s", [y, x])

`    `con.commit()

`    `cur.close()

`    `con.close()























# ![A screenshot of a login screen

Description automatically generated](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.005.png)![A screenshot of a login form

Description automatically generated](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.006.png)![](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.007.png)**OUTPUT**

|![Raised hand with solid fill]|*Given below are screenshots of the program running properly.* |
| :-: | :- |



![A white background with black text

Description automatically generated](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.008.png)





![A screenshot of a message

Description automatically generated](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.009.png)	




![A screenshot of a computer screen

Description automatically generated](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.010.png)





![A white background with black text

Description automatically generated](Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.011.png)





# **CONCLUSIONS**

|![Raised hand with solid fill]|*Concluding our project, we share that:*|
| :-: | :- |

This project has helped us learn the basics of tkinter and mysql-connector. It has showed us how we can combine our knowledge on Relational Database Management Systems with a high-level programming language like python to create a user-friendly interface which is simple, yet efficient, in the work it has been assigned to do. 

Our project has cleverly used tkinter and other common python modules to make a project which we are proud to present. Our project has gone beyond what was taught in the classroom and has showed us the limitless capabilities of what can be achieved with programming. 

We thank our computer teacher, Mr. Prajeesh, who has helped us learn the basics of this programming language and provide the inspiration to go past our traditional books to achieve something truly remarkable. We also thank our wonderful principal, Father Sabu, for giving us this opportunity to learn and grow in Chavara Public School, Pala. 
# **REFERENCES**

|![Raised hand with solid fill]|*We have used multiple external documentations and books to create this project, some of them being:* |
| :-: | :- |

- **NCERT** Computer Science Textbook for Class XI/XII.

- **APC Books**, Textbook of Computer Science with Python, Grade XII.

- Python [tkinter module documentation](https://docs.python.org/3/library/tkinter.html).
  - <https://docs.python.org/3/library/tkinter.html>

- [StackOverflow](https://stackoverflow.com) for common questions and queries.
  - <https://stackoverflow.com/>

- [Geek4Geeks](http://www.geeksforgeeks.org/) for in-depth documentation with examples.
  - <http://www.geeksforgeeks.org/>

- [LeetCode](https://leetcode.com/problemset/all/) to practice the functions we’ve learned in different types of problems.
  - <https://leetcode.com/problemset/all/>
**2 **|** Page									   Login Portal

[Raised hand with solid fill]: Aspose.Words.d4a312bd-b8c8-4e77-9882-881c971574ed.002.png
