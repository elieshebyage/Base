# Ecrire un programme en python permettant de realiser la difference de deux liste donné par l'utilisateur 
# c'est à dire les elements qui se trouve dans la premier liste mais pas dans la deuxiemme
liste1=input("entrer la liste L1 :")
liste2=input("entrer la liste L2 :")
L=[] # L est la liste dela difference 
# split permet de transformer la variable en une liste
L1=liste1.split()
L2=liste2.split()
for i in L1 :
    if i not in L2 :
        L.append(i)
print(" la difference entre L1 et L2 est : ",L)
