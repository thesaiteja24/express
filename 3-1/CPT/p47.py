'''
NOTE 4/7/24
You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
->Number can start with +, - or . symbol.

For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖ -+4.5
->Number must contain at least 1 decimal value.


For example:
✖ 12.
✔12.0
->Number must have exactly one . symbol.
->Number must not give any exceptions when converted using float(N).

Input Format
The first line contains an integer T, the number of test cases. The next T line(s) contains a string N.
Constraints
0 < T < 10

Output Format
Output True or False for each test case.

Sample Input 0
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 0
False True True False
'''
import re

def is_valid_float(N):
    # Check for exactly one '.' symbol
    if N.count('.') != 1:
        return False
    
    # Ensure it has at least one decimal digit
    if re.fullmatch(r'[+-]?\d*\.\d+', N) is None:
        return False
    
    # Ensure valid conversion to float
    try:
        float(N)
    except ValueError:
        return False
    
    return True

l = []

for i in range(int(input())):
    s = input()
    l.append(is_valid_float(s))
for i in l:
    print(i)