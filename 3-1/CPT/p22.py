'''
Recently, Ravi visited his doctor. The doctor advised Chef to drink at
least 2000 ml of water each day.
Ravi drank X ml of water today. Determine if Ravi followed the doctor's advice or not.
Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains one integer X — the amount of water Ravi drank today.
Output Format
For each test case, output YES if Ravi followed the doctor's advice of drinking at least 2000 ml of water. Otherwise, output NO.
You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).
Constraints 1≤T≤2000
1≤X≤4000
Input :	Output:
3	YES
2999	NO
1450	YES
2000
'''

T = int(input())
lis = []
for i in range(T):
    lis.append(int(input()))
for i in lis:
    if i < 2000:
        print("NO")
    else:
        print("YES")