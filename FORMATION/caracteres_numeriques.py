''' Ecrire un programme en python sous forme de fonction qui prend en parametre une chaine s
et qui renvoie la liste des caracteres numeriques contenus dans la chaine s'''
s=input("entrer la chaine : ")
def  caractere_numeruque(s) :
    liste=[]
    for i in s :
        if i.isnumeric() :
            liste.append(i)
    return liste
print(caractere_numeruque(s))