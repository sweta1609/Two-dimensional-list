from sys import stdin

def rowWiseSum(mat, nRows, mCols):
    #Your code goes here
    output = []
    for i in range (nRows):
        sum = 0
        for j in range (mCols):
            sum += mat[i][j]
        output.append(sum)
    print (*output)

