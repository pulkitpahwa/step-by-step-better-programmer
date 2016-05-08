count = 0
for i in range(input()) : 
    if sum(map(int, raw_input().split())) > 1 : 
        count += 1 
print count
