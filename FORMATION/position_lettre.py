''' Ecrire un programme en python qui demende à l'utilisateur de saisir une chaine une chaine de caractere s 
et de lui renvoyer un message indiquant si la chaine contient la lettre a tout en indiquant 
sa position sur la chaine . EXEMPLE si l'utilisateur tape la chaine s="langage" le programme lui renvoie :
La lettre 'a' se trouve à la position: 1 
La lettre 'a' se trouve à la position: 4 '''
s=input("entrer une chaine de caractere : ")
lettre=input("La lettre : ")
n=len(s)
for i in range(0,n) :
    if s[i]==lettre:
        print("la lettre '",lettre,"' se trouve à la position : ",i)

    