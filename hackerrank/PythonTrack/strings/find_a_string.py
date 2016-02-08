#    In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
#    
#    NOTE: String letters are case-sensitive.
#    
#    Input Format
#    
#    The first line of input contains the original string. The next line contains the substring.
#    
#    Constraints
#    
#    1<=len(string)<=200 
#    Each character in the string is an ascii character.
#    
#    Output Format
#    
#    Output the integer number indicating the total number of occurrences of the substring in the original string.
#    
#    Sample Input
#    
#    ABCDCDC
#    CDC
#    Sample Output
#    
#    2
#    
#    Link : https://www.hackerrank.com/challenges/find-a-string
#    

def find_a_string(string, substring):
    occurences = 0
    i = 0
    while i< len(string):
        found = string[i:].find(substring)
        if found == -1 :
            break 
        else:
            occurences = occurences + 1
            i = i+found+1
            
           
    return occurences

string = raw_input()
substring = raw_input()
print find_a_string(string, substring)

