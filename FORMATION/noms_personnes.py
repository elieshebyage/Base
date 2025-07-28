# sort permet de trier la liste par ordre alphabetique. Toute fois, le majuscule vient avant le minisciule
noms=[]
nom=input("Entrez votre nom : ")
while nom!="":
    noms.append(nom)
    nom=input("Entrez votre nom : ")
noms.sort()
print(noms)