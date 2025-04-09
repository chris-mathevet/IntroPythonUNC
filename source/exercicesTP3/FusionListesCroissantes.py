entrees_visibles = [
		([1,3,5,9],[2,4,6]),
		([1,3,5,9],[]),
		([3,3,5,15],[2,4,6]),
		([-1,3,5,9],[12,13,14]),
]

entrees_invisibles = [
		([],[]),
		([],[1]),
		([1],[]),
		([0,0,0],[0,0,0]),
		([10,11,12],[1,2,3,7,8,9]),
		(list(range(0,1000,2)),list(range(1,10020,2))),
		([-5,-3,-1],[-2,0,10,15]),
]

@solution
def fusion(liste1,liste2):
    res=[]
    i1=0
    i2=0
    while i1<len(liste1) and i2<len(liste2) :
        if liste1[i1]<liste2[i2]:
            res+=[liste1[i1]]
            i1+=1
        else: # liste1[i]>=liste2[i]
            res+=[liste2[i2]]
            i2+=1
    while i1<len(liste1):
        res+=[liste1[i1]]
        i1+=1
    while i2<len(liste2):
        res+=[liste2[i2]]
        i2+=1
    return res
