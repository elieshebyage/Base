# Ecrrire un programme python qui demande à l'utilisateur de saisir un nombre entier n
#  et de lui afficer n!
n=int(input("entrer un nombre entier n : "))
facto=1
for i in range(1,n+1):
    facto=facto*i
print(" le factoriel  de", n , "est", facto)