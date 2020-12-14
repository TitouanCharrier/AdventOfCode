import re
import sys

liste = []
membre = 0
membreliste = []
i = -1
acc = 0
for line in sys.stdin :
    if line.rstrip()== "" :
        liste.append([0]*122)
        i+=1
        membreliste.append(membre)
        membre = 0
    else :
        answer = re.findall("[a-z]+",line)
        if len(answer) != 0 :
            for j in range(1,len(answer[0])-1) :
                liste[i][ord(answer[0][j])] += 1
        membre += 1
for k in range(i+1) :
    for l in range(97,123) :
        print(liste[k], membreliste[k+1])
        if liste[k][l] == membreliste[k] :
            acc += 1
print(acc)
