#!/usr/bin/python
import sys

maxN = 1000
if len(sys.argv) > 1:
    maxN = int(sys.argv[1])

sumatoria = 0
for i in range(maxN):
    if (i % 3 == 0) or (i % 5 == 0):
        sumatoria += i
print(sumatoria)
