#    There is an array of nn integers. There are also 2 disjoint sets, A and B, each containing m integers. 
#    You like all the integers in set AA and dislike all the integers in set BB. Your initial happiness is 00. 
#    For each i integer in the array, if i is in  A, you add 1 to your happiness. If i is in B, you add -1 to your happiness. 
#    Otherwise, your happiness does not change. Output your final happiness at the end.
#    
#    Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
#    
#    Constraints 
#    1<=n<=1051<=n<=105 
#    1<=m<=1051<=m<=105 
#    1<=Any integer in the input<=10**9
#    
#    Input Format
#    
#    The first line contains integers n and m separated by a space. 
#    The second line contains nn integers, the elements of the array. 
#    The third and fourth lines contain m integers, A and B, respectively.
#    
#    Output Format
#    
#    Output a single integer, your total happiness.
#    
#    Sample Input
#    
#    3 2
#    1 5 3
#    3 1
#    5 7
#    Sample Output
#    
#    1
#    Explanation
#    
#    You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.
#    
#    Hence, the total happiness is 2-1=1
#    
#    Link :https://www.hackerrank.com/challenges/no-idea

n,m = (int(i) for i in raw_input().split())
array = [int(i) for i in raw_input().split()]
A = set([int(i) for i in raw_input().split()])
B = set([int(i) for i in raw_input().split()])
positive = [ 1 if i in A else 0 for i in array]
negative = [ -1 if i in B else 0 for i in array]
print positive.count(1) - negative.count(-1)
