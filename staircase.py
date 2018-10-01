#Print a staircase of size n using "#" symbols and spaces.
#The last line must have 0 spaces in it.

import math
import os
import random
import re
import sys

def staircase(n):
    
    for i in range(n-1, -1, -1):
        print(" "*(i) + "#"*(n-i))
            

if __name__ == '__main__':
    n = int(input())

    staircase(n)
