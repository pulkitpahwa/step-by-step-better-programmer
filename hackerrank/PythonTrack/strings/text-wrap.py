#    Task
#    
#    You are given a string S and width w. 
#    Your task is to wrap the string into a paragraph of width w.
#    
#    Input Format
#    
#    The first line contains a string, S. 
#    The second line contains the width, w.
#    
#    Constraints
#    
#    0<len(S)<1000 
#    0<w<len(S)
#    Output Format
#    
#    Print the text wrapped paragraph.
#    
#    Sample Input
#    
#    ABCDEFGHIJKLIMNOQRSTUVWXYZ
#    4
#    Sample Output
#    
#    ABCD
#    EFGH
#    IJKL
#    IMNO
#    QRST
#    UVWX
#    YZ  

# Link : https://www.hackerrank.com/challenges/text-wrap

import textwrap
string = raw_input()
length = input()
wraps =  textwrap.wrap(string,length)
for i in wraps :
    print i
