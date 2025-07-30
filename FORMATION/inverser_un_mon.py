''' Ecrire un programme qui demande à l'utilisateur de saisir un mot et de lui renvoyer son inverse 
Exemple si l'utilisateur saisi le mot python le programme lui revoie nohtyp'''
mot=input("entrer le mot : ")
print(mot)
n=len(mot)
L=[]
for i in range(0,n):
    L.append(mot[-i-1])
mot_inverse="".join(L) # A ce niveau on transforme la liste en une chaine des ceracteres
print("la lecture inverse de ",mot, " est ",mot_inverse)