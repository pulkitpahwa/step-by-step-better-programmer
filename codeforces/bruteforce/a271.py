a = input()
while True :
    a = a+1
    b = str(a)
    if len(set(list(b))) == len(b) : 
        print b
        break
    else :
        continue
