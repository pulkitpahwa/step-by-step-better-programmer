#    Task
#    
#    You are given a date. Your task is to find what the day is on that date.
#    
#    Input Format
#    
#    A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
#    
#    Constraints
#    
#    2000<year<3000
#    Output Format
#    
#    Output the correct day in capital letters.
#    
#    Sample Input
#    
#    08 05 2015
#    Sample Output
#    
#    WEDNESDAY
#    Explanation
#    
#    The day on August 55th 2015 was WEDNESDAY.
#    
#    Link : https://www.hackerrank.com/challenges/calendar-module
    

#solution 1

date_string = raw_input().split(" ")
month = int(date_string[0])
date = int(date_string[1])
year = int(date_string[2])
import datetime
d = datetime.date(year, month, date)
if d.weekday() == 0 : 
    print "MONDAY"
elif d.weekday() == 1 :
    print "TUESDAY"
elif d.weekday() == 2 : 
    print "WEDNESDAY"
elif d.weekday() == 3 :
    print "THURSDAY"
elif d.weekday() == 4 :
    print "FRIDAY"
elif d.weekday() == 5 :
    print "SATURDAY"
else:
    print "SUNDAY"


#solution 2
#   import calendar 
#   date_string = raw_input().split(" ")
#   month = int(date_string[0])
#   date = int(date_string[1])
#   year = int(date_string[2])
#   days  = ["MONDAY" , "TUESDAY" , "WEDNESDAY", "THURSDAY", "FRIDAY","SATURDAY" , "SUNDAY"]
#   print days[calendar.weekday(year, month, date)]
