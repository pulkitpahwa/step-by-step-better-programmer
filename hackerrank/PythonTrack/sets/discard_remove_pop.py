#    Task
#    You have a non-empty set s, and you have to execute N commands given in N lines.
#    
#    The commands will be pop, remove and discard.
#    
#    Input Format
#    
#    The first line contains integer n, the number of elements in the set s. 
#    The second line contains nn space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9. 
#    The third line contains integer N, the number of commands.
#    The next N lines contains either pop, remove and/or discard commands followed by their associated value.
#    
#    Constraints
#    
#    0<n<20
#    0<N<20
#    
#    Output Format
#    
#    Print the sum of the elements of set ss on a single line.
#    
#    Sample Input
#    
#    9
#    1 2 3 4 5 6 7 8 9
#    10
#    pop
#    remove 9
#    discard 9
#    discard 8
#    remove 7
#    pop 
#    discard 6
#    remove 5
#    pop 
#    discard 5
#    Sample Output
#    
#    4
#    Explanation
#    
#    After completing these 10 operations on the set, we get set([4]). Hence, the sum is 4
#    
#    Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.

#    Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = input()
s = set(map(  int, raw_input().split() )   )
N = input()

for i in xrange(0,N) :
    inputs = [i for i in raw_input().split()]
    if len(inputs) > 1 :
        inputs[1] = int(inputs[1])
    if inputs[0] == "pop" :
        s.pop()
    elif inputs[0] == "remove" : 
        try :
            s.remove(inputs[1])
        except :
            pass
    elif inputs[0] == "discard" :
        s.discard(inputs[1])
    else :
        pass
print sum(s)
