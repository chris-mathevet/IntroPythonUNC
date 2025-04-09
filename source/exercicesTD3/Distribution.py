entrees_visibles = [
        ([1,0,1,3,3,1,1],3),
]
entrees_invisibles = [
		([0,0,1,1,2,3,4,2,3,5,6,7,7,7,7,7,8,1,0],8),
]

@solution
def distribution(liste,n):
    res=[0]*(n+1)
    for x in liste:
        if 0<=x<=n:
            res[x]+=1
    return res