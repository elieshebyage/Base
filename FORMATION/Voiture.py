a=input("Quelle action voulez-vous exécuter? (rouler / klaxonner): \n ")
while a!="rouler" and a!="klaxonner" :
    print("l'action choisie n'est pas disponible ! ")
    a=input("Quelle action voulez-vous exécuter? (rouler / klaxonner): \n ")
if a=="rouler":
    print("vroum vroum !")
elif a=="klaxonner" :
    print("bip bip !")

   