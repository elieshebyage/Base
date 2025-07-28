def recuperer_et_afficher_infos_personne(numero_personne):
    nom=input("nom de la personne " + str(numero_personne)+" : ")
    age=input("age de la personne " + str(numero_personne)+" : ")
    print("la personne",numero_personne,"est",nom,"son age est",age,"ans")
    print("le nom possede",len(nom),"lettres")
recuperer_et_afficher_infos_personne(1)
recuperer_et_afficher_infos_personne(2)
recuperer_et_afficher_infos_personne(3)