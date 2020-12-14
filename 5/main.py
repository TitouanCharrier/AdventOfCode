from re import *
import sys


def row_number(listeRow) :
    coeff = 127
    nbrRow = 0
    for i in range(7) :
        coeff//=2
        if listeRow[0][i] == 'B' :
            nbrRow+=coeff+1
    return nbrRow

def col_number(listeCol) :
    coeff = 7
    nbrCol = 0
    for i in range(7,10) :
        coeff//=2
        if listeCol[0][i] == 'R' :
            nbrCol+=coeff+1

    return int(nbrCol)

maxi = 0
listemine = []
for line in sys.stdin :
    liste = findall("[A-Z]{10}",line)
    res = row_number(liste) * 8 + col_number(liste)
    listemine.append(res)
    if res > maxi :
       maxi = res
for i in range(908) :
    if i not in listemine :
        print(i)




























































