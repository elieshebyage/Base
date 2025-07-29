'''Ecrire un programme en python permettant d'afficher pour une chaine de caracteres donné, le nombre d'occurrences
de chaque caractere dans la chaine '''
s=input("entrer la chaire des caracteres : ")
n=len(s)
L=[]
for i in range(0,n) :
    if s[i] not in L:
        L.append(s[i])
        print("le caractere : ", s[i] , "figure", s.count(s[i]), "fois dans la chaine s")