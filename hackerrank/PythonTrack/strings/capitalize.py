#   You are given a string S. Your task is to capitalize each word of S.
#   
#   Input Format
#   
#   A single line of input containing the string, S.
#   
#   Constraints
#   
#   0<len(S)<1000
#   The string consists of alphanumeric characters and spaces.
#   
#   Output Format
#   
#   Print the capitalized string, S.
#   
#   Sample Input
#   
#   hello world
#   Sample Output
#   
#   Hello World
#   
#   Link :https://www.hackerrank.com/challenges/capitalize

string = raw_input().split(" ")
for i in xrange(len(string)) : 
    string[i] = string[i].capitalize()
print " ".join(string)

