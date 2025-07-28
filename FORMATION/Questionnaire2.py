# LES FONCTIONS : Projet Questionnaire et gerer les scores(+1 en cas de bonne reponse et inchangé en cas de mauvaise)
# score est la variable global du codenet non la variable locale de la fonction
def poser_question(question,r1,r2,r3,r4,choix_bonne_reponse):
    global score
    print("Quastion",question)
    print("(a)",r1)
    print("(b)",r2)
    print("(c)",r3)
    print("(d)",r4)
    reponse=input("votre reponse :" )
    if reponse==choix_bonne_reponse :
        print("bonne reponse")
        score+=1
    else :
        print("Mauvaise reponse")
score=0
poser_question("quelle_est_la_capitale_dela_france","Marseille","Nice","Paris","Nantes","c")
poser_question("Quelle_est_la_capitale_de_l'italie","Rome","Venise","Pise","florence","a")
print("score final:",score)