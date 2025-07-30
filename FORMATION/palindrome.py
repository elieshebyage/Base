''' Un palindrome un mot dont l'ordre des lettres reste le meme si on le lit de gauche à droite
ou de droite à gauche. Ecrire un programme en python qui demande à l'utilisateur de saisir 
un mot et de lui renvoyer s'il s'agit d'un palindrome ou nom '''
mot=input("entrer le mot : ")
print(mot)
n=len(mot)
L=[]
for i in range(0,n):
    L.append(mot[-i-1])
mot_inverse="".join(L) # A ce niveau on transforme la liste en une chaine des ceracteres
if mot_inverse==mot :
    print("le mot",mot, "est un palindrome")
else :
    print("le mot",mot, "n'est pas un palindrome")
