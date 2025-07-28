# Exercice fonctions : Table de multiplication
def afficher_table_multiplication(n):
    min=1
    max=10
    for i in range(min,max+1):
        print(i,"x",n,"=",i*n)
afficher_table_multiplication(5)