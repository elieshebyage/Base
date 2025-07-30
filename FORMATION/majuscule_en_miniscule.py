'''Ecrire un programme python sous forme de fonction qui prend comme parametre une chaine s
 et qui retourne une chaine obtenue à partir de la chaine s en transformant chaque caractere majuscule 
 en caractere miniscule et vice versa sans utiliser la methode swapcase()'''
s=input("entrer la chaine : ")
def miniscule_majuscule(s) :
    swap_s=""
    for i in s :
        if i.isupper() :
            i=i.lower()
            swap_s= swap_s + i
        elif i.islower() :
            i=i.upper()
            swap_s= swap_s + i
        else :
            swap_s= swap_s + i
    return swap_s
print(" la transformation majuscule miniscule et vis vesa est : ",miniscule_majuscule(s))