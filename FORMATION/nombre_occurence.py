# on va determiner le nombre des fois un element d'une liste est repeter sans utiliser la fontion count()
elements=input("Donner les elements de la liste : ")
x=input("entrer l'element : ")
X=[]
def nombre_occurences(x) :
    L=elements.split() # la variable elements est converti en une liste d'elements
    for i in L :
        if i==x :
            X.append(i)
    print("le nombre d'occurence de",x,"est : ", len(X))
nombre_occurences(x)