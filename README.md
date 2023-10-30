<a name="br1"></a> 

**COMPUTER SCIENCE PROJECT**

**DOCUMENTATION**

*The given project documentation goes through the overview of the Python program*

*created by our team to provide a login portal for users to easily Sign up, sign in and*

*interact with the GUI of the program, while storing all details into a MySQL database.*

**INDEX**

***1.***

***2.***

***3.***

***4.***

***5.***

***6.***

*System Requirements*

*Introduction*

*Source Code*

*Output*

*1*

*2*

*4*

*16*

*18*

*18*

*References*

*Conclusion*

**SYSTEM REQUIREMENTS**

*The basic system requirements to run our program are given below, including OS Version,*

*Modules to be downloaded, etc.*

L o g i n P o r t a l



<a name="br2"></a> 

**Minimum System**

**Requirements**

**Recommended System**

**Requirements**

**Processor**

**Disk Space/Storage**

**Memory**

1 GHz Clock speed

1\.5 – 2 GHz Clock speed

1 GB

1 GB

2-3 GB

2 GB

**OS**

Windows: 7+

MacOS: 10.11 or higher, 64-bit

Linux: RHEL 6/7 64-bit

**Modules**

tkinter, MySQL-Connector, os, sys, pillow, random, time \*

**\*The following modules must be installed using pip before the running of the project to ensure no module errors**

**can arise during runtime**

**INTRODUCTION**

*The given computer science project uses tkinter to create a basic GUI*

*containing a login, sign up and forgot password system. Account data is*

*then stored in a database created in MySQL.*

The program consists of 2 .py files, splitting the main GUI code into main.py and containing all

database related connections into the sqlstuff.py files. The program uses:

•

•

The **tkinter** module for the basic GUI,

The **mysql.connector** module provides a connection between the python program and

MySQL Database.

•

•

The **PIL** module helps process and display PNG files properly.

The **os** and **sys** module to help retrieve the exact location of the PNG file to be displayed

in the GUI.

•

•

The **random** module to generate a random 5-digit number as an OTP for the “Forgot

Password” function.

The time module is primarily used to make the program sleep for a while, to provide a

delay between individual functions being run.

All of these modules work together to create a memory efficient, low runtime program which is

able to provide a basic interface for a login portal.

**1 |** P a g e

L o g i n P o r t a l



<a name="br3"></a> 

*Development*

This project has seen multiple draft copies. Primarily, it was a console driven menu program,

with all user data being stored in a dictionary in python itself. This caused the deletion of data

the moment the program was closed, so it was heavily unoptimized for general use in real life

scenarios.

The second draft incorporated mysql.connector to help store the user data in a database, so

that users information can be securely stored in an external database. In a proper scenario, the

directory for this database would be an external server, however since that is out of the scope

of this project, databases created shall be stored in the computer running the program.

Finally, I incorporated tkinter to provide a simple but user-friendly GUI so that all features of

our project can be easily accessed by anyone who wants to use our program.

*Flowchart*

**2 |** P a g e

L o g i n P o r t a l



<a name="br4"></a> 

**OUTPUT**

*Given below are screenshots of the program running properly.*



<a name="br5"></a> 

**4 |** P a g e



<a name="br6"></a> 

**CONCLUSIONS**

*Concluding our project, we share that:*

This project has helped us learn the basics of tkinter and mysql-connector. It has showed us

how we can combine our knowledge on Relational Database Management Systems with a high-

level programming language like python to create a user-friendly interface which is simple, yet

efficient, in the work it has been assigned to do.

Our project has cleverly used tkinter and other common python modules to make a project

which we are proud to present. Our project has gone beyond what was taught in the classroom

and has showed us the limitless capabilities of what can be achieved with programming.

We thank our computer teacher, Mr. Prajeesh, who has helped us learn the basics of this

programming language and provide the inspiration to go past our traditional books to achieve

something truly remarkable. We also thank our wonderful principal, Father Sabu, for giving us

this opportunity to learn and grow in Chavara Public School, Pala.

**REFERENCES**

*We have used multiple external documentations and books to create*

*this project, some of them being:*

•

•

•

**NCERT** Computer Science Textbook for Class XI/XII.

**APC Books**, Textbook of Computer Science with Python, Grade XII.

Python [tkinter](https://docs.python.org/3/library/tkinter.html)[ ](https://docs.python.org/3/library/tkinter.html)[module](https://docs.python.org/3/library/tkinter.html)[ ](https://docs.python.org/3/library/tkinter.html)[documentation](https://docs.python.org/3/library/tkinter.html)[.](https://docs.python.org/3/library/tkinter.html)

o <https://docs.python.org/3/library/tkinter.html>

•

•

•

[StackOverflow](https://stackoverflow.com/)[ ](https://stackoverflow.com/)for common questions and queries.

o <https://stackoverflow.com/>

[Geek4Geeks](http://www.geeksforgeeks.org/)[ ](http://www.geeksforgeeks.org/)for in-depth documentation with examples.

o <http://www.geeksforgeeks.org/>

[LeetCode](https://leetcode.com/problemset/all/)[ ](https://leetcode.com/problemset/all/)to practice the functions we’ve learned in different types of problems.

o <https://leetcode.com/problemset/all/>

**5 |** P a g e

L o g i n P o r t a l

