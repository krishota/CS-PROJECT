d={"#001-B":
   {'Victim Details':["Arianna","25 yrs","F","Villa 42, South Street, Jumeirah","056-7894321"],
    'Charges':"Burglary",
    'Details of Crime':["23/01/23","17:00","Victim's Home","TV and Jewellery Stolen"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["DNA","Fingerprints"],
                 'Witness Details':[["Nil"]]},
    'Suspect Details':[['Nil']],
    'Accused Details':[["John C","27 yrs","M","Flat#502, Black Building, Karama","065-9876356"]],
    'Status':"Solved",
    'Department':'Organized Crime Bureau',
    'Investigating Officer':'Nancy Drew',
    "Analyst(s)":["Andre Raines","Isobel Castille"]},
   "#001-M":
   {'Victim Details':["Jack","20 yrs","M","Flat#901, Pearl Oasis Complex, Creek","050-9230487"],
    'Charges':"Murder",
    'Details of Crime':["29/01/23","23:30","Victim's Home","Knife Wound & Gunshot to Head","Laptop Missing"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["Blue Fiber","Bloody Footprint - Male Size 10"],
                 'Witness Details':["Nil"]},
    'Suspect Details':[["Carlos","29 yrs","M","Flat#608, GreenView Apartments, Karama", "067-9872347"],
                       ["Rihanna","27 yrs","F","Villa 52, Southbridge Community, DSO", "047-9823468"]],
    'Accused Details':["Nil"],
    'Status':"Ongoing",
    'Department':'Homicide Bureau',
    'Investigating Officer':'Rosa Diaz',
    'Analyst(s)':["Kristen Vega","Ian Daniels"]},
   "#001-C":
   {'Victim Details':["Caren","17 yrs","F","Flat#105, Al Tala Apartments, Jadaf","092-8762341"],
    'Charges':"Cyber Crime",
    'Details of Crime':["01/02/23","Via Instagram","Cyber Bullying followed by Account Hack"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["Hacker's Signature"],
                 'Witness Details':["Nil"]},
    'Suspect Details':[["Rory_23_Rocking (Screen Name)","Unknown Age","Unknown Gender","Unknown Address", "Contact Info Unavailable"]],
    'Accused Details':["Nil"],
    'Status':"Unsolved",
    'Department':'Cyber Crimes Bureau',
    'Investigating Officer':'Erin Reagan',
    'Analyst(s)':["Hana Gibson","Remy Scott","Katrin Jeager"]},
   "#002-M":
   {'Victim Details':["Jasper","25 yrs","M","Flat#301, Avenue Bridge Builidng, Deira","050-8872231"],
    'Charges':"Murder",
    'Details of Crime':["03/02/23","22:30","Victim's Home","Knife Wound & Gunshot to Head","Laptop Missing"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["Blue Fiber","Bloody Footprint - Male Size 10"],
                 'Witness Details':["Nil"]},
    'Suspect Details':[["Nil"]],
    'Accused Details':["Nil"],
    'Status':"Ongoing",
    'Department':'Homicide Bureau',
    'Investigating Officer':'Everly Kingston',
   'Analyst(s)': ["Jamie Kellet"]},
   "#001-A":
   {'Victim Details':["Mairah","21 yrs","F","Villa 55, Stoneybridge Premium Villas, JVC","055-0900213"],
    'Charges':"Assault",
    'Details of Crime':["30/01/23","21:00","Neighbourhood Park","Blow to the Head","Stolen Purse and Diamond Bracelet"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':[""],
                 'Witness Details':[["Lana J","29 yrs","F","Room 2987, Green Time Hotel Apartments, Dubai Marina", "065-9903218"],
                                    ["Amira","21 yrs","F","Villa 57, JBR Beach, Jumeirah","076-9870273"]]},
    'Suspect Details':[["Nil"]],
    'Accused Details':["Nil"],
    'Status':"Ongoing",
    'Department':'Organized Crime Bureau',
    'Investigating Officer':'Frank Hardy',
    'Analyst(s)':["Jubal Valentine"]},
   "#003-M":
   {'Victim Details':["Evan Buckley","26 yrs","M","#2201, Starry Night Apartments, Broad Street, Elkfield Drive","058-0913883"],
    'Charges':"Murder",
    'Details of Crime':["23/01/2022","02:00","Elkfield Park","Gunshot to Chest","Missing Ring"],
    'Evidences':{'Comparison Samples (Forensic Evidence)':["GSR on Victim's Clothing"],
                 'Witness Details':["Nil"]},
    'Suspect Details':[["Nil"]],
    'Accused Details':["Nil"],
    'Status':"Ongoing",
    'Department':'Homicide Bureau',
    'Investigating Officer':'Eve Dallas',
    'Analyst(s)':["Jamie Kellet","Ian Daniels"]}}
D={}
import pickle
f=open('GBI_Records.dat','wb+')
for k in d:
    x={}
    x[k]=d[k]
    pickle.dump(x,f)
f.seek(0)
f=open('GBI_Records.dat','rb')
try:
    while True:
        x=pickle.load(f)
        for k in x:
            D[k]=x[k]
        print(x)
except EOFError:
    print('over')
    f.close()
print(D)
