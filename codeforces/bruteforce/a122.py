n = input()
count = 0
lucky = [4, 7, 44, 47, 77, 444, 447, 474, 477]
for i in lucky : 
    if n%i == 0 :
        count = 1
        break
if count == 1  :
    print "YES"
else : print "NO"  
    
