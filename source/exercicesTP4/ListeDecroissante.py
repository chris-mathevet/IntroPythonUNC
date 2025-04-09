entrees_visibles = [
        ([352100, 325410, 312785, 220199, 127853]),
        ([352100, 325410, 312785, 127853, 220199]),
        ([]),
]

entrees_invisibles = [
        ([0,2]),
        ([0]),
        ([-100,-50,0]),
        ([-100,-200,-300]),
]


@solution
def listeDecroissante(scores):#exo2
    """renvoie True si la liste est triée dans l'ordre décroissant (False sinon)"""
    ok=True
    i=0
    while i<len(scores)-1 and ok:
        if scores[i]<scores[i+1]:
            ok=False
        i+=1
    return ok
