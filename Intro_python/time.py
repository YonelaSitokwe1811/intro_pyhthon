Hours=int(input("Enter Hours : "))
Minutes=int(input("Enter Minutes : "))
Seconds=int(input("Enter Seconds : "))
if (Hours<0 or Hours>23):
     print("Your time is invalid")
elif (Minutes<0 or Minutes>59):
      print("Your time is invalid")
else:
    if (Seconds<0 or Seconds>59):
      print("Your time is invalid")
    else:
      print ("Your time is valid")
