#    Task
#    
#    You are given a string S. 
#    Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#    
#    Input Format
#    
#    A single line containing a string S.
#    
#    Constraints
#    
#    0<len(S)<1000
#    Output Format
#    
#    In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
#    In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
#    In the third line, print True if S has any digits. Otherwise, print False. 
#    In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
#    In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
#    
#    Sample Input
#    
#    qA2
#    Sample Output
#    
#    True
#    True
#    True
#    True
#    True
#    
#    Link : https://www.hackerrank.com/challenges/string-validators
#    
a = raw_input()
status = [False, False, False, False, False]
for i in a :
    if i.isalpha() : 
        status[1] = True
    if i.isalnum() :
        status[0] = True
    if i.isdigit() : 
        status[2] = True
    if i.islower() :
        status[3] = True
    if i.isupper():
        status[4] = True
    
for i in status :
    print i
