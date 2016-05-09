def compute_largest(a,b,c) :
    sum = []
    sum.append(a+b*c)
    sum.append((a+b)*c)
    sum.append(a*b+c)
    sum.append(a*(b+c))
    sum.append(a*b*c)
    sum.append(a+b+c)
    sum.sort()
    return sum[-1]

a = input()
b = input()
c = input() 
print compute_largest(a,b,c)
