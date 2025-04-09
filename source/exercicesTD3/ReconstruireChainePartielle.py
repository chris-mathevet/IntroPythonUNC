
entrees_visibles = [
        ('bonjour',2),
        ('bonjour',3),
        ('b',4),
        ('',2)
]
entrees_invisibles = [
		("cet exercice n'est pas très difficile",3),
]

@solution
def reconstruireChainePartielle(s,n):
	res=''
	for i in range(0,len(s),n):
		res=res+s[i]
	return res
