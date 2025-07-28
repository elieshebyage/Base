# Ecrire un programme en python qui determine la liste des motsne contenant pas la lettre "a"dans un texte qui sera donné
#T="python est un langage de haut niveau"
T=input ("T= ")
def motSans_a(T):
    liste_motSans_a=[]
    # convertir le texte T en liste 
    L=T.split()
    for mot in L :
        if "a" not in mot :
            liste_motSans_a.append(mot)
    return liste_motSans_a
print("la liste de mots sans a est :",motSans_a(T) )