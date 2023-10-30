

|![Raised hand with solid fill]|<p>*The given project documentation goes through the overview of the Python program created by me to provide a login portal for users to easily Sign up, sign in and interact with the GUI of the program, while storing all details into a MySQL database.* </p><p></p>|
| - | :- |

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

Finally, I incorporated tkinter to provide a simple but user-friendly GUI so that all features of our project can be easily accessed by anyone who wants to use our program. 

|![Raised hand with solid fill]|*Flowchart*|
| :-: | :- |

![](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.003.png)

# **OUTPUT**
|![Raised hand with solid fill]|*Given below are screenshots of the program running properly.* |
| :-: | :- |

![A screenshot of a login screen](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.004.png)
![A screenshot of a login form](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.005.png)
![](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.006.png)


![A white background with black text](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.007.png)





![A screenshot of a message](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.008.png)	




![A screenshot of a computer screen](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.009.png)





![A white background with black text](Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.010.png)




[Raised hand with solid fill]: Aspose.Words.5f9428f4-9848-452a-8362-ed691ebbebf9.002.png
