'''
Given a list of numbers, you have to sort them in non decreasing order.
Input Format
The first line contains a single integer N, denoting the number of integers in the list.
The next N lines contain a single integer each, denoting the elements of the list.
Output Format
Output N lines, containing one integer each, in non-decreasing order.
Constraints
1≤N≤10^6
0≤0≤ elements of the list ≤10^6≤10^6

Input :5 5 3 6 7 1
Output :1 3 5 6 7
'''


# def reverseNums(n):
#     lis = []
#     for i in range(n):
#         lis.append(int(input()))
#     lis = sorted(lis)
#     for i in lis:
#         print(i)

# n = int(input())
# reverseNums(n)

l = list(map(int, input().split()))
l = sorted(l)
print(list(set(l)))