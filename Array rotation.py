import math
import os
import random
import re
import sys

T = int(input())

for i in range(T):

    ND = input().split()
    N = int(ND[0])
    D = int(ND[1])

    a = list(map(int, input().split()))

    a.extend(a[:D])
    del (a[:D])

    for j in range(N):
        print(a[j])
    print('')