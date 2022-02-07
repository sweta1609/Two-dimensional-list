from sys import stdin

def wavePrint(mat, nRows, mCols):
    #Your code goes here
    for i in range (mCols):
        if i%2 == 0:
            for j in range (nRows):
                print(mat[j][i],end=" ")
        else:
            for j in range(nRows-1,-1,-1):
                print(mat[j][i],end = " ")
        

