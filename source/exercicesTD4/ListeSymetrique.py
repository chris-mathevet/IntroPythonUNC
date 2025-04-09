entrees_visibles = [
        ([1,2,3,2,1]),
        ([1,2,3,1]),
        ([]),
]

entrees_invisibles = [
        ([8,1,4,198,7,-65,90,-2,90,-65,7,198,4,1,8]),
        ([8,1,4,198,7,-65,90,-2,-2,90,-65,7,198,4,1,8]),
        ([8,3,-2,1,8]),
        ([8,3,-2,-2,1,8]),
]


@solution
def listeSymetrique(l):
    res=True
    i=0
    while i<len(l)//2 and res:
        if l[i]!=l[-(i+1)]:
            res=False
        i+=1
    return res
