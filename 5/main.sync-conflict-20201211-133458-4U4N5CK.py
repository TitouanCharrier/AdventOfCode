
#Number seat initialized to 63 and acc to 0 like counter
def row_number(listeRow) :
    coeff = 63
    nbrRow = 63
    for i in range(7) :
        if listeRow[i] == 'F' :
            nbrRow-=coeff//2
            coeff//=2
    
        elif listeRow[i] == 'B' :
            nbrRow+=coeff//2
            coeff//=2

    return nbrRow

liste = ['F','B','F','B','B','F','R','L','R']
liste1 = ['B','F','F','F','B','B','F','R','R','R']
liste2 = ['B','B','F','F','B','B','F','R','L','L']
print(row_number(liste))
print(row_number(liste1))
print(row_number(liste2))




























































