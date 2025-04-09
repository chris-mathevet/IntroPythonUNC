entrees_visibles = [
	([0,1,3,7,15,31],2,1),
	([2,5,11,23,47],2,1),
	([0,1,3,7,15,31],1,2),
	([10],1,2),
	([],1,2),
]
entrees_invisibles = [
	([0,1,3,7,15,30],2,1),
	([13,27,55,111,223,447],2,1),
	([13,27,55,111,223,448],2,1),
	([0,0,0,0,0,0,0],0,0),
	([0],2,1),
]

@solution
def verifSuiteAriGeo(liste,a,b):
  ok=True
  n=1
  while n<len(liste) and ok:
    if liste[n]!=liste[n-1]*a+b:
      ok=False
    n+=1
  return ok
