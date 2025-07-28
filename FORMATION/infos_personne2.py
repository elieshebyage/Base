def recuperer_et_afficher_infos_personne(numero_personne):
    nom=input("nom de la personne " + str(numero_personne)+" : ")
    age=input("age de la personne " + str(numero_personne)+" : ")
    print("la personne",numero_personne,"est",nom,"son age est",age,"ans")
    print("le nom possede",len(nom),"lettres")
nombre_personnes=2
for i in range(nombre_personnes):
    recuperer_et_afficher_infos_personne(i+1)
