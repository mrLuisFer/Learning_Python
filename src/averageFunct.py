#!/bin/python3
import os
# write your code here
def avg(*nums):
    argList = list(nums)
    x = sum(argList)
    v = len(argList)
    
    return (x / v)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
