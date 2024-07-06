import os

path = "/Users/saiteja/Programming/academic/3-1/CPT"

n = int(input("Enter number of files:"))

for i in range(19,n+1):
    file = f"p{i}.py"
    with open(os.path.join(path, file), 'w') as fp:
        pass