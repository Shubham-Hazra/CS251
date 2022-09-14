from math import floor,sqrt
from unittest import result
from exception import Lab5Exception
from functools import reduce
import matplotlib.pyplot as plt


# Running your solution - You can run this script in console with the command given in the next line
# python q2.py 10
# Here 10 is the input provided by the user. Hence the output should be the list of prime numbers less than or equal to 10. Your console output shpuld be:
# List of primes = [2,3,5,7]

########################################## Script starts here ########################################
import argparse 
# This python module can be used for getting the input provided by user
parser = argparse.ArgumentParser()
parser.add_argument('integer', metavar='N', type=int)
args = parser.parse_args()
num = args.integer


def get_primes(num):
   # Should take an integer as input and reutrn a list of primes less than or equal to the given input
   bool_val = [(i,False) for i in range(2,num+1)]
   result = bool_val.copy()
   num_list = [i for i in range(2,num+1)]
   root = [i for i in range(2,floor(sqrt(num))+1)]
   checker = lambda a,x,i: True if x==True else (bool(a%i==0) if a>i else False)
   root_list = lambda i : [i for j in range(2,num+1)]
   for k in range(2,floor(sqrt(num))+1):
      result = map(checker,num_list,result,root_list(k))
   final_list = list(map(lambda x:x[0],filter(lambda x:x[1]==False,map(lambda x,i:(x,i),num_list,result))))
   print("List of primes = ",final_list)
   x_vals = final_list
   y_vals = final_list
   plt.scatter(x_vals,y_vals)
   plt.title("Prime numbers till {}".format(num))
   plt.show()



# the variable num should be declared before the main() function as a global variable

if __name__ == '__main__':
    # Edit this part of the code in order to pass the argument to get_primes() function
    # num is the argument you got from command line using argparse module
    get_primes(num)
    
    
