'''Ecrire un programme python qui permet de realisé la difference symetrique de deux listes L1 et L2 
c à d la liste formée des elements de L& qui ne sont pas dans L2 quine sont pas dans L1 '''
liste1=input("entrer la liste L1 :")
liste2=input("entrer la liste L2 :")
L=[] # L est la liste dela difference symetrique
# split permet de transformer la variable en une liste
L1=liste1.split()
L2=liste2.split()
for i in L1  :
    if i not in L2 :
        L.append(i)
for a in L2 :
    if a not in L1 :
        L.append(a)
print(" la difference symetrique entre L1 et L2 est : ", L)