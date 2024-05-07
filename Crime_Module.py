import pickle
import mysql.connector
import time

obj=mysql.connector.connect(\
    host='localhost',
    database='GBI_RECORDS',
    user='root',
    password='SQL@1984')
c=obj.cursor()
q='SELECT FULL_NAME, DESIGNATION, DEPARTMENT FROM USER_LOGIN'
c.execute(q)
l=c.fetchall()

d={}
flag="red"
f=open('GBI_Records.dat','rb')
try:
    while True:
        x=pickle.load(f)
        for k in x:
            d[k]=x[k]
except EOFError:
    f.close()


def userlogin():
    global ut
    global user
    Q='SELECT * FROM USER_LOGIN'
    c.execute(Q)
    L=c.fetchall()

    print ("Welcome to the GBI Crime Records Dept.")
    print ("\nDo you wish to continue with authorized login?")
    print ("1. Yes")
    print ("2. No")
    print()
    x=str(input("Enter your choice: "))

    if  x=="2":
        ut='View Only Access'
    elif x=="1":
        for i in range(3):
            flag='not logged in'
            flag2="valid username"
            print('\nYou have',3-i,'attempt(s) to complete your login \n')
            u=str(input("Username: "))

            for i in L:
                if u in i:
                    break
            else:
                flag2="invalid username"
                print ("Invalid Username!")

            if flag2=="valid username":
                p=str(input("Password: "))
                for i in L:
                    if u==i[5] and p==i[6]:
                        ut='Authorised Access'
                        user=i
                        flag='logged in'
                        break
                else:
                    print('Incorrect Password!')
                if flag=='logged in':
                    q='UPDATE USER_LOGIN SET LAST_LOGGED_IN=CURRENT_TIMESTAMP WHERE USER_NAME=%s;'
                    c.execute(q,(u,))
                    obj.commit()
                    break
        else:
            print('\nYou have exceeded the number of login attempts \nRedirecting to View Only Access...\n')
            ut='View Only Access'
    else:
            print("\nInvalid Option")
            print("Auto-Redirecting to View Only Access...\n")
            time.sleep(2)
            ut='View Only Access'

def victim():
  global lv
  lv=[]
  print()
  print('Victim Details')
  lv.append(str(input('Name: ')))
  lv.append(str(input('Age: ')))
  lv.append(str(input('Gender: ')))
  lv.append(str(input('Address: ')))
  lv.append(str(input('Contact: ')))

def crime():
  global ch
  global dets
  print()
  print('Crime Details')
  ch=str(input('Charges Pressed against the Accused: '))
  dets=str(input('Enter the Details of the Crime (Date, Time, Location, Important Facts) briefly: ')).split(',')
  
def evidences():
  global de
  de={}
  lwn=[]
  print()
  print('Evidences')
  el=input('Enter the List of Comparison Samples: ')
  ec=el.split(',')
  if len(ec)==0:
    ec=["Nil"]
  nw=int(input('Enter the no. of Witnesses: '))
  print()
  for i in range(nw):
    lw=[]
    lw.append(str(input('Name: ')))
    lw.append(str(input('Age: ')))
    lw.append(str(input('Gender: ')))
    lw.append(str(input('Address: ')))
    lw.append(str(input('Contact: ')))
    lwn.append(lw)
  if nw==0:
    lwn+=['Nil']
  de['Comparison Samples (Forensic Evidence)']=ec
  de['Witness Details']=lwn

def i_suspects():
  global lsn
  lsn=[]
  print()
  print ("Suspect Details")
  ns=int(input('Enter the no. of Suspects: '))
  for i in range(ns):
    print()
    ls=[]
    ls.append(str(input('Name: ')))
    ls.append(str(input('Age: ')))
    ls.append(str(input('Gender: ')))
    ls.append(str(input('Address: ')))
    ls.append(str(input('Contact: ')))
    lsn.append(ls)
  if ns==0:
    lsn+=['Nil']

def accuse():
  global la
  la=[]
  print()
  print('Accused Details')
  j=input("Has the Accused been Identified? ")
  if "y" in j.lower():
    print()
    x=str(input("Are there Multiple Accused? "))
    if "y" in x.lower():
      n=eval(input("Enter the no. Accused: "))
      for i in range(n):
        print()
        a=[]
        print ("Enter the Details of Accused no.",i,":")
        a.append(str(input('Name: ')))
        a.append(str(input('Age: ')))
        a.append(str(input('Gender: ')))
        a.append(str(input('Address: ')))
        a.append(str(input('Contact: ')))
        la.apend(a)
    elif "n" in x.lower():
      print()
      print ("Enter the Details")
      la.append(str(input('Name: ')))
      la.append(str(input('Age: ')))
      la.append(str(input('Gender: ')))
      la.append(str(input('Address: ')))
      la.append(str(input('Contact: ')))
    else:
      print ("Enter Yes or No")
      accuse()
  elif "n" in j.lower():
    la=["Nil"]
  else:
    print ("Enter Yes or No")
    accuse()

def multi_an():
    global an
    global dpt
    an=[]
    dal=[]
    for i in l:
        if i[2]==dpt.upper() and "ANALYST" in i[1]:
            dal.append(i[0].title())
    cp=input("Has an Analyst been Assigned? ")
    if "y" in cp.lower():
        print()
        x=str(input("Are there Multiple Analysts? "))
        if "y" in x.lower():
            n=eval(input("Enter the no. analysts: "))
            print()
            i=1
            while i<=n:
                aa= input ("Enter the Name of the Analyst: ")
                if aa in dal:
                    an.append(aa)
                    i+=1
                else:
                    print('Invalid Analyst')
                    print('Select an analyst from the below analyst:')
                    print(dal)
        elif "n" in x.lower():
            aaa=input ("Enter the Name of Ananlyst : ")
            an.append(aaa)
        else:
            print ("Enter Yes or No")
            multi_an()
    elif "n" in cp.lower():
        an=["Nil"]
    else:
        print ("Enter Yes or No")
        multi_an()

def Valid_IO():
    global dpt
    global ins
    for i in l:
        dl=[]
        if i[2]==dpt and i[1] in ['SPECIAL AGENT, SPECIAL AGENT IN CHARGE, ASST. SPECIAL AGENT IN CHARGE']:
            dl+=[i[0]]
            ins=str(input('Please Enter the Investigating Officer: '))
            if ins not in dl:
                print('Invalid Investigating Officer')
                print('Select an investigating officer from the below officers:')
                for k in dl:
                    print(k)
                Valid_IO()
               
def File():
  global file
  global fileee
  global flag
  flag="red"
  print()
  file=input("Enter the File No.: ")
  if file not in d:
    print()
    print ("Invalid File No. ")
    File()
  fileee='valid'
  if user[3] in ['SPECIAL AGENT IN CHARGE','ASST. SPECIAL AGENT IN CHARGE','SENIOR ANALYST']:
          if d[file]['Department']==user[4].title():
              fileee='valid'
          else:
              print("Access to file denied")
              print("ERROR 404 - Cross Department Access")
              fileee='invalid'
              flag="green"
              aoptions()
  elif user[3] in ['SPECIAL AGENT','ANALYST']:
          if (d[file]['Investigating Officer']==user[1].title()) or (user[1].title in d[file]['Analyst(s)']):
              fileee='valid'
          else:
              print("Access to file denied")
              print("ERROR 403- Invalid Credentials for Access")
              fileee='invalid'
              flag="green"
              aoptions()

def NewCase():
  global d
  global dpt
  global ins
  global flag
  global an
  flag="red"
  print()
  print('Options: ')
  print('i. Continue')
  print ('ii. Go Back')
  print()
  cp=input('Enter your Choice: ')
  if cp=="i":
      file_id=input("Enter File ID: ")
      if file_id in d:
          print ("File Exists")
          print()
          print ("Do you wish to Update the Details in the File?")
          print('Options: ')
          print('i. Update')
          print ('ii. Go Back')
          print()
          cn=input('Enter your Choice: ')
          if cn=="i":
              update()
          elif cn=="ii":
              flag="green"
              aoptions()
          else:
             NewCase() 
      else:
          dpt=str(input("Please Enter the Department Investigating the Case: "))
          if dpt.upper()==user[4] or user[4]=='N/A':
              victim()
              crime()
              evidences()
              i_suspects()
              accuse()
              print()
              stat=str(input('Status (Ongoing/Solved/Unsolved): '))
              if user[4]=="N/A" or user[3] in ["BUREAU DIRECTOR", "SPECIAL AGENT IN CHARGE", "ASST. SPECIAL AGENT IN CHARGE"]:
                  Valid_IO()
                  multi_an()
              elif user[3]=="SPECIAL AGENT":
                  ins=user[1].title()
                  multi_an()
              elif user[3]=='SENIOR ANALYST':
                  Valid_IO()
                  multi_an()
              elif i[1]=='ANALYST':
                  Valid_IO()
                  x=str(input("Are there Multiple Analysts Working with You? "))
                  if "y" in x.lower():
                      n=eval(input("Enter the no. analysts apart from yourself: "))
                      print()
                      i=1
                      while i<=n:
                          aa= input ("Enter the Name of the Analyst: ")
                          if aa in dal:
                              an.apend(aa)
                              i+=1
                          else:
                              print('Invalid Analyst')
                              print('Select from the below analysts:')
                              print(dal)
                      an.append(user[1])
                  elif 'n' in x.lower():
                      an.append(i[0])
                  else:
                      print ("Enter a valid option")
                      print ("Re-routing to Start")
                      NewCase()
              d1={'Victim Details':lv,'Charges':ch,'Details of Crime':dets,'Evidences':de,'Suspect Details':lsn,'Accused Details':la,'Status':stat,"Department":dpt,"Investigating Officer":ins,"Analyst(s)":an}
              d[file_id]=d1
              print()
              print("Case Added")
          else:
              print("Access to file denied")
              print("ERROR 404 - Cross Department Access")
              print ("Do you wish to add another case?")
              NewCase()
                  
  elif cp=="ii":
        flag="green"
        aoptions()
  else:
        print ("Invalid Option")
        NewCase()

#Status
def status():
  File()
  if fileee=='valid':
      a=input("Enter the New Status: ")
      d[file]["Status"]=a
      print ("Status Updated")

def asu():
  q=input("Enter your Choice: ")
  if "y" in q.lower():
    a=input("Enter the New Status: ")
    d[file]["Status"]=a
    print ("Status Updated")
  elif "n" in q.lower():
    pass
  else:
    print ("Invalid Choice")
    print()
    asu()
    
def ar():
  n=input("Enter the Name: ")
  for i in d[file]["Accused Details"]:
    if n in i:
      d[file]["Accused Details"].remove(i)
      print()
      print ("Accused Removed")
      if len(d[file]["Accused Details"])==0:
        d[file]["Accused Details"]+=["Nil"]
        if d[file]["Status"]=="Solved":
          print ()
          print ("You have 0 accused, would you like to change the status? ")
          asu()
      break
    else:
      print ("Invalid Name")
      ar()

def ueia():
  x=input("Enter the Name of Accused: ").lower()
  print()
  print('Parameters:')
  print('i. Name')
  print('ii. Age')
  print('iii. Gender')
  print('iv. Address')
  print('v. Contact')
  print()
  for i in d[file]["Accused Details"]:
    if i[0].lower()==x:
      c=str(input('Enter your Choice: '))
      if c=="i":
        u=input("Enter the Updated Name: ")
        i[0]=u
        print ("Details Updated")
        break
      elif c=="ii":
        u=input("Enter the Updated Age: ")
        i[1]=u
        print ("Details Updated")
        break
      elif c=="iii":
        u=input("Enter the Updated Gender: ")
        i[2]=u
        print ("Details Updated")
        break
      elif c=="iv":
        u=input("Enter the Updated Address: ")
        i[3]=u
        print ("Details Updated")
        break
      elif c=="v":
        u=input("Enter the Updated Contact: ")
        i[4]=u
        print ("Details Updated")
        break
      else:
        print ("Invalid Choice")
        ueia()
    else:
      print ("Invalid Name")
      ueia()
  
#Accused
def accused():
  print()
  print('Parameters: ')
  print('i. Add')
  print('ii. Remove')
  print ('iii. Update Existing Info')
  print('iv. Go Back')
  print()
  c=str(input('Enter your Choice: '))
  File()
  if fileee=='valid':
      l=d[file]["Accused Details"]
  else:
      c='iv'
  if c=="i":
    if l==["Nil"]:
      l.clear()
    print()
    print ("New Accused Details")
    las=[]
    las.append(str(input('Name: ')))
    las.append(str(input('Age: ')))
    las.append(str(input('Gender: ')))
    las.append(str(input('Address: ')))
    las.append(str(input('Contact: ')))
    l.append(las)
    d[file]["Accused Details"]=l
    print()
    print ("New Accused Added")
  elif c=="ii":
    ar()
  elif c=='iii':
    ueia()
  elif c=="iv":
    update()
  else:
    print ("Invalid Choice")
    accused()

def sur():
  n=input("Enter the Name: ")
  for i in d[file]["Suspect Details"]:
    if n in i:
      d[file]["Suspect Details"].remove(i)
      print()
      print ("Suspect Removed")
      if len(d[file]["Suspect Details"])==0:
        d[file]["Suspect Details"]+=["Nil"]
      break
  else:
      print ("Invalid Name")
      sur()

def ueis():
  x=input("Enter the name of suspect: ").lower()
  print()
  print('Parameters:')
  print('i. Name')
  print('ii. Age')
  print('iii. Gender')
  print('iv. Address')
  print('v. Contact')
  print()
  c=str(input('Enter your Choice: '))
  for i in d[file]["Suspect Details"]:
    if i[0].lower()==x:
      if c=="i":
        u=input("Enter the Updated Name: ")
        i[0]=u
        break
      elif c=="ii":
        u=input("Enter the Updated Age: ")
        i[1]=u
        break
      elif c=="iii":
        u=input("Enter the Updated Gender: ")
        i[2]=u
        break
      elif c=="iv":
        u=input("Enter the Updated Address: ")
        i[3]=u
        break
      elif c=="v":
        u=input("Enter the Updated Contact: ")
        i[4]=u
        break
      else:
        print ("Invalid Choice")
        ueis()
    else:
      print ("Invalid Name")
      ueis()
    
#Suspects
def suspects():
  print()
  print('Parameters: ')
  print('i. Add')
  print('ii. Remove')
  print ('iii. Update Existing Info')
  print ('iv. Go Back')
  print()
  c=str(input('Enter your Choice: '))
  File()
  if fileee=='valid':
      l=d[file]["Suspect Details"]
  else:
      c='iv'
  if c=="i":
    if l==[["Nil"]]:
      l.clear()   
    print()
    print ("New Suspect Details")
    ls=[]
    ls.append(str(input('Name: ')))
    ls.append(str(input('Age: ')))
    ls.append(str(input('Gender: ')))
    ls.append(str(input('Address: ')))
    ls.append(str(input('Contact: ')))
    l.append(ls)
    d[file]["Suspect Details"]=l
    print()
    print ("New Suspect Added")
  elif c=="ii":
    sur()
  elif c=="iii":
    ueis()
  elif c=="iv":
    update()
  else:
    print ("Invalid Choice")
    suspects()

def sr():
  k=str(input("What sample would you like to remove? "))
  for i in d[file]["Evidences"]["Comparison Samples (Forensic Evidence)"]:
    if k in i:
      d[file]["Evidences"]["Comparison Samples (Forensic Evidence)"].remove(i)
      print()
      print ("Sample Removed")
      if len(d[file]["Evidences"]["Comparison Samples (Forensic Evidence)"])==0:
        d[file]["Evidences"]['Comparison Samples (Forensic Evidence)']+=["Nil"]
      break
  else:
    print("Invalid Sample")
    sr()
      
def samples():
  print()
  print('Parameters: ')
  print('i. Add Sample')
  print('ii. Remove Sample')
  print('iii. Go Back')
  print()
  cp=str(input('Enter your Choice: '))
  l=d[file]["Evidences"]['Comparison Samples (Forensic Evidence)']
  if cp=="i":
    if l==["Nil"]:
      l.clear()
    e=input("Enter the Sample: ")
    l.append(e)
    d[file]["Evidences"]["Comparison Samples (Forensic Evidence)"]=l
    print ("New Sample Added")
  elif cp=="ii":
    sr()
  elif c=="iii":
    evidence()
  else:
    print ("Invalid Choice")
    samples()

def wr():
  n=input("Enter the Name: ")
  for i in d[file]["Evidences"]["Witness Details"]:
    if n in i:
      d[file]["Evidences"]["Witness Details"].remove(i)
      print()
      print ("Witness Removed")
      if len(d[file]["Evidences"]["Witness Details"])==0:
        d[file]["Evidences"]["Witness Details"]+=["Nil"]
      break
  else:
    print ("Invalid Name")
    wr()

def ueiw():
  x=input("Enter the Name of Witness: ").lower()
  print()
  print('Parameters:')
  print('i. Name')
  print('ii. Age')
  print('iii. Gender')
  print('iv. Address')
  print('v. Contact')
  print()
  c=str(input('Enter your Choice: '))
  for i in d[file]["Evidences"]["Witness Details"]:
    if i[0].lower()==x:
      if c=="i":
        u=input("Enter the Updated Name: ")
        i[0]=u
        break
      elif c=="ii":
        u=input("Enter the Updated Age: ")
        i[1]=u
        break
      elif c=="iii":
        u=input("Enter the Updated Gender: ")
        i[2]=u
        break
      elif c=="iv":
        u=input("Enter the Updated Address: ")
        i[3]=u
        break
      elif c=="v":
        u=input("Enter the Updated Contact: ")
        i[4]=u
        break
      else:
        print ("Invalid Choice")
        ueiw()
    else:
      print ("Invalid Name")
      ueiw()

def witnesses():
  print()
  print('Parameters:')
  print('i. Add Witness')
  print('ii. Remove Witness')
  print ("iii. Update Existing Info")
  print('iv. Go Back')
  print()
  cp=str(input('Enter your Choice: '))
  l=d[file]["Evidences"]["Witness Details"]
  if cp=="i":
    if l==[["Nil"]]:
      l.clear()
      print()
    print ("New Witness Details")
    ls=[]
    ls.append(str(input('Name: ')))
    ls.append(str(input('Age: ')))
    ls.append(str(input('Gender: ')))
    ls.append(str(input('Address: ')))
    ls.append(str(input('Contact: ')))
    l.append(ls)
    print()
    print ("New Witness Added")  
  elif cp=="ii":
    wr()
  elif cp=="iii":
    ueiw()
  elif cp=="iv":
    evidence()
  else:
    print ("Invalid Choice")
    witnesses()

#Evidence
def evidence():
  print()
  print('Parameters: ')
  print('i. Comparison Samples')
  print('ii. Witness')
  print('iii. Go Back')
  print()
  c=str(input('Enter your Choice: '))
  File()
  if fileee=='valid':
      if c=="i":
        samples()
      elif c=="ii":
        witnesses()
      elif c=="iii":
        update()
      else:
        print ("Invalid Choice")
        evidence()

def uxdets():
  global flg
  global dpt
  File()
  if fileee=='valid':
      print()
      print('Transfer Ownership: ')
      print('i. Department')
      print('ii. Investigating Officer')
      print('iii. Analyst(s)')
      print('iv. Go Back')
      print()
      if flg==0:
          c=str(input('Enter your Choice: '))
      if c=='i':
          dpt=str(input("Please Enter the Department: "))
          Valid_IO()
          d[file]['Investigating Officer']=ins
          multi_an()
          d[file]['Analyst(s)']=an
          print ("Case Transferred to Another Department")
      elif c=='ii' or flg==2:
          flg=2
          dl=[]
          for i in l:              
              if i[2]==d[file]["Department"].upper() and "AGENT" in i[1]:
                  print (i)
                  dl.append(i[0].title())
          nio=str(input('Enter the New Investigating Officer: '))
          if nio in dl:
              d[file]['Investigating Officer']=nio
          else:
              print('Invalid Officer')
              print('Select Investigating Officer from the Available List of Officers - ',dl)
              uxdets()
          print ("Investigating Officer Changed")
      elif c=='iii' or flg==3:
          flg=3
          dal=[]
          for i in l:
              if i[2]==d[file]['Department'].upper() and "ANALYST" in i[1]:
                  dal.append(i[0].title())
          print('All Current Analysts removed \n Enter new analyst(s) details: \n')
          cp=input("Has a new analyst been Assigned? ")
          if "y" in cp.lower():
              an=[]
              print()
              x=str(input("Are there Multiple Analysts? "))
              if "y" in x.lower():
                  n=eval(input("Enter the no. analysts: "))
                  print()
                  i=1
                  while i<=n:
                      aa= input ("Enter the Name of Analyst: ")
                      if aa in dal:
                          an.append(aa)
                          i+=1
                      else:
                          print('Invalid Analyst')
                  d[file]['Analyst(s)']=an
              elif "n" in x.lower():
                  aaa=input ("Enter the Name of Analyst : ")
                  an.append(aaa)
                  d[file]['Analyst(s)']=an
              else:
                  print ("Enter Yes or No")
                  uxdets()
          elif "n" in j.lower():
              an=["Nil"]
              print ("Analyst Details Changed")
          else:
              print ("Enter Yes or No")
              uxdets()
      elif c=="iv":
        update()
      else:
        print("Invalid Choice")
        uxdets()

def update(): 
    global flag
    flag="red"
    print()
    print('Parameters :')
    print('i. Status')
    print('ii. Accused')
    print('iii. Suspects')
    print('iv. Evidence')
    print('v. Transfer Case')
    print('vi. Go Back')
    print()
    c=str(input('Enter your Choice: '))
    if c=="i":
        status()
    elif c=="ii":
        accused()
    elif c=="iii":
        suspects()
    elif c=="iv":
        evidence()
    elif c=='v':
        global flg
        flg=0
        uxdets()
    elif c=='vi':
        flag="green"
        aoptions()
    else:
        print ("Invalid Choice")
        update()

#History
def history():
  global ut
  global flag
  flag="red"
  print()
  print('Options: ')
  print('i. Continue')
  print ('ii. Go Back')
  print()
  cp=input('Enter your Choice: ')
  if cp=="i":
      criminal=str(input('Enter Name of Criminal: ')).title()
      c=0
      for k in d:
        for w in d[k]['Accused Details']:
          if criminal in w[0].title():
            print()
            print("File No.:",k)
            for j in d[k]:
              print(j,":",d[k][j],end="\n")
            c+=1
      else:
        if c==0:
          print('All Clear')
  elif cp=="ii":
    if ut=="Authorised Access":
        flag="green"
        aoptions()
    else:
        flag="green"
        goptions()
  else:
    print ("Invalid Option")
    history()

#Similar
def similar():
  global flag
  flag="red"
  simc=0
  print()
  print('Parameters:')
  print('i. Charges')
  print('ii. Details')
  print('iii. Evidence')
  print ('iv. Go Back')
  print()
  cp=input('Enter your choice - ')
  if cp=="i":
    c=str(input('Enter charges - '))
    p=c.lower()
    for k in d:
      if d[k]['Charges'].lower()==p:
        print()
        simc+=1
        print("File No.:",k)
        for j in d[k]:
          print(j,":",d[k][j],end="\n")
    else:
        if simc==0:
            print('No existing cases matches')      
  elif cp=="ii":
    dt=str(input('Enter the Details of Crime (Date, Time, Location, Important Facts) briefly: ')).lower()
    x=dt.split(",")
    for k in d:
        for y in d[k]['Details of Crime']:
            if y.lower() in x:
                simc+=1
                print()
                print("File No.:",k)
                for j in d[k]:
                    print(j,":",d[k][j],end="\n")
                break
    else:
        if simc==0:
            print('No existing cases matches')
  elif cp=="iii":
    print()
    print('Parameters - ')
    print('i. Comparison Samples')
    print('ii. Witness')
    print('iii. Go Back')
    print()
    c=str(input('Enter your Choice: '))
    if c=="i":
        el_=str(input('Enter Comparison Sample: '))
        for k in d:
            for y in d[k]['Evidences']['Comparison Samples (Forensic Evidence)']:
              if el_==y:       
                print()
                simc+=1
                print("File No.:",k)
                for j in d[k]:
                  print(j,":",d[k][j],end="\n")
              break
        else:
            if simc==0:
                print('No existing cases matches') 
    elif c=="ii":
        wl_=str(input('Enter Witness Name: '))
        for k in d:
            for y in d[k]['Evidences']['Witness Details']:
              for l in y:
                  if wl_==y[0]:
                    print()
                    print("File No.:",k)
                    for j in d[k]:
                      print(j,":",d[k][j],end="\n")
                      simc+=1
                    break
        else:
            if simc==0:
                print('No existing cases matches')
    elif c=="iii":
        similar()
    else:
        print ("Invalid Choice")
        similar()
    
  elif cp=='iv':
    if ut=="Authorised Access":
        flag="green"
        aoptions()
    else:
        flag="green"
        goptions()
  else:
    print ("Invalid Choice")
    print()
    similar()

def Fno():
  f=str(input("Enter the file no.: "))
  for i in d:
    if i==f:
      print()
      print("File No.:",i)
      for j in d[i]:
        print(j,":",d[i][j],end="\n")
      break
  else:
    print("Invalid File No.")
    Fno()
    
#Display()

def adispalystatus():
    global flag
    flag="red"
    print()
    print('Parameters: ')
    print('i. Ongoing')
    print('ii. Solved')
    print('iii. Unsolved')
    print ('iv. Go Back')
    print()
    cp=str(input('Enter your Choice: '))
    if cp=='i':
        c=0
        for i in d:
          if d[i]["Status"].lower()=="ongoing":
            c+=1
            print()
            print("File No.:",i)
            for j in d[i]:
              print(j,":",d[i][j],end="\n")
        else:
          if c==0:
            print ("No Ongoing Cases")
    elif cp=='ii':
        c=0
        for i in d:
          if d[i]["Status"].lower()=="solved":
            c+=1
            print()
            print("File No.:",i)
            for j in d[i]:
              print(j,":",d[i][j],end="\n")
        else:
          if c==0:
            print ("No Solved Cases")
    elif cp=="iii":
        c=0
        for i in d:
          if d[i]["Status"].lower()=="unsolved":
            c+=1
            print()
            print("File No.:",i)
            for j in d[i]:
              print(j,":",d[i][j],end="\n")
        else:
          if c==0:
            print ("No Unsolved Cases")
    elif cp=="iv":
          flag="green"
          adisplay()
    else:
          print ("Invalid Option")
          adispalystatus()

def AllCaseDpt():
    global flag
    global user
    flag="red"
    print()
    print('Parameters: ')
    print('i. Your Department')
    print('ii. Other Department')
    print ('iii. Go Back')
    print()
    ch=str(input('Enter your Choice: '))
    if ch=="i":
        c=0
        for i in d:
            if d[i]["Department"].upper()==user[4]:
                c+=1
                print()
                print("File No.:",i)
                for j in d[i]:
                    print(j,":",d[i][j],end="\n")
        else:
            if c==0:
                print ("No Cases Exist in Your Deaprtment")
    elif ch=="ii":
           print()
           dpt=str(input("Enter the Department: "))
           c=0
           for i in d:
              if d[i]["Department"].upper()==dpt.upper():
                  c+=1
                  print()
                  print("File No.:",i)
                  for j in d[i]:
                      print(j,":",d[i][j],end="\n")
           else:
                if c==0:
                    print ("No Cases Exist in the",dpt)
    elif ch=="iii":
        flag='green'
        adisplaydpt()
    else:
           AllCaseDpt()

def adisplaydpt():
  global flag
  global user
  flag="red"
  print()
  print('Parameters: ')
  print('i. All Cases in A Department')
  print('ii. Specifc Investigating Officer')
  print ('iii. Go Back')
  print()
  cp=str(input('Enter your Choice: '))
  if cp=="i":
       AllCaseDpt()
  elif cp=="ii":
      print()
      ins=str(input("Enter the Investigating Offcier: "))
      c=0
      for i in d:
          if d[i]["Investigating Officer"].upper()==ins.upper():
              c+=1
              print()
              print("File No.:",i)
              for j in d[i]:
                  print(j,":",d[i][j],end="\n")
      else:
          if c==0:
              print (ins,"is not the investigating officer of any case")
  elif cp=="iii":
      flag='green'
      adisplay()
  else:
      print ("Invalid Option")
      adisplaydpt()
      
def adisplay():
  global flag
  flag="red"
  print()
  print('Parameters: ')
  print('i. File No.')
  print('ii. Status')
  print('iii. Department')
  print ('iv. All Cases')
  print ('v. My Cases')
  print ('vi. Go Back')
  print()
  cp=str(input('Enter your Choice: '))
  if cp=='i':
    Fno()
  elif cp=="ii":
    adispalystatus()
  elif cp=="iii":
    adisplaydpt()
  elif cp=="iv":
      for i in d:
          print()
          print("File No.:",i)
          for j in d[i]:
              print(j,":",d[i][j],end="\n")
  elif cp=="v":
    c=0
    if 'ANALYST' not in user[3]:
        for i in d:
          if d[i]["Investigating Officer"].upper()==user[1]:
              c+=1
              print()
              print("File No.:",i)
              for j in d[i]:
                print (j,":",d[i][j], end="\n")
        else:
           if c==0:
               print ("You currently have 0 cases registered.")
    elif 'ANALYST' in user[3]:
        for i in d:
           for j in d[i]["Analyst(s)"]:
               if j==user[1]:
                   c+=1
                   print()
                   print("File No.:",i)
                   for k in d[i]:
                       print (k,":",d[i][k], end="\n")
        else:
           if c==0:
               print ("You currently have 0 cases registered.")
  elif cp=="vi":
    flag="green"
    aoptions()
  else:
    print ("Invalid Choice")
    adisplay()
    
def gdispalystatus():
    global flag
    flag="red"
    print()
    print('Parameters: ')
    print('i. Ongoing')
    print('ii. Solved')
    print('iii. Unsolved')
    print ('iv. Go Back')
    print()
    cp=str(input('Enter your Choice: '))
    if cp=='i':
        c=0
        for i in d:
          if d[i]["Status"].lower()=="ongoing":
            c+=1
            print()
            print("File No.:",i)
            for j in d[i]:
              print(j,":",d[i][j],end="\n")
        else:
          if c==0:
            print ("No Ongoing Cases")
    elif cp=='ii':
        c=0
        for i in d:
          if d[i]["Status"].lower()=="solved":
            c+=1
            print()
            print("File No.:",i)
            for j in d[i]:
              print(j,":",d[i][j],end="\n")
        else:
          if c==0:
            print ("No Solved Cases")
    elif cp=="iii":
        c=0
        for i in d:
          if d[i]["Status"].lower()=="unsolved":
            c+=1
            print()
            print("File No.:",i)
            for j in d[i]:
              print(j,":",d[i][j],end="\n")
        else:
          if c==0:
            print ("No Unsolved Cases")
    elif cp=="iv":
        flag="green"
        gdisplay()
    else:
        print ("Invalid Option")
        gdispalystatus()

def gdisplaydpt():
  global flag
  global user
  flag="red"
  print()
  print('Parameters: ')
  print('i. All Cases in A Department')
  print('ii. Specifc Investigating Officer')
  print ('iii. Go Back')
  print()
  cp=str(input('Enter your Choice: '))
  if cp=="i":
      print()
      dpt=str(input("Enter the Department: "))
      c=0
      for i in d:
          if d[i]["Department"].upper()==dpt.upper():
              c+=1
              print()
              print("File No.:",i)
              for j in d[i]:
                  print(j,":",d[i][j],end="\n")
      else:
          if c==0:
              print (dpt,"is not investigating any case")
  elif cp=="ii":
      print()
      ins=str(input("Enter the Investigating Offcier: "))
      c=0
      for i in d:
          if d[i]["Investigating Officer"].upper()==ins.upper():
              c+=1
              print()
              print("File No.:",i)
              for j in d[i]:
                  print(j,":",d[i][j],end="\n")
      else:
          if c==0:
              print (ins,"is not the investigating officer of any case")
  elif cp=="iii":
      flag='green'
      gdisplay()
  else:
      print ("Invalid Option")
      gdisplaydpt()

def gdisplay():
  global flag
  flag="red"
  print()
  print('Parameters: ')
  print('i. File No.')
  print('ii. Status')
  print('iii. Department')
  print ('iv. All Cases')
  print ('v. Go Back')
  print()
  cp=str(input('Enter your Choice: '))
  if cp=='i':
    Fno()
  elif cp=="ii":
    gdispalystatus()
  elif cp=="iii":
    gdisplaydpt()
  elif cp=="iv":
      for i in d:
          print()
          print("File No.:",i)
          for j in d[i]:
              print(j,":",d[i][j],end="\n")
  elif cp=="v":
    flag="green"
    goptions()
  else:
    print ("Invalid Choice")
    gdisplay()

def updateinfile():
    f=open('GBI_Records.dat','wb+')
    for k in d:
        x={}
        x[k]=d[k]
        pickle.dump(x,f)
    f.close()

def aoptions():
  global flag
  while True:
    print()
    print ("Please select the option you wish to execute")
    print()
    print('1. Update - Status | Accused | Suspects | Evidence | Case Handlers') 
    print('2. Criminal History')
    print('3. Details of Similar Crimes - Charges | Details of Crime | Evidence')
    print('4. Add New Case') 
    print('5. Display Details - File No. | Status | Department | All Cases | My Cases') 
    print('6. Exit')
    print()
    c=str(input('Enter your Choice:  '))
    if c=="1":
        update()
        updateinfile()
        if flag=="green":
            break
    elif c=="2":
        history()
        if flag=="green":
            break
    elif c=="3":
        similar()
        if flag=="green":
            break
    elif c=="4":
        NewCase()
        updateinfile()
        if flag=="green":
            break
    elif c=="5":
        adisplay()
        if flag=="green":
            break
    elif c=="6":
        print ("Logging Out...")
        print("Exiting Database")
        break
    else:
      print("Invalid Option")
      aoptions()
      
def goptions():
  global flag
  flag="red"
  while True:
    print()
    print ("Please select the option you wish to execute")
    print()
    print('1. Criminal History')
    print('2. Details of Similar Crimes - Charges | Details of Crime | Evidence')
    print('3. Display Details - File No. | Status | Derpartment | All Cases')
    print('4. Exit')
    print()
    c=str(input('Enter your Choice:  '))
    if c=="1":
        history()
        if flag=="green":
            break
    elif c=="2":
        similar()
        if flag=="green":
            break
    elif c=="3":
        gdisplay()
        if flag=="green":
            break
    elif c=="4":
        print ("Exiting Database")
        break
    else:
      print("Invalid Option")
      goptions()
