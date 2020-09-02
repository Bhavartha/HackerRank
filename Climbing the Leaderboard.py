#!/bin/python3

import os
import sys

#
# Complete the climbingLeaderboard function below.
#
def climbingLeaderboard(scores, alice):
    scores = sorted(set(scores),reverse=True)
    ans=[]
    ia=0
    isc = len(scores)-1
    while ia<len(alice) and isc>=0:
        if scores[isc]>alice[ia]:
            ans.append(isc+2)
            ia+=1
        else:
            isc-=1
    while ia<len(alice): 
        ans.append(1)
        ia+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
