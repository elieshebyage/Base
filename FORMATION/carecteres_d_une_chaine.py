'''Ecrire un programme python qui permet de parcourir et afficher les caracteres d'une variable 
type chaine de caracteres'''
''' Exemple pour s=<< Python >>, le programme affiche les caracters 
P
y
t
h
o
n '''

texte=input("entrer un texte : ")
n=len(texte)
for i in range(0,n) :
    print(texte[i])