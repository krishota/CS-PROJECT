d={"#001-B":
   {'Victim Details':["Arianna","25 yrs","F","Villa 42, South Street, Jumeirah","056-7894321"],
    'Charges':"Burglary",
    'Details of Crime':["23/01/23","17:00","Victim's Home","TV and Jewellery Stolen"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["DNA","Fingerprints"],
                 'Witness Details':[["Nil"]]},
    'Suspect Details':[['Nil']],
    'Accused Details':[["John C","27 yrs","M","Flat#502, Black Building, Karama","065-9876356"]],
    'Status':"Solved"},
   "#001-M":
   {'Victim Details':["Jack","20 yrs","M","Flat#901, Pearl Oasis Complex, Creek","050-9230487"],
    'Charges':"Murder",
    'Details of Crime':["29/01/23","23:30","Victim's Home","Knife Wound & Gunshot to Head","Laptop Missing"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["Blue Fiber","Bloody Footprint - Male Size 10"],
                 'Witness Details':["Nil"]},
    'Suspect Details':[["Carlos","29 yrs","M","Flat#608, GreenView Apartments, Karama", "067-9872347"],
                       ["Rihanna","27 yrs","F","Villa 52, Southbridge Community, DSO", "047-9823468"]],
    'Accused Details':["Nil"],
    'Status':"Ongoing"},
   "#001-C":
   {'Victim Details':["Caren","17 yrs","F","Flat#105, Al Tala Apartments, Jadaf","092-8762341"],
    'Charges':"Cyber Crime",
    'Details of Crime':["01/02/23","Via Instagram","Cyber Bullying followed by Account Hack"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["Hacker's Signature"],
                 'Witness Details':["Nil"]},
    'Suspect Details':[["Rory_23_Rocking (Screen Name)","Unknown Age","Unknown Gender","Unknown Address", "Contact Info Unavailable"]],
    'Accused Details':["Nil"],
    'Status':"Unsolved"},
   "#002-M":
   {'Victim Details':["Jasper","25 yrs","M","Flat#301, Avenue Bridge Builidng, Deira","050-8872231"],
    'Charges':"Murder",
    'Details of Crime':["03/02/23","22:30","Victim's Home","Knife Wound & Gunshot to Head","Laptop Missing"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["Blue Fiber","Bloody Footprint - Male Size 10"],
                 'Witness Details':["Nil"]},
    'Suspect Details':[["Nil"]],
    'Accused Details':["Nil"],
    'Status':"Ongoing"},
   "#001-A":
   {'Victim Details':["Mairah","21 yrs","F","Villa 55, Stoneybridge Premium Villas, JVC","055-0900213"],
    'Charges':"Assault",
    'Details of Crime':["30/01/23","21:00","Neighbourhood Park","Blow to the Head","Stolen Purse and Diamond Bracelet"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':[""],
                 'Witness Details':[["Lana J","29 yrs","F","Room 2987, Green Time Hotel Apartments, Dubai Marina", "065-9903218"],
                                    ["Amira","21 yrs","F","Villa 57, JBR Beach, Jumeirah","076-9870273"]]},
    'Suspect Details':[["Nil"]],
    'Accused Details':["Nil"],
    'Status':"Ongoing"}}
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
  ch=str(input('Charges pressed against the Accused: '))
  dets=str(input('Enter the Details of Crime (Date, Time, Location, Important Facts) briefly: ')).lower().split(',')
  
def evidences():
  global de
  de={}
  lwn=[]
  print()
  print('Evidences')
  el=input('Enter list of comparison samples: ')
  ec=el.split(',')
  if len(ec)==0:
    ec=["Nil"]
  nw=int(input('Enter no. of Witnesses: '))
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
  ns=int(input('Enter no. of Suspects: '))
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
  j=input("Has the accused been identified? ")
  if j in ["Yes","yes","y","ye","Y"]:
    print()
    x=str(input("Are there multiple accused? "))
    if x in ["Yes","yes","y","ye","Y"]:
      n=eval(input("Enter the no. accused: "))
      for i in range(n):
        print()
        a=[]
        print ("Enter the details of accused no.",i,":")
        a.append(str(input('Name: ')))
        a.append(str(input('Age: ')))
        a.append(str(input('Gender: ')))
        a.append(str(input('Address: ')))
        a.append(str(input('Contact: ')))
        la.apend(a)
    elif x in ["No","no","n","N"]:
      print ("Enter the Details")
      la.append(str(input('Name: ')))
      la.append(str(input('Age: ')))
      la.append(str(input('Gender: ')))
      la.append(str(input('Address: ')))
      la.append(str(input('Contact: ')))
    else:
      print ("Enter Yes or No")
      accuse()
  elif j in ["No","no","n","N"]:
    la=["Nil"]
  else:
    print ("Enter Yes or No")
    accuse()

def File():
  print()
  file=input("Enter the File No.: ")
  if file not in d:
    print()
    print ("Invalid File No. ")
    File()

def NewCase():
  global d
  file_id=input("Enter file id: ")
  victim()
  crime()
  i_suspects()
  evidences()
  accuse()
  print()
  stat=str(input('Status (Ongoing/Solved/Unsolved): '))
  d1={'Victim Details':lv,'Charges':ch,'Details of Crime':dets,'Evidences':de,'Suspect Details':lsn,'Accused Details':la,'Status':stat}
  d[file_id]=d1
  print()
  print("Case Added")

#Status
def status():
  File()
  a=input("Enter the New Status: ")
  d[file]["Status"]=a
  print ("Status Updated")

#Accused
def accused():
  print()
  print('Parameters - ')
  print('i. Add')
  print('ii. Remove')
  print('iii. Go Back')
  print()
  c=str(input('Enter your Choice: '))
  File()
  l=d[file]["Accused Details"]
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
    else:
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
    n=input("Enter the Name: ")
    for i in d[file]["Accused Details"]:
      if n in i:
        d[file]["Accused Details"].remove(i)
        print()
        print ("Accused Removed")
        if len(d[file]["Accused Details"])==0:
          d[file]["Accused Details"]+=["Nil"]
        break
    else:
      print ("Invalid Name")
      accused()
  elif c=="iii":
    update()
  else:
    print ("Invalid Choice")
    accused()

#Suspects
def suspects():
  print()
  print('Parameters - ')
  print('i. Add')
  print('ii. Remove')
  print ('iii. Go Back')
  print()
  c=str(input('Enter your Choice: '))
  file=str(input("Enter the File No.: "))
  l=d[file]["Suspect Details"]
  File()
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
    else:
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
      suspects()
  elif c=="iii":
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
  print('Parameters - ')
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

def witnesses():
  print()
  print('Parameters - ')
  print('i. Add Witness')
  print('ii. Remove Witness')
  print('iii. Go Back')
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
    evidence()
  else:
    print ("Invalid Choice")
    witnesses()

#Evidence
def evidence():
  print()
  print('Parameters - ')
  print('i. Comparison Samples')
  print('ii. Witness')
  print('iii. Go Back')
  print()
  c=str(input('Enter your Choice: '))
  File()
  if c=="i":
    samples()
  elif c=="ii":
    witnesses()
  elif c=="iii":
    update()
  else:
    print ("Invalid Choice")
    evidence()

#Update
def update():
  print()
  print('Parameters - ')
  print('i. Status')
  print('ii. Accused')
  print('iii. Suspects')
  print('iv. Evidence')
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
  else:
      print ("Invalid Choice")
      update()

#History
def history():
  criminal=str(input('Enter Name of Criminal: ')).lower()
  c=0
  for k in d:
    for w in d[k]['Accused Details']:
      if w[0].lower()==criminal:
        print()
        print("File No.:",k)
        for j in d[k]:
          print(j,":",d[k][j],end="\n")
        c+=1
  else:
    if c==0:
      print('All Clear')

#Similar
def similar():
  print()
  print('Parameters - ')
  print('i. Charges')
  print('ii. Details')
  print('iii. Evidence')
  print()
  cp=input('Enter your choice - ')
  if cp=="i":
    c=str(input('Enter charges - '))
    p=c.lower()
    for k in d:
      if d[k]['Charges'].lower()==p:
        print()
        print("File No.:",k)
        for j in d[k]:
          print(j,":",d[k][j],end="\n")
  elif cp=="ii":
    dt=str(input('Enter the Details of Crime (Date, Time, Location, Important Facts) briefly: ')).lower()
    x=dt.split(",")
    for k in d:
      for i in x:
        for y in d[k]['Details of Crime']:
          if i==y.lower():       
            print()
            print("File No.:",k)
            for j in d[k]:
              print(j,":",d[k][j],end="\n")
            break
  elif cp=="iii":
    el_=str(input('Enter list of comparison samples: ')).lower()
    x=el_.split(",")
    for k in d:
      for i in x:
        for y in d[k]['Evidences']['Comparison Samples (Forensic Evidence)']:
          if i==y.lower():       
            print()
            print("File No.:",k)
            for j in d[k]:
              print(j,":",d[k][j],end="\n")
            break
  else:
    print ("Invalid Choice")
    print()
    similar()

#Display()
def display():
  print()
  print('Parameters - ')
  print('i. File No.')
  print('ii. Ongoing Cases')
  print('iii. Solved Cases')
  print('iv. Unsolved Cases')
  print ('v. All Cases')
  print()
  cp=str(input('Enter your choice - '))
  if cp=='i':
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
      display()
  elif cp=='ii':
    c=0
    for i in d:
      if d[i]["Status"]=="Ongoing":
        c+=1
        print()
        print("File No.:",i)
        for j in d[i]:
          print(j,":",d[i][j],end="\n")
    else:
      if c==0:
        print ("No Ongoing Cases")
  elif cp=='iii':
    c=0
    for i in d:
      if d[i]["Status"]=="Solved":
        c+=1
        print()
        print("File No.:",i)
        for j in d[i]:
          print(j,":",d[i][j],end="\n")
    else:
      if c==0:
        print ("No Solved Cases")
  elif cp=="iv":
    c=0
    for i in d:
      if d[i]["Status"]=="Unsolved":
        c+=1
        print()
        print("File No.:",i)
        for j in d[i]:
          print(j,":",d[i][j],end="\n")
    else:
      if c==0:
        print ("No Unsolved Cases")
  elif cp=="v":
    for i in d:
      print()
      print("File No.:",i)
      for j in d[i]:
        print (j,":",d[i][j], end="\n")
  else:
    print ("Invalid Choice")
    display()

def options():
  while True:
    print()
    print ("Welcome to the GBI Crime Records Dept.")
    print()
    print ("Please select the option you wish to execute")
    print()
    print('1. Update - Status | Accused | Suspects | Evidence')
    print('2. Criminal History')
    print('3. Details of Similar Crimes - Charges | Details of Crime | Evidence')
    print('4. Add New Case')
    print('5. Display Details - File No. | Ongoing Cases | Solved Cases | Unsolved Cases | All Cases')
    print('6. Exit')
    print()
    c=str(input('Enter your Choice:  '))
    if c=="1":
      update()
    elif c=="2":
      history()
    elif c=="3":
      similar()
    elif c=="4":
      NewCase()
    elif c=="5":
      display()
    elif c=="6":
      print ("Exiting Database")
      break
    else:
      print("Invalid Option")
      options()
options()
