''' 1) Ecrire un programme en python qui demande à l'utilisateur de saisir un nombre entier n 
et de lui afficher la table de multiplication de ce nombre'''
n=int(input(" enter un nombre entier n : "))
for i in range(1,10) :
    mult=i*n
    print(i,"x",n," = ",mult)