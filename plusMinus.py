#This program prints:
#A decimal representing of the fraction of positive numbers in the array compared to its size.
#A decimal representing of the fraction of negative numbers in the array compared to its size.
#A decimal representing of the fraction of zeros in the array compared to its size.

import math
import os
import random
import re
import sys

def plusMinus(arr):
    
    pos = 0
    neg = 0
    zero = 0
    
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zero += 1
            
    pos = pos/len(arr)
    neg = neg/len(arr)
    zero = zero/len(arr)
       
    return("%.6f" % pos, "%.6f" % neg, "%.6f" % zero)
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    res = plusMinus(arr)
    
    for i in range(len(res)):
        print(res[i])
