# Function to find the common elements in all the rows of the specified matrix
def findCommon(mat):
 
    # base case
    if not mat or not len(mat):
        return set()
 
    d = {}
 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
 
            # insert elements of the first row into the dictionary and
            # initialize them with a value of 1
            if i == 0:
                d[mat[0][j]] = 1
 
                # if matrix contains the single row, print all its elements
                if len(mat) == 1:
                    print(mat[i][j], end=' ')
 
            # from the second row onwards, check if the current element exists
            # in the dictionary and first in the current row
            if i > 0 and mat[i][j] in d and d[mat[i][j]] == i:
                # increment the count of the element by 1
                d[mat[i][j]] = i + 1
 
                # if `i` represent the last row, print the element
                if i == len(mat) - 1:
                    print(mat[i][j], end=' ')
 
 
if __name__ == '__main__':
 
    mat = [
        [2, 4, 3, 8, 7],
        [4, 7, 1, 3, 6],
        [3, 5, 2, 1, 3],
        [4, 5, 0, 2, 3]
    ]
 
    findCommon(mat)
