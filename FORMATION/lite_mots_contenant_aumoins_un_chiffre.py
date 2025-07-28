# Liste des mots contenant au moins un chiffre dans un texte qui sera donné
T=input("T= ")
def digitInWord(mot):
    counter=0
    for x in mot :
        if x.isdigit() :
            counter=counter + 1
    if counter==0 :
        return False
    else:
        return True
    
def digitInText(T) :
    Liste_aumoins_un_chiffre=[]
    #convertir le texte T en liste
    L=T.split()
    for word in L :
        if digitInWord(word) :
            Liste_aumoins_un_chiffre.append(word)
    return Liste_aumoins_un_chiffre
print("la liste de mots contenant au moins un chiffre est : ",digitInText(T))