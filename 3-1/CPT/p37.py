'''
DATE: 3/7/24
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
Input Format
The first line contains a string, S.
The second line contains the width, w.

Constraints
0 < len(S) < 1000
0 < w < len(S)

Output Format
Print the text wrapped paragraph. Sample Input 0 ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD EFGH IJKL IMNO QRST UVWX YZ
'''

s = input()
w = int(input())
result = ''
for i in range(0, len(s), w):
    result += s[i:i+w] + ' '
print(result)