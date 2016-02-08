#   Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#   
#   Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
#   The design should have 'WELCOME' written in the center.
#   The design pattern should only use |, . and - characters.
#   Sample Designs
#   
#       Size: 7 x 21 
#       ---------.|.---------
#       ------.|..|..|.------
#       ---.|..|..|..|..|.---
#       -------WELCOME-------
#       ---.|..|..|..|..|.---
#       ------.|..|..|.------
#       ---------.|.---------
#       
#       Size: 11 x 33
#       ---------------.|.---------------
#       ------------.|..|..|.------------
#       ---------.|..|..|..|..|.---------
#       ------.|..|..|..|..|..|..|.------
#       ---.|..|..|..|..|..|..|..|..|.---
#       -------------WELCOME-------------
#       ---.|..|..|..|..|..|..|..|..|.---
#       ------.|..|..|..|..|..|..|.------
#       ---------.|..|..|..|..|.---------
#       ------------.|..|..|.------------
#       ---------------.|.---------------
#   Input Format
#   
#   A single line containing the space separated values of N and M.
#   
#   Constraints
#   
#   5<N<101
#   15<M<303
#   Output Format
#   
#   Output the design pattern.
#   
#   Sample Input
#   
#   9 27
#   Sample Output
#   
#   ------------.|.------------
#   ---------.|..|..|.---------
#   ------.|..|..|..|..|.------
#   ---.|..|..|..|..|..|..|.---
#   ----------WELCOME----------
#   ---.|..|..|..|..|..|..|.---
#   ------.|..|..|..|..|.------
#   ---------.|..|..|.---------
#   ------------.|.------------
#   Note: 
#   More than 6 lines of code will result in a score of 0. Comment lines are counted. Blank lines are not counted.


n,m = map(int, raw_input().split())
for i in xrange(n/2) :
    a = ""
    for j in xrange(0,(n*3)/2 - 3*i-1 ):
        a += "-"
#    print ""
    for j in xrange(0,2*i+1):
        a += ".|."
    for j in xrange(0,(n*3)/2 - 3*i-1 ):
        a += "-"

    print a
print "WELCOME".center(n*3, "-")
for i in xrange(n/2-1,-1,-1) :
    a = ""
    for j in xrange((n*3)/2 - 3*i-1,0,-1 ):
        a += "-"
#    print ""
    for j in xrange(0,2*i+1):
        a += ".|."
    for j in xrange((n*3)/2 - 3*i-1,0,-1 ):
        a += "-"
    print a

