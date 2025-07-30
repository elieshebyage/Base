''' ecrire un programme qui regroupe dans une liste tous les noms commencant 
par une majuscules dans une chaine donnée  s '''
s=input("entrer la chaine : ")
liste=s.split()
word_maj=[]
for i in liste :
    if i[0].isupper() :
        word_maj.append(i)
print(word_maj)