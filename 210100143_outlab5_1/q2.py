#######################################

"""
Import any libraries if required
Extra functions or variables if required

"""
#######################################
import string

from exception import Lab5Exception


def weirdProblem(L):
    
    converted_string = ""

    """
    This function takes a list of lists as input and returns a string which is a
    concatenation of elements 
    Input arguments:
    L : List of lists

    Returns: converted_string
	string

    """
    L = str(L)
    array = eval(L)
    n = len(array)
    if not isinstance(array,list):
        raise Lab5Exception("Input is not a list")

    max=0
    for i in range(0,n):
        if(len(array[i])>max):
            max = len(array[i])

    for j in range(0,max):
        for i in range(0,n):
            if(not isinstance(array[i],list)):
                raise Lab5Exception("Input is not given as a list of lists")
            if(j<len(array[i])):
                if(not isinstance(array[i][j],str)):
                    raise Lab5Exception("Element is not a string")
                converted_string+=array[i][j]
                converted_string+=" "
    converted_string = converted_string[0:len(converted_string)-1]

    return converted_string


if __name__ == "__main__":

    """
    Main function

    Example call:
    You can use the following list of lists "L" for testing your solution.
    For running the code, use the command "python q2.py" 
    
    L = [ ["this", "programming", "is"], ["is", "assignment", "kinda"], ["a", "which", "weird"]  ]
    converted_string = weirdProblem(L)
    print(converted_string)

    Console output should be: this is a programming assignment which is kinda weird

    """
