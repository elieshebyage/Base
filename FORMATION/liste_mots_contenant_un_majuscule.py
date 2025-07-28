# la liste de mots contenant au moins un majuscule
T=input("T= ")
def majInWord(mot):
    counter=0
    for x in mot :
        if x.isupper() :
            counter=counter + 1
    if counter<2 :
        return False
    else:
        return True
def list2Maj(T) :
    Liste_aumoins_2Maj=[]
    #convertir le texte T en liste
    L=T.split()
    for word in L :
        if majInWord(word) :
            Liste_aumoins_2Maj.append(word)
    return Liste_aumoins_2Maj
print("la liste de mots contenant au moins un chiffre est : ", list2Maj(T))