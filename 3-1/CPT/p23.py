'''
Sita and Geetha are playing with dice. In one turn, both of them roll their dice at once.
They consider a turn to be good if the sum of the numbers on their dice is greater than 6.
Given that in a particular turn Sita and Geetha got X and Y on their respective dice, find whether the turn was good.
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case contains two space-separated integers X and Y — the numbers Sita and Geetha got on their respective dice.
Output Format
For each test case, output on a new line, YES, if the turn was good and NO otherwise.
Each character of the output may be printed in either uppercase or lowercase. That is, the strings NO, no, nO, and No will be treated as equivalent.
Constraints 1≤T≤100
1≤X,Y≤6

Input : 4	Output:
1 4	NO
4	YES
2	NO
2 6	YES
'''
T = int(input())
lis = []
for i in range(T):
    X, Y = input().split()
    lis.append(int(X)+int(Y))

for i in lis:
    if int(i) > 6:
        print("YES")
    else:
        print("NO")