entrees_visibles = [
        ('bonjour',2,3),
        ('bonjour',7,4),
        ('bonjour',2,7),
        ('',1,2)
]
entrees_invisibles = [
		("cet exercice n'est pas très difficile",3,5),
		("cet exercice n'est pas très difficile",3,20),
		("cet exercice n'est pas très difficile",40,5),
		("cet exercice n'est pas très difficile",20,50),
]

@solution
def sousChaine(s,debut,longueur):
    res=''   
    for i in range(debut,min(debut+longueur,len(s))):
        res=res+s[i]
    return res