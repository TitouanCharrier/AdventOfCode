#!/usr/bin/env python3

import re
import sys
import time

File = []
for line in sys.stdin :
    File.append(line)
i = 0
acc = 0
while 1 :
    time.sleep(0.01)
    tmpcommand = re.search("[a-z]{3}",File[i])
    tmpnum = re.search('.[0-9]+',File[i])
    if tmpcommand != None and tmpnum != None:
        command = tmpcommand.group()
        num = int(tmpnum.group())
        print(i,File[i])
        File[i] = '+0 stp'
        if command == 'nop' :
            i+=1
        if command == 'jmp' :
            i+=num
        if command == 'acc' :
            acc += num
            i+=1
        if command == 'stp' :
            break
    else :
        i += 1 
print(acc)
































































