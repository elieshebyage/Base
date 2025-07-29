'''Ecrire un programme pytho qui demande à l'utilisateur de saisir un nombre entier n 
et lui demande de saisir tous les diviseur de ce nombre'''
n=int(input("entrer un nombre entier n : "))
for i in range (1,n+1) :
    if n%i==0 :
        print(i,"est un diviseur de", n)