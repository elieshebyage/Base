'''Ecrire un programme qui demande à l'utilisateur de saisir un texte 
et de lui renvoyer tous les commencant par a'''
texte=input("entrer le texte : ")
T=texte.split()
N=len(T)
for I in range(0,N) :
    mot=T[I]
    if  mot[0]=="a":
        print("le mot",mot,"commence par 'a' ")