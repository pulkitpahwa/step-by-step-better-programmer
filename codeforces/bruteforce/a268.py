n = input()
host = []
guest = []
for i in xrange(0,n):
    b = [x for x in raw_input().split()]
    host.append(b[0])
    guest.append(b[1])

count = 0
for i in host :
    count += guest.count(i)

print count
