# Ecrire un programme python sous forme de fonction qui prend en parametre deux listes L1 et L2 
# et renvoie la liste des elements communs à ces deux listes
liste1=input("entrer les elements de L1 : ")
liste2=input("entrer les elements de L2 : ")
L =[] # L est la liste des elements commun
def elements_commun(liste1,liste2):
    L1=liste1.split()
    L2=liste2.split()
    for i in L1 :
            if i in L2 :
                L.append(i)
elements_commun(liste1,liste2)
print("les elements communs à L1 et L2 sont : ", L)