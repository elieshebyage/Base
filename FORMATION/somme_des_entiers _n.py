# Ecrire un programme en python qui demende à l'utlisateur de saisir un nombre entier n 
# et de lui afficher la valeur de la somme 1+2+3+...+n=
n=int(input("entrer un entier n : "))
somme=0
for i in range(1,n+1) :
    somme=somme+i
print("la valeur de la somme 1+2+3+...+n = " , somme)