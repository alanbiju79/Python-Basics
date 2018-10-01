#Find the maximum sum and the minimum sum from an array

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    
    arr.sort()
    low = 0
    high = 0
    
    for i in range(len(arr)-1):
        low += arr[i]
        
    for i in range(1, len(arr)):
        high += arr[i]
        
    print(low, high)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
