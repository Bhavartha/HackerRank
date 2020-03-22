#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
  left={}
  right={}
  val=0
  for i in arr:
    if i not in right:
      right[i]=1
    else:
      right[i]+=1
  for i in arr:
    right[i]-=1
    try:
      if i%r==0 and left[i//r]>0 and right[i*r]>0:
        val+=(left[i//r]*right[i*r])
    except:
      pass
    if i in left:
      left[i]+=1
    else:
      left[i]=1
  return val
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
