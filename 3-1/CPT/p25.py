'''
Chef is fond of burgers and decided to make as many burgers as possible.
Chef has A patties and B buns. To make 1 burger, Chef needs 1 patty
and 1 bun.
Find the maximum number of burgers that Chef can make.
Input Format
The first line of input will contain an integer T — the number of test cases.
The description of T test cases follows.
The first and only line of each test case contains two space-separated
integers A and B, the number of patties and buns respectively.
Output Format
For each test case, output the maximum number of burgers that Chef can
make.
Constraints
1≤T≤1000
1≤A,B≤105
Input: 4	Output:
2 2	2
2 3	2
3 2	2
23 17	17
'''

T = int(input())
lis = []

for i in range(T):
    A, B = input().split()
    lis.append(min(int(A),int(B)))
for i in lis:
    print(i)