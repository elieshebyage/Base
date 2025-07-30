''' Ecrire un programme python sous forme de fonction qui prend en parametre 
une chaine S et qui retourne  la liste de tous les mots contenus dans la s dont la longueur
est superieur ou egal à 7'''
s=input("entrer une chaine : ")
liste=s.split()
def chaine_de_longueur(s) :
    L=[]
    for i in liste :
        if len(i)>=7 :
            L.append(i)
    return L
print("les mots de longueur superieur ou egal à 7 sont : ",chaine_de_longueur(s))