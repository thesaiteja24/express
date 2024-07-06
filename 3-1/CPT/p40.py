'''
You are given a two lists A and B. Your task is to compute their cartesian
product A x B.
Example
A = [1, 2]
B = [3, 4]
A x B = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note: A and B are sorted lists, and the cartesian product’s tuples should be
output in sorted order.
Input Format
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.
Constraints
0 < A < B
0 < B < 30
Output Format
Output the space separated tuples of the cartesian product.
Sample Input
1 2
3 4
Sample Output
(1, 3) (1, 4) (2, 3) (2, 4)
'''

# Python3 code to demonstrate working of
# Construct Cartesian Product Tuple list
# using list comprehension

# initialize list and tuple
test_list = [1, 2]
test_tup = (3, 4)

# printing original list and tuple
# print("The original list : " + str(test_list))
# print("The original tuple : " + str(test_tup))

# Construct Cartesian Product Tuple list
# using list comprehension
res = [(a, b) for a in test_tup for b in test_list]
# printing result
result = sorted(res)
print(res)
