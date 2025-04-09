entrees_visibles = [
        ('bonjour'),
        ('doremi'),
        (''),
]
entrees_invisibles = [
		("cet exercice n'est pas très difficile"),
]

@solution
def permutationChaine(s):
    res=''
    for i in range(0,len(s)-1,2):
        res=res+s[i+1]+s[i]
    #on traite le (dernier) caractère restant dans le cas
    #d'une chaîne de taille impaire
    if(len(s)%2!=0): # ou encore if len(res)!=len(s)
        res=res+s[-1]
    return res