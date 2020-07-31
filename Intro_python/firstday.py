# This python script is for getting every 1 jan day .

startyear=int(input("Enter the first year:\n"))
endyear=int(input("Enter the second year:\n"))

def R(n,m):
    return (n%m)



for i in range(startyear,endyear+1):
    i=int(i)

    a=1+5*R(i-1,4)
    b=4*R(i-1,100)
    c=6*R(i-1,400)
    d=a+b+c

    day=R(d,7)

    day=int(day)
    if day==0:
        result="Sunday"
    elif day==1:
        result="Monday"
    elif day==2:
        result="Tuesday"
    elif day==3:
        result="Wednesday"
    elif day==4:
        result="Thrusday"
    elif day==5:
        result="Friday"
    elif day==6:
        result="Saturday"

    print("The 1st of January "+str(i)+" falls on a "+str(result))
