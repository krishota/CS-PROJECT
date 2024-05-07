import mysql.connector
import Crime_Module
import time

Crime_Module.userlogin()
print(Crime_Module.ut)
if Crime_Module.ut=='Authorised Access':
    x=Crime_Module.user[1].title()+', '+Crime_Module.user[3].title()
    print('\nHi',x)
    if Crime_Module.user[7]!=None:
        s=str(Crime_Module.user[7])
        l1=s.split()
        print('Your last login was on ',l1[0],"at",l1[1],'\n')
    else:
        print ("This is your First Login")
    time.sleep(1)
    Crime_Module.aoptions()
else:
    time.sleep(1)
    Crime_Module.goptions()

