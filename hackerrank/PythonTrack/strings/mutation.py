#    Task 
#    Read a given string, change the character at a given index and then print the modified string.
#    
#    Input Format 
#    The first line contains a string, S. 
#    The next line contains an integer i, denoting the index location and a character c separated by a space.
#    
#    Output Format 
#    Using any of the methods explained above, replace the character at index i with character c.
#    
#    Sample Input
#    
#    abracadabra
#    5 k
#    Sample Output
#    
#    abrackdabra
#    
#    Link : https://www.hackerrank.com/challenges/python-mutations/

string = raw_input()
index, character = raw_input().split(" ")
index = int(index)
new_string = string[:index] + character + string[index+1:]
print new_string
