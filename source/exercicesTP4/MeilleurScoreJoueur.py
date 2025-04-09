entrees_visibles = [
        ([352100, 325410, 312785, 220199, 127853],['Batman', 'Robin', 'Batman', 'Jocker', 'Batman'],'Batman'),
        ([352100, 325410, 312785, 220199, 127853],['Batman', 'Robin', 'Batman', 'Jocker', 'Batman'],'Robin'),
        ([352100, 325410, 312785, 220199, 127853],['Batman', 'Robin', 'Batman', 'Jocker', 'Batman'],'Toto'),
]

entrees_invisibles = [
        ([10,9,8,7,6,5,4,3,2,1],['a','b','c','a','b','b','a','a','c','d'],'a'),
        ([10,9,8,7,6,5,4,3,2,1],['a','b','c','a','b','b','a','a','c','d'],'b'),
        ([10,9,8,7,6,5,4,3,2,1],['a','b','c','a','b','b','a','a','c','d'],'d'),
		([],[],'r'),
]


@solution
def meilleurScoreJoueur(scores,joueurs,nom):#exo3
    """renvoie le meilleur score du joueur 'nom' (0 si le joueur n'est pas dans la liste"""
    trouve=False
    i=0
    while i<len(joueurs) and not trouve:
        if joueurs[i]==nom:
            trouve=True
        i+=1
    if trouve:
        res=scores[i-1]
    else:
        res=0
    return res
