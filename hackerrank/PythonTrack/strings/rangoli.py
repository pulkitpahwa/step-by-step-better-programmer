#    You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
#    
#    Different sizes of alphabet rangoli are shown below:
#    
#    #size 3
#    
#    ----c----
#    --c-b-c--
#    c-b-a-b-c
#    --c-b-c--
#    ----c----
#    
#    #size 5
#    
#    --------e--------
#    ------e-d-e------
#    ----e-d-c-d-e----
#    --e-d-c-b-c-d-e--
#    e-d-c-b-a-b-c-d-e
#    --e-d-c-b-c-d-e--
#    ----e-d-c-d-e----
#    ------e-d-e------
#    --------e--------
#    
#    #size 10
#    
#    ------------------j------------------
#    ----------------j-i-j----------------
#    --------------j-i-h-i-j--------------
#    ------------j-i-h-g-h-i-j------------
#    ----------j-i-h-g-f-g-h-i-j----------
#    --------j-i-h-g-f-e-f-g-h-i-j--------
#    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#    j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
#    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#    --------j-i-h-g-f-e-f-g-h-i-j--------
#    ----------j-i-h-g-f-g-h-i-j----------
#    ------------j-i-h-g-h-i-j------------
#    --------------j-i-h-i-j--------------
#    ----------------j-i-j----------------
#    ------------------j------------------
#    The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
#    
#    Input Format
#    
#    Only one line of input containing N, the size of the rangoli.
#    
#    Constraints
#    
#    0<N<27
#    Output Format
#    
#    Print the alphabet rangoli in the format explained above.
#    
#    Sample Input
#    
#    5
#    Sample Output
#    
#    --------e--------
#    ------e-d-e------
#    ----e-d-c-d-e----
#    --e-d-c-b-c-d-e--
#    e-d-c-b-a-b-c-d-e
#    --e-d-c-b-c-d-e--
#    ----e-d-c-d-e----
#    ------e-d-e------
#    --------e--------
#    
#    
#    Link : https://www.hackerrank.com/challenges/alphabet-rangoli
#    

n = input()
length = n*3
for i in xrange(0, n) : 
    a = ""
    for j in xrange(0, (length/2 + 1) - 2*i) : 
        a += "-"
    for j in xrange(96 + n + 1, 96 + n - i, -1 ) :
        a += chr(j-1)
        if not j == (96+n-i+1):
            a += "-"
    b = ""
    for j in xrange(96 + n , 96 + n - i, -1  ) :
        b += chr(j)
        b += "-"
    b = b[::-1]
    for j in xrange(0, (length/2 + 1) - 2*i ) : 
        b += "-"
    print a+b

for i in xrange(n-1 , 0, -1) : 
    a = ""
    b = ""
    for j in xrange(n-i, 0,-1 ) : 
        a += "--"
    for j in xrange(96 + n , 96 + n - i, -1 ) :
        a += chr(j-1)
        if not j == (96+n-i+1):
            a += "-"
    for j in xrange(96 + n -i , 96 + n  ) :
        b += chr(j)
        b += "-"
    b = b[::-1]
    for j in xrange(0, (length/2 + 1) - 2*i ) : 
        b += "-"
    print a+b
#for i in xrange(n,0,-1) : 
#    a = ""
#    for j in xrange((length/2 + 1) - 2*i, 0, -1) : 
#        a += "-"
#    for j in xrange(96 + n -i  + 1, 96 + n +1 ) :
#        a += chr(j-1)
#        if not j == (96+n+2):
#            a += "-"
#    b = ""
#    for j in xrange(96 + n - i , 96 + n ) :
#        b += chr(j)
#        b += "-"
#    b = b[::-1]
#    for j in xrange((length/2 + 1) - 2*i , 0 ,-1 ) : 
#        b += "-"
#    print a+b
#
#
#
