n = input()
a = []
if n== 1 :
    print 1
else :
    for i in xrange(0,n):
        a.append([1])
    
    for i in xrange(0,n) :
        for j in xrange(0,n-1) : 
            if i == 0 :
                a[i].append(1)
            else : 
                a[i].append(0)
    
    b=  []
    
    for i in xrange(1,n):
        for j in xrange(1,n):
            a[i][j] = a[i-1][j] + a[i][j-1]
            b.append(a[i][j])
    
    b.sort()
    print b[-1]
