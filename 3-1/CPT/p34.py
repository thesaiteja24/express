'''
There is an array of integers. There are also 2 disjoint sets, A and , B each containing integers. You like all the integers in set A and dislike all the integers in set B . Your initial happiness is 0. For each integer in the array, if I belongs to A, you add i to your happiness. If ,I belongs to B you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since A and B are sets, they have no repeated elements. However, the
array might contain duplicate elements.
Constraints
1<=n<=10^5
1<=m<=10^5
1<=Any integer in the input<=10^9
Input Format
The first line contains integers n and m separated by a space. The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.
Output Format
Output a single integer, yo7ur total happiness.
Sample Input
3 2
1 5 3
3 1
5 7
Sample Output
1
'''
n, m = input().split()
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
A, B = input().split()
h = 0  
for i in l1:
    if i == int(A):
        h += 1

for i in l2:
    if i == int(B):
        h -= 1
print(h)