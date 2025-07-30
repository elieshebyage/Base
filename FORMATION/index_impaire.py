''' Ecrire un programme python qui remplace les caracteres d'index impaires d'une chaine 
 s par # '''
s=input("entrer la chaine de caractere : ")
n=len(s)
s2=""
for i in range(0,n) :
    if i%2==0 :
        s2= s2 + s[i]
    else :
        s2= s2 + "#"
print(s2)