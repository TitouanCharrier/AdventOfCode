from re import *
import sys

i = 0
liste = [0,0,0,0,0,0,0]
finalcount = 0

for line in sys.stdin :
    if '' == line.rstrip():
        print("section",i,"match",liste)
        for j in range(7) :
            liste[j] = 0
        i+=1
    else :
        x = findall("hcl:#([0-9a-f]){6}",line)
        if len(x) == 1 :
            liste[0] += 1

        x = findall("pid:\d{9}",line)               
        if len(x) == 1 :
            liste[1] += 1

        x = findall("byr:\d{4}",line)
        try :
            z = str(x)[6]+str(x)[7]+str(x)[8]+str(x)[9]

            if (1920 <= int(str(z))) and (int(z) <= 2002) :
                liste[2] += 1
        except : pass

        x = findall("ecl:[a-z]{3}",line)
        try :
            y = str(x)[6]+str(x)[7]+str(x)[8]
            if y=='amb' or y=='blu' or y=='brn' or y=='gry' or y=='grn'or y=='hzl' or y=='oth' :
                liste[3] += 1
        except : pass

        x = findall("hgt:[0-9]{3}cm",line)
        y = findall("hgt:[0-9]{2}in",line)
        if len(x) == 1 :
            if 150 <= int(str(x)[6]+str(x)[7]+str(x)[8]) <= 193 :
                liste[4] += 1
        
        elif len(y) == 1 :
            if 59 <= int(str(y)[6]+str(y)[7]) <= 76 :
                liste[4] += 1

        x = findall("iyr:\d{4}",line)
        if len(x) == 1 :
            y = findall("\d{4}",str(x))
            z = str(y)[2]+str(y)[3]+str(y)[4]+str(y)[5]

            if (2010 <= int(str(z))) and (int(z) <= 2020) :
                liste[5] += 1

        x = findall("eyr:\d{4}",line)
        if len(x) == 1 :
            y = findall("\d{4}",str(x))
            z = str(y)[2]+str(y)[3]+str(y)[4]+str(y)[5]

            if (2020 <= int(str(z))) and (int(z) <= 2030) :
                liste[6] += 1
        
        count = 0
        for j in range(7) :
            if liste[j] == 1 :
                count += 1
        if count == 7 :
            finalcount += 1
print(finalcount)




























































