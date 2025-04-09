entrees_visibles = [
        (['Batman', 'Robin', 'Batman', 'Jocker', 'Batman'],'Batman'),
        (['Batman', 'Robin', 'Batman', 'Jocker', 'Batman'],'Robin'),
        (['Batman', 'Robin', 'Batman', 'Jocker', 'Batman'],'Toto'),
]

entrees_invisibles = [
        (['a','b','c','a','b','b','a','a','c','d'],'a'),
        (['a','b','c','a','b','b','a','a','c','d'],'b'),
        (['a','b','c','a','b','b','a','a','c','d'],'d'),
		([],'r'),
]


@solution
def nbOccurrencesJoueur(joueurs,nom):#exo5
    """renvoie le nombre de fois que le joueur 'nom' apparaît dans la liste 'joueurs'"""
    res=0
    for j in joueurs:
        if j==nom:
            res=res+1
    return res
