def print_welcome():
    print('Test harness for calutils');
def is_leap_year(year):

   if(year%4==0 or year%400==0):
      return True
   else:
      print("Not leap year")

def first_day_of_year(year):
 days = ((1 + 5*((year - 1)%4)) + 4*((year - 1)%100) + 6*((year - 1)%400))%7
 return days
def first_day_of_month(num,year):
    Wdays = first_day_of_year(year)
    days = 0
    for m in range(1, num):
        days+= days_in_month(m,year)
    for i in range(1,days+1):        
        if Wdays == 6:
            Wdays = 0
        else:
          Wdays+=1
    return Wdays



def get_selection():
    print('\nChoose from the following options:')
    print('0. quit')
    print('1. Test is_leap_year().')
    print('2. Test month_name().')
    print('3. Test days_in_month().')
    print('4. Test first_day_of_year().')
    print('5. Test first_day_of_month().')
    return int(input())
def month_name(num):
 if num==1:
   return'January'
 elif num==2:
   return'February'
 elif num==3:
   return'March'
 elif num==4:
   return'April'
 elif num==5:
   return'May'
 elif num==6:
   return'June'
 elif num==7:
   return'July'
 elif num==8:
   return'August'
 elif num==9:
   return'september'
 elif num==10:
   return'October'
 elif num==11:
   return'November'
 elif num==12:
   return'December'
def days_in_month(mon,year):
  if mon==1:
   return 31
  elif mon==2:
   if is_leap_year(year):
    return 29
  elif mon==3:
   return 31
  elif mon==4:
   return 30
  elif mon==5:
   return 31
  elif mon==6:
   return 30
  elif mon==7:
   return 31
  elif mon==8:
   return 31
  elif mon==9:
   return 31
  elif mon==10:
   return 31
  elif mon==11:
   return 30
  elif mon==12:
   return 31
def test_leap_year():
    from calutils import is_leap_year

    year = int(input('Enter the year (4 digits):\n'))
    if is_leap_year(year):
        print('The year '+str(year)+' is a leap year.')
    else:
        print('The year '+str(year)+' is not leap year.')
def test_month_name():
    from calutils import month_name
    
    for month_number in range(1, 13):
        print('Month number '+str(month_number)+ ' is '+month_name(month_number)+'.')       
def test_days_in_month():

    from calutils import days_in_month

    year = int(input('Enter the year (4 digits):\n'))
    for month_number in range(1, 13):
        print('The days in the month with number '+str(month_number)+ ' in year '+str(year)+' is '+str(days_in_month(month_number, year))+'.')
def test_first_day_year():
    from calutils import first_day_of_year
    
    year = int(input('Enter the year (4 digits):\n'))
    print('The first day of '+str(year)+' is '+str(first_day_of_year(year))+'.')
def test_first_day_month():
    from calutils import first_day_of_month
    
    month = int(input('Enter the month (1 for January, ..., 12 for December):\n'))
    year = int(input('Enter the year (4 digits):\n'))
    print('The first day of month '+str(month)+' in '+str(year)+' is '+str(first_day_of_month(month, year))+'.')
      
def main():
    print_welcome()
    
    selection = get_selection()
    while not selection==0:

        if selection==1:
            test_leap_year()
        elif selection==2:
            test_month_name()
        elif selection==3:
            
            test_days_in_month()
        elif selection==4:
            test_first_day_year()
        elif selection==5:
            test_first_day_month()
        else:
            print('That selection was not recognised.')

        selection = get_selection()
        
        
main()
