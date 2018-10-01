#Prints the absolute difference between the sums of the matrix's two diagonals as a single integer.

import math
import os
import random
import re
import sys

def diagonalDifference(a):
    resa = 0
    resb = 0
            
    for i in range(len(a)):
        resa += a[i][i]
        resb += a[i][len(a)-1-i]
                        
    return abs(resa - resb)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()
