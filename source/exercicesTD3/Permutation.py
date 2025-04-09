entrees_visibles = [
        ([12,18,23,8],[3,2,0,1]),
        ([12,18,23,8],[0,1,2,3]),        
]
entrees_invisibles = [
		(list(range(0,200,2)),list(reversed(range(100)))),
]

@solution
def permutationListe(liste,permutation):
    res=[0]*len(liste)
    for i in range(len(liste)):
        res[permutation[i]]=liste[i]
    return res