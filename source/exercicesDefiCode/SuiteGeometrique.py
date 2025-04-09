entrees_visibles = [
	([]),
	([1]),
	([0,1]),
	([1,2,3]),
	([1,3,9,27,81]),
]
entrees_invisibles = [
	([1,10,100,1000,10000]),
	([-1,-10,-100,-1000,-10000]),
	([0]),
	([0,0,0,0,0,0,0,0,0]),
	([0,0,0,0,0,0,0,0,1]),
	([1,0,0,0,0,0,0,0]),
	([2,4,6,8,10]),
]

@solution
def suiteGeo(liste):
  res=True
  if len(liste)>1:
    if liste[0]==0:
      q=0
    else:
      q=liste[1]/liste[0]
    res=verifSuiteAriGeo(liste,q,0)
  return res

def verifSuiteAriGeo(liste,a,b):
  ok=True
  n=1
  while n<len(liste) and ok:
    if liste[n]!=liste[n-1]*a+b:
      ok=False
    n+=1
  return ok
