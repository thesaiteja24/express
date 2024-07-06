'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be N X M. (N is an odd natural number, and M is 3 times N.) The design should have ‘WELCOME’ written in the center.
The design pattern should only use |, . and – characters.
Sample Designs
Size: 7 x 21
 	.|. 	
 	.|..|..|. 	
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
 	.|..|..|. 	
 	.|. 	

Size: 11 x 33
 	.|. 	
 	.|..|..|. 	
 	.|..|..|..|..|. 	
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
 	WELCOME 	
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
 	.|..|..|..|..|. 	
 	.|..|..|. 	
 	.|. 	
Input Format
A single line containing the space separated values of N and M.
Constraints
5 < N < 101
15 < M < 303
Output Format
Output the design pattern.
Sample Input
9 27



Sample Output
 	. | .  	
 	. | . . | . . | .  	
------ . | . . | . . | . . | . . |. ------
--- . | . . | . . | . . | . . | . . | . . | . ---
 	WELCOME 	
--- . | . . | . . | . . | . . | . . | . . | . ---
------ . | . . | . . | . . | . . | . ------
 	. | . . |. . | .  	
 	. | .  	
'''

# N, M = map(int, input().split())

# # Check if the input is valid
# if N % 2 == 0 or M != 3 * N:
#     print("Invalid input. N must be an odd natural number and M must be 3 times N.")
#     exit()

# # Helper function to generate the pattern
# def generate_pattern(n):
#     pattern = ''
#     for i in range(1, n+1, 2):
#         pattern += '.' * ((n-i)//2) + '|' * i + '.' * ((n-i)//2) + '\n'
#     return pattern

# # Generate the door mat design
# top_bottom = '-' * ((M-7)//2)
# middle = 'WELCOME'
# pattern = generate_pattern(N)

# print(top_bottom + '.|.' + top_bottom)
# for i in range(N//2):
#     print(top_bottom + '.|' * (i+1) + '.|' * i + top_bottom)

# print(top_bottom + middle + top_bottom)

# for i in range(N//2-1, -1, -1):
#     print(top_bottom + '.|' * (i+1) + '.|' * i + top_bottom)

# print(top_bottom + '.|.' + top_bottom)

n, m = map(int, input().split())
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))

