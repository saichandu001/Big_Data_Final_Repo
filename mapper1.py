#!/usr/bin/env python3
import sys

k = 0 
for i in sys.stdin:
    i = i.split(",")
    k += 1
    print( f'{i[4]}\t{i[5]}\t{i[7]}\t{i[8]}\t{i[9]}\t{i[10]}\t{i[11]}\n', end='')
    