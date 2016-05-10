n = input()
a = [int(i) for i in raw_input().split()]
minimum = a[0]
maximum = a[0]
count = 0
for i in a :
    if i<minimum :
        minimum = i
        count += 1
    elif i> maximum :
        maximum  = i
        count += 1
    else :pass

print count
