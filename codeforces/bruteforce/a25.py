n = input()
def odd(i): return i%2==0
l = map(int, raw_input().split())
my_list = list(map(odd,l))
true_count = my_list.count(True)
false_count = my_list.count(False)

if true_count > false_count : 
    print my_list.index(False) + 1
else : 
    print my_list.index(True) + 1


