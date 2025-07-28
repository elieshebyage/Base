# on veux determiner le nombre des nombres divisibles par n dans une liste qui sera donnée
nombres=input("donner ces nombres: ")
liste_nombre_divisibles=[]
n=int(input("on cherche les nombres divisible par : "))
def nombreDivisibles(n) :
    Liste=nombres.split() # dans cette ligne, on converti nombres en une liste
    for x in Liste :
        X=int(x)
        if X%n==0 :
            liste_nombre_divisibles.append(x)
    return liste_nombre_divisibles
nombreDivisibles(n)
print("il ya dans la liste,",len(liste_nombre_divisibles),"nombre divisibles par", n)