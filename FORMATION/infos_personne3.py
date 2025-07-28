def afficher_infos_personne(numero_personne,nom,age):
 print("la personne",numero_personne,"est",nom,"son age est",age,"ans")
 print("le nom possede",len(nom),"lettres")

def recuperer_et_afficher_infos_personne(numero_personne):
    nom_personne=input("nom de la personne " + str(numero_personne)+" : ")
    age_personne=input("age de la personne " + str(numero_personne)+" : ")
    afficher_infos_personne(numero_personne,nom_personne,age_personne)
nombre_personnes=2
for i in range(nombre_personnes):
    recuperer_et_afficher_infos_personne(i+1)
afficher_infos_personne("007","James","40")