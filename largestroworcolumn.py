from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    if nRows == 0:
        print('row',0,-2147483648)
        return
    #nRows = len(arr)
    #mCols = len(arr[0])
    max_sum = -1
    max_index = -1
    for j in range (mCols):
        sum = 0 
        for ele in arr:
            sum += ele[j]
        if sum>max_sum:
            max_sum = sum
            max_index = j
    max_rsum = -1
    max_rindex = -1
    for i in range (nRows):
        sum =0 
        for j in range(mCols):
            sum += arr[i][j]
        if sum >max_rsum:
            max_rsum = sum
            max_rindex = i
    if max_sum>max_rsum:
        print('column',max_index,max_sum)
    else:
        print('row',max_rindex,max_rsum)
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
    findLargest(mat, nRows, mCols)

    t -= 1
