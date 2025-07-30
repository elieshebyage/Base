# Ecrire un programme python qui permet de supprimer les elements dupliqués d'une liste
liste=input("entrer les elements de la liste : ")
L=liste.split()
n=len(L)
D=[]
for i in range (0,n) :
    if L[i] not in D :
        D.append(L[i])  
print("la liste des elements unique est : ",D)