def binarySearch(arr, val):
    """
    This is a function to search for a value in a sorted array
    using binary search i.e. in log(n) time complexity.

    :param arr: Takes in the array on which binary search is to be executed. This array has to be already sorted.

    :type arr: int*

    :param val: The value of the element to search for

    :type val: int

    :return: Returns the index at which element is found if found else -1

    :rtype: int 
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (r + l) // 2
        if arr[m] > val:
            r = m-1
        elif arr[m] < val:
            l = m+1
        else:
            return m
    return -1



