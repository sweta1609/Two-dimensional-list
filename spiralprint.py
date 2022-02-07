from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    if not mat or not len(mat):
        return
 
    top = left = 0
    bottom = len(mat) - 1
    right = len(mat[0]) - 1
 
    while True:
        if left > right:
            break
 
        # print top row
        for i in range(left, right + 1):
            print(mat[top][i], end=' ')
        top = top + 1
 
        if top > bottom:
            break
 
        # print right column
        for i in range(top, bottom + 1):
            print(mat[i][right], end=' ')
        right = right - 1
 
        if left > right:
            break
            
        for i in range(right, left - 1, -1):
            print(mat[bottom][i], end=' ')
        bottom = bottom - 1
 
        if top > bottom:
            break
 
        # print left column
        for i in range(bottom, top - 1, -1):
            print(mat[i][left], end=' ')
        left = left + 1
 
#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
