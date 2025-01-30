date = "2019-01-09"
year, month, day = map(int, date.split("-"))#splits into year month day

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#input of all sum of days in month

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):#checks wethere february is a leap year
    days_in_month[1] = 29

day_number = sum(days_in_month[:month-1]) + day #here it takes the sum of all the months and the the no of days passed and then sums it

print(day_number)