''' Ecrire un algorithme en python sous forme d'une fonction qui determine la longueur d'une 
chaine sans utliser la methode len() ni aucune methode predefinie en python'''
chaine=input("entrer une chaine des caracteres : ")
def longueur_lis(chaine) :
    longueur=0
    for i in chaine :
        longueur= longueur+1
    return longueur
print("la longueur de la chaine est ", longueur_lis(chaine) )