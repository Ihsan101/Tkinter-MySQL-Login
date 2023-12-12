#Designing a login system with forget password, registration and login. 

#ADMIN PASS = verysecretadminpass

#Not really as important, just added this module so i can add a small delay between each input
import time
#Used this module for OTP. 
import random
#prettytable and mysql.connector must be installed using pip before running the program. 
import prettytable as pt
import mysql.connector as sql

#Youll see this later in the program. Mainly used this to check if they didnt make any typos in password, so it asks them to type it twice. 
def checkitem(x):
    y,z = [".",""]
    while y != z:
        print(f'''
Please enter your {x}:''')
        y = input()
        print(f'''
Please confirm your{x}''')
        z = input()
        if y == z:
            return(y)
        else:
            print(f'''
            Data provided does not match, please re-enter your {x}.''')

#This function i used to check if the otp they typed was the correct one they have received. 
def otpsys(x):
    while True:
        otpc = int(input('''Enter the OTP you have received in your email:
        '''))
        if x == otpc:
            print('''
            The OTP you have entered is correct!
            ''')
            time.sleep(1)
            return True
            break
        else:
            print('''
            "The OTP you have entered is incorrect!. Please re-enter the OTP.)
            ''')

def getdata(connec):
    curs = connec.cursor()
    #first, I retreive all values in records.
    curs.execute("USE school")
    curs.execute("SELECT * FROM ihsanproj")
    data = curs.fetchall()
    data_user = [item[0] for item in data]
    data_pass = [item[1] for item in data]
    data_email = [item[2] for item in data]
    data_admin = [item[3] for item in data]
    curs.close()
    return data_user, data_pass, data_email, data_admin


con = sql.connect(host = "localhost", user = "root", passwd = "1234")
cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS school")
cur.execute("USE school")
cur.execute("SHOW TABLES")

results = cur.fetchall()
results_list = [item[0] for item in results]
con.commit()
if "ihsanproj" not in results_list:
    cur.execute('''USE school''')
    cur.execute('''CREATE TABLE ihsanproj (user VARCHAR(25) PRIMARY KEY,
pass VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL UNIQUE,
admin INT(1) NOT NULL DEFAULT 0)''')
    con.commit()
    cur.execute('''INSERT INTO ihsanproj VALUES("Ihsan", "2006!!!", "ihsanhashir@gmail.com", 1)''')
    cur.execute('''INSERT INTO ihsanproj VALUES("CPS", "cps@123", "chavaraschool@gmail.com", 1)''')
    cur.execute('''INSERT INTO ihsanproj VALUES("Guy1", "Guy1Pass", "guy1@gmail.com", 0)''')
    cur.execute('''INSERT INTO ihsanproj VALUES("Guy2", "Guy2Pass", "guy2@gmail.com", 0)''')

con.commit()
cur.close()


#First thing which will be shown when the program is run.
print("Welcome to ABCD")
data_user, data_pass, data_email, data_admin = getdata(con)
while True:
    time.sleep(1)
    print("Choose your required operation")
    op = input('''
    1. Registration
    2. Login
    3. Forgot password
    4. Exit
''')


    #REGISTRATION
    #I ran 2 conditions here, cuz I knew some idiots would just type out "registration" instead of typing 1 or something. So this checks if they typed in the number 1, or a word which starts with r. You will see this tactic used multiple times in this code. 
    if op == "1" or (op.lower())[0] == "r":

        print("\nRegistration selected \n")
        cur = con.cursor()
        time.sleep(1)
        while True:
            user = input("Enter your username: \n")
            if user in data_user:
                print(f"{user} is already in use, please enter another username: \n")
                time.sleep(1)
            else:
                break

        email = input("Enter your E-Mail: \n")
        #Calling the checkitem function which I had setup in line 27. 
        passw = checkitem("password")

        cur.execute(f'''INSERT INTO ihsanproj VALUES(%s, %s, %s, 0)''', [user, passw, email])
        con.commit()
        cur.close()
        data_user.append(user)
        data_pass.append(passw)
        data_email.append(email)
        data_admin.append(0)
        continue

    #LOGIN
    elif op == "2" or (op.lower())[0] == "l":
        print("\nLogin selected.")

        time.sleep(1)
        while True:
            user = input('''Enter your username:
''')
            if user in data_user:
                data_pos = data_user.index(user)
                passw = input('''Enter your password:
''')
                if passw == data_pass[data_pos]:
                    print("Login succesful. Now go do stuff which u can do in ABCD company :D\n")
                    time.sleep(1)
                    login = True
                    break
                else:
                    print("Password doesnt match given username. Please re-login.")
                    time.sleep(1)
                    continue
            else:
                print(f"{user} given is not registered. Please perform registration first. Ending login stage")
                time.sleep(1)
                break
        #Portal after login
        while login == True:
            time.sleep(1)
            print("Choose your required operation")
            print('''
            1. View very secret info ;)
            2. Password reset
            3. Email reset
            4. Become an admin user
            5. See all user info. **ADMIN ONLY**
            6. Logout
            7. Close portal''')

            po = input("")

            #View secret info
            if po == "1" or (po.lower())[0] == "v":
                print("\n Hello. You are viewing very secret info. Very very secret info which only ADCB company workers have. End of very secret info. ;D \n")

            elif po == "2" or (po.lower())[0] == "p":
                if data_admin[data_pos] == 1:
                    print("\nYou are an admin user. You cannot change your email.")
                else:
                    print("\n Reset password selected")
                    time.sleep(1)
                    print(f'''
                    Currently changing the password of {user}.
                    ''' )
                    data_pass[data_pos] = checkitem("password")
                    cur = con.cursor()
                    cur.execute("SELECT school")
                    cur.execute("UPDATE ihsanproj SET pass = %s WHERE user = %s",[data_pass[data_pos], user] )
                    con.commit()
                    cur.close()
                    print("\nYour password has been updated!")

            elif po == "3" or (po.lower())[0] == "e":
                if data_admin[data_pos] == 1:
                    print("\nYou are an admin user. You cannot change your email.")
                else:
                
                    print("\nReset email selected")
                    time.sleep(1)
                    print(f'''
                    Currently changing the email of {user}.
                    ''' )
                    data_email[data_pos] = checkitem("email")
                    cur = con.cursor()
                    cur.execute("SELECT school")
                    cur.execute("UPDATE ihsanproj SET email =%s WHERE user = %s",[data_email[data_pos], user] )
                    con.commit()
                    cur.close()
                    print("\nYour email has been updated!")

            elif po == "4" or (po.lower())[0] == "b":
                if data_admin[data_pos] == 1:
                    print("\nYou are already an admin user, what are you trying to do here???")
                else:
                    print("\nBecome an admin selected.")
                    print("To become an admin, you need to enter the admin password provided by the developer. Please enter the admin password:")
                    a = input("")
                    print("\nVerifying the entered password.")
                    time.sleep(1)
                    #This password is already set. You cant change it unless you change the source code, hence why its an admin pass. 
                    if a == "verysecretadminpass":
                        print(f"Congrats, {user}, you are now an admin user!")
                        data_admin[data_pos] = 1
                        cur = con.cursor()
                        cur.execute("SELECT school")
                        cur.execute("UPDATE ihsanproj SET admin = 1 WHERE user = %s",user )
                        con.commit()
                        cur.close()
            
                    else:
                        print(f"Entered admin password is incorrect. {user}, do not try to become an admin if you do not have permission. You will be executed, killed, destroyed, dead.")
                    

            elif po == "5" or (po.lower())[0] == "s":
                if data_admin[data_pos] == 1:
                    print("\nYou are now viewing the login information of all registered users. Please do not share this information.\nThis table will not show the information of admin users.\n")
                    time.sleep(1)
                    LoginInfo = pt.PrettyTable(["Username","Password", "Email"])
                    cur = con.cursor()
                    cur.execute("USE school")
                    cur.execute("SELECT user, pass, email FROM ihsanproj WHERE admin = 0")
                    data = cur.fetchall()
                    for i in data:
                        LoginInfo.add_row(i)
                    cur.close()
                    print(LoginInfo)
                    time.sleep(5)
                else:
                    print("\nYou are not an admin. Stop tryna scam this very wealthy ADCB company. You cannot steal our passwords ):<")
                    time.sleep(1)

            elif po == "6" or (po.lower())[0] == "l":
                print(f"\nLoggout in progress. Thank you for using our platform {user}.")
                time.sleep(1)
                login = False
                break

            elif po == "7" or (po.lower())[0] == "c":
                print(f"\nClosing the portal. Thank you for using our platform {user}.")
                time.sleep(1)
                exit()

            else:
                print("\nOperation entered is not in the given list. Please choose an appropriate operation.")
                

    #Forgot Password
    elif op == "3" or (op.lower())[0] == "f":
        print("\nForgot password selected.")
        time.sleep(1)
        while True:
            user = input("Enter your username: \n")
            if user in data_user:
                data_pos = data_user.index(user)
                cur_email = data_email[data_pos]
                if data_admin[data_pos] == 1:
                    print("\nYou are an admin user, you cannot change your password. Rewrite the program to change your password.")
                    print("Ending forgetting password stage.")
                    time.sleep(1)
                    break

                print(f"\nAn OTP has been sent to your email,{cur_email}. Please input the OTP that you receive.")
                time.sleep(1)
                print("\nI am not integrating an API to send you a mail, so here is the very secure very unbreakable system to change your password :) \n")
                time.sleep(1)
                otp = random.randint(1, 99999)

                print("To:",cur_email)
                print(f"The OTP for you to reset your password is {otp}\n" )
                time.sleep(1)

                a = otpsys(otp)
                if a == True:
                    data_pass[data_pos] = checkitem("password")
                    cur = con.cursor()
                    cur.execute("SELECT school")
                    cur.execute("UPDATE ihsanproj SET pass = %s WHERE user = %s",[data_pass[data_pos], user] )
                    con.commit()
                    cur.close()
                    print("\nYour password has been updated!")
                    print("Password has been updated. You can now login to your account.")
                    break
            
    elif op == "4" or (op.lower())[0] == "e":
        print("\nThank you for using the portal. Exiting the program.")
        time.sleep(1)
        exit()
    else:
        print("\nOperation entered is not in the given list. Please choose an appropriate operation.")
