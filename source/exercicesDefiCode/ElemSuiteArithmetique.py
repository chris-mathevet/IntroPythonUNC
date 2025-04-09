entrees_visibles = [
	(2,1,2),
	(0,1,2),
	(3,0,-2),
]
entrees_invisibles = [
	(50,13,7),
	(5,-145,2),
	(0,10,-2),
]

@solution
def elemAri(n,u0,r):
  return u0+n*r
