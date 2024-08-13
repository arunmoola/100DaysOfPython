secs_in_min = 60
mins_in_hr = 60
hrs_in_day = 24
days_in_yr = 365

secs_in_yr = secs_in_min * mins_in_hr * hrs_in_day * days_in_yr

secs_in_leap_yr = secs_in_min * mins_in_hr * hrs_in_day * (days_in_yr+1)

year = int(input("Enter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if is_leap:
    print('{} is a leap year'.format(year))
    print('{} seconds are in the year {}'.format(secs_in_leap_yr, year))
else:
    print('{} is not a leap year'.format(year))
    print("{} seconds are in the year {}".format(secs_in_yr, year))