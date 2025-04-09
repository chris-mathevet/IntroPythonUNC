entrees_visibles = [
        [1,102,360,14,201,8,471,365],
		[1,100,360,14],
		[],
]

entrees_invisibles = [
		[1,2,3,99,45,-12],
		[-1,-1,0,0,-1,-1],
        [10,13,360,14,2010,83,4711,45,365,548,-14],
		[10,100,360,14,453,27],
]

@solution
def quatrePlus100(liste):
    cpt=0
    i=0
    res=[]
    while i<len(liste) and cpt<4:
        if liste[i]>100:
            res.append(liste[i])
            cpt+=1
        i+=1
    return res
