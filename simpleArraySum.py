#This program adds the contents of an integer array together

import os
import sys

def simpleArraySum(ar):
    res = 0
    
    for i in ar:
        res = res+i
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
