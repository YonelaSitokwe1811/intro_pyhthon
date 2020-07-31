name_of_month = (input("Enter the month('January',...,'December') :\n"))
first_weekday = input("Enter start day('Monday',...,'Sunday') :\n")
number_of_days=31

month={'January','February','March','April','May','June','July','August','September','October','November','December'}
weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
print('{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'
      .format( 'M', 'T', 'W', 'Th', 'F', 'Sa','Su'))

print (weekdays[first_weekday]*4*' ' + '{:>3}'.format(1), end=' ')
for current_day in range(1, number_of_days+1):
    if (weekdays[first_weekday] + current_day) % 7 == 0:
        print ()
    print ('{:>3}'.format(current_day ), end=' ')
