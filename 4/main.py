from re import *
import sys
i = 0
liste = [0]
for line in sys.stdin :
    if 'exit' == line.rstrip():
        break
    if '' == line.rstrip():
        liste.append(0)
        i+=1
    else :
        x = findall("...:",line)
        if x != None :
            for k in x :
                if k != 'cid:' :
                    liste[i] += 1

finalcount = 0
for j in range(len(liste)) :
    if liste[j] == 7 :
        finalcount += 1
print(finalcount," Done")



























































