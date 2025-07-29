''' 2) Amaeliorez le programme afin qu'il affiche les tables de multiplications 
de tous les nombre complris entre 1 et 9'''
for n in range(1,10):
    print("---la table de multiplication de ",n,"---")
    for i in range(1,10):
        mult=i*n
        print(i,"x",n," = ",mult)