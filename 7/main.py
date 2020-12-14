import re
import sys

puzzle = []

for line in sys.stdin :
    puzzle.append(line)

amorce = " shiny gold"

def detect(subject) :
    listeOk = []
    for line in puzzle :
        out = re.search(subject,line)
        if out != None :
            color = re.search("^[a-z]+.[a-z]+",line)
            if color.group() not in listeOk :
                listeOk.append(color.group())
    return listeOk
res = []
step = detect(amorce)
while 1 :
    for i in range(len(step)) :
        for color in detect(step[i]) :
            #print(detect(step[i]))
            if color not in step :
                step.append(color)
    print(len(step))
    break

liste = [1, [2, [3,4]]]


        



































































