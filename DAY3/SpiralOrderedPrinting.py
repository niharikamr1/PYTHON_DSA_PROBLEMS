def SpiralOrder(matrix, m, n):

    top = 0
    bottom = m - 1 # rows - 1

    left = 0
    right = n - 1 # cols - 1

    while top<=bottom and left<= right:

        #Left to Right
        for i in range(left,right+1):
            print(matrix[top][i],end=" ")
        top += 1

        #Top to Bottom
        for i in range(top, bottom+1):
            print(matrix[i][right], end=" ")
        right -= 1

        #Right to Left 
        if top <= bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
            bottom -= 1

        #Bottom to Top
        if left <= right:
            for i in range(bottom, top-1,-1):
                print(matrix[i][left],end=" ")
            left += 1

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]    

SpiralOrder(matrix,3,3)