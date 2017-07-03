#!/usr/bin/python
import sys

maxValue = 4000000
if len(sys.argv) > 1:
    maxValue = int(sys.argv[1])


elementn1 = 2
elementn2 = 1
elemn = 0
sumatoria = 2

while elemn < maxValue:
    if elemn % 2 == 0:
        sumatoria += elemn        
    elemn = elementn1 + elementn2
    elementn2 = elementn1
    elementn1 = elemn

print(sumatoria)
    
