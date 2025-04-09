entrees_visibles = [
        (300000,[352100, 325410, 312785, 220199, 127853]),
        (360000,[352100, 325410, 312785, 220199, 127853]),
        (120000,[352100, 325410, 312785, 220199, 127853]),
]

entrees_invisibles = [
        (100,[10,9,8,7,6,5,4,3,2,1]),
        (-12,[10,9,8,7,6,5,4,3,2,1]),
        (9.5,[10,9,8,7,6,5,4,3,2,1]),
		(1,[]),
]


@solution
def indiceInsertion(sc,scores):#exo8
    """renvoie l'indice ou devra être inséré sc dans scores (pour conserver le tri décroissant)"""
    trouve=False
    i=0
    while i<len(scores) and not trouve:
        if sc>scores[i]:
            trouve=True
        i+=1
    if trouve:
        res=i-1
    else:
        res=i
    return res
