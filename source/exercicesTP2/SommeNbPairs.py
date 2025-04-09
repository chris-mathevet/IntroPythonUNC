entrees_visibles = [
        [12,13,6,5,7],
		[],
]

entrees_invisibles = [
		[13,15,-3,711],
		[1224,-728],
		list(range(0,1000))
]

@solution
def sommeNbPairs(liste):
   res=0
   for x in liste:
      if x%2==0:
         res+=x
   return res
