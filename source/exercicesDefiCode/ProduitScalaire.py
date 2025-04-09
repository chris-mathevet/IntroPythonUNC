entrees_visibles = [
	([2,1,0,-1],[0,3,-2,1]),
	([],[]),
]
entrees_invisibles = [
	([12,11,10,-11],[10,13,-12,11]),
	([12,11,10,-11,12,11,10,-11,12,11,10,-11,12,11,10,-11],[10,13,-12,11,10,13,-12,11,10,13,-12,11,10,13,-12,11]),	
]

@solution
def produitScalaire(vec1,vec2):
  res=0
  for i in range(len(vec1)):
    res+=vec1[i]*vec2[i]
  return res
