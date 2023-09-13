import mysql.connector as sql

def check():
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
    con.close()

def getdata():
    con = sql.connect(host = "localhost", user = "root", passwd = "1234", database = 'school')
    cur = con.cursor()
    cur.execute("SELECT * FROM ihsanproj")
    data = cur.fetchall()
    data_user = [item[0] for item in data]
    data_pass = [item[1] for item in data]
    data_email = [item[2] for item in data]
    data_admin = [item[3] for item in data]
    cur.close()
    con.close()
    return data_user, data_pass, data_email, data_admin
    
def insertdata(x, y, z):
    con = sql.connect(host = "localhost", user = "root", passwd = "1234", database = 'school')
    cur = con.cursor(buffered=True)
    cur.execute(f'''INSERT INTO ihsanproj VALUES(%s, %s, %s, 0)''', [x, y, z])
    con.commit()
    cur.close()
    con.close()

def updatepass(x, y):
    con = sql.connect(host = "localhost", user = "root", passwd = "1234", database = 'school')
    cur = con.cursor(buffered=True)
    cur.execute("UPDATE ihsanproj SET pass = %s WHERE user = %s", [y, x])
    con.commit()
    cur.close()
    con.close()