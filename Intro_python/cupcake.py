print("Welcome to the 30 Second Rule Expert")
print("-------------------------------------")
print("Answer the following questions by selecting from among the options.")

stickyans=input("Was it sticky? (yes/no)")
print(type(stickyans),"stickyans:",stickyans)
if stickyans=="no":
 sticky2ans=input("Did anyone see you?(yes/no)")
if sticky2ans=="yes":
  sticky3ans=input("Was it a boss/lover/parent?(yes/no)")
if sticky3ans=="yes":
  stick4ans=input("Was it expensive?(yes/no)")
if stick4ans=="yes":
  sticky5ans=input("Can you cut off the part that touched the floor?(yes/no)")
if sticky5ans=="yes":
  print("EAT IT.")
elif sticky5ans=="no":
  print("YOUR CALL")
elif stick4ans=="no":
  sticky52ans=input("Is it chocolate?(yes/no)")
if sticky52ans=="yes":
  print("EAT IT.")
elif sticky52ans=="no":
  print("DON'T EAT IT")
elif sticky3ans=="no":
  print("EAT IT.")

elif stickyans=="yes":
  sticky11ans=input("Is it a raw steak?(yes/no)")
if sticky11ans=="yes":
  sticky12ans=input("Are you a puma?(yes/no)")
if sticky12ans=="yes":
  print("EAT IT")
elif sticky12ans=="no":
  print("DON'T EAT IT")

elif sticky11ans=="no":
  stickycatans=input("Did the cat lick it?(yes/no)")
if stickycatans=="no":
  print("EAT IT")
elif stickycatans=="yes":
  stickycat2=input("Is your cat healthy?(yes/no)")
if stickycat2=="yes":
  print("EAT IT")
elif stickycat2=="no":
  print("YOUR CALL")

elif stickyans=="Other":
  stickyother1=input("Is it an Emausaurus?(yes/no)")
if stickyother1=="yes":
  stickyot2=input("Are you a Megalosaurus?(yes/no)")
if stickyot2=="yes":
  print("EAT IT")
elif stickyot2=="no":
  print("DON'T EAT IT")
elif stickyother1=="NO" or "no":
  stickothercat=input("Did the cat lick it?(yes/no)")
if stickothercat=="no":
  print("EAT IT")
elif stickothercat=="yes":
 stickyotcat2=input("Is your cat healthy?(yes/no)")
if stickyotcat2=="yes":
  print("EAT IT")
elif stickyotcat2=="no":
  print("YOUR CALL")

            