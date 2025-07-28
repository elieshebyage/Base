# Ecrire un programme calculant la somme des nombres pairs de 0 à 100 et des nombres impairs de 0 à 101
nb_pair=0
nb_impair=0
for i in range(0,101) :
    if i%2==0 : 
        nb_pair=nb_pair+i
for i in range(1,102) :
    print(i)
    if i%2!=0 : 
        nb_impair=nb_impair+i
print("la somme des nombres pairs de 0 à 100 est ", nb_pair)
print("la somme des nombres impairs de 0 à 101 est ", nb_impair)