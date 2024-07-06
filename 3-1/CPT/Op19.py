'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:
Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1: Input: s = "()" Output: true
Example 2:
Input: s = "()[]{}" Output: true 
Example 3:
Input: s = "(]" Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

testCase1 = "()"
testCase2 = "()[]{}"
testCase3 = "(]"

print(isValid(testCase1))
print(isValid(testCase2))
print(isValid(testCase3))

