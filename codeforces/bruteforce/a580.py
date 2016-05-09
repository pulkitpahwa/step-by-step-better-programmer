def calculate_max_non_decreasing_segment(l):
    if len(l) == 1 :
        return 1
    if len(l) == 0:
        return 0
    count = 1
    counts = []
    for i in xrange(1,len(l)):
#        print l[i]
        if l[i] >= l[i-1] :
            count += 1
            #print count, l[i]
        else : 
            counts.append(count)
            count = 1
        counts.append(count)
#        print i, count, l[i]
    counts.sort()
    return counts[-1]


a = input()
l = map(int, raw_input().split())
print calculate_max_non_decreasing_segment(l)
