#!/usr/bin/env python3
import re                            
import sys                                                         

puzzle = []                                                                                                           

for line in sys.stdin :                                                                                               
    puzzle.append(line)
cible = "shiny gold"
def count(cible, counter) :
    for line in puzzle :
        sujet = re.search("^"+cible,line)
        if sujet != None :
            listeNeeds = re.findall("[0-9]+.[a-z]+.[a-z]+",line)
            if len(listeNeeds) == 0 :
                return 1
            else :
                for i in range(len(listeNeeds)) :
                    tmpNum = re.search("[0-9]+",listeNeeds[i])
                    Number = int(tmpNum.group())
                    tmpTitle = re.search("[a-z]+.[a-z]+",listeNeeds[i])
                    Title = tmpTitle.group()
                    Number += count(Title, Number)
        else : return 0
print(count(cible, 1))



































































