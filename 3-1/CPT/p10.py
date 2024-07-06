def generatePascalTriangle(numRows):
    triangle = []
    
    for i in range(numRows+1):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle[numRows]

print(generatePascalTriangle(3))
print(generatePascalTriangle(0))
print(generatePascalTriangle(1))