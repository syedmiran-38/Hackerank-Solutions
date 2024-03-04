#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    mins = maxs = 0
    minscore = maxscore = scores[0]
    
    for i in range(1, len(scores)):
        if minscore < scores[i]:
            minscore = scores[i]
            mins += 1
        elif maxscore > scores[i]:
            maxscore = scores[i]
            maxs += 1
    
    return mins, maxs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
