from logging import exception
from exception import Lab5Exception

##############################################
"""
Extra functions or variables if required

"""
##############################################


def rotate(arr):

    rotated_array = []

    """
    This function takes a list of lists as input and returns the rotated verion 
    (rotated 90 degrees anti-clockwise)

    Input arguments:
    arr : List of lists

    Returns: rotated_array

    """
    arr = str(arr)
    array = eval(arr)
    n = len(array)
    if(not isinstance(array,list)):
        raise Lab5Exception("Input not a list")
    if(n==1 and len(array[0])==0):
        raise Lab5Exception("Matrix of size 0 not allowed")
    for i in range(0,n):
        if(not isinstance(array[i],list)):
            raise Lab5Exception("Rows and Columns not given as lists")
        if len(array[i]) != n:
            raise Lab5Exception("Not a square matrix")
    for i in range(0,n):
        sublen = len(array[i])
        for j in range(0,sublen):
            if(not isinstance(array[i][j],int)):
                raise Lab5Exception("Element not an integer")
    for i in range(n-1,-1,-1):
        l = [array[j][i] for j in range(0,n)]
        rotated_array.append(l)

    return rotated_array


# Use the main() function only for testing your code

if __name__ == "__main__":
    
    """
    Main function

    Example call:
    You can use the following matrix "test_arr" for testing your solution.
    For running the code, use the command "python q1.py" 
    
    test_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotated_array = rotate(test_arr)
    print(rotated_array)

    Console output should be: [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]

    """