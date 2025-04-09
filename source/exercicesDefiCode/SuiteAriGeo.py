entrees_visibles = [
	([]),
	([1]),
	([0,1]),
	([1,3,5,7,9,11]),
	([1,3,9,27,81]),
	([1,3,7,15,31,63]),
	([1,3,4,7,11]),
]
entrees_invisibles = [
	([0,0,0,0,0,0,0,0,0]),
	([10]),
	([-1]),
	([0,10]),
	([2,6,14,30,62,126]),
	([5,13,37,109,325]),
	([0,1,3,7,15,31,64]),
	([5,13,37,110,325]),
]

@solution
def suiteAriGeo(liste):
  res=True
  if len(liste)>2:
    if (liste[1]-liste[0])==0:
      q=0
      r=0
    else:
    	q=(liste[2]-liste[1])/(liste[1]-liste[0])
    	r=liste[1]-q*liste[0]
    res=verifSuiteAriGeo(liste,q,r)
  return res

def verifSuiteAriGeo(liste,a,b):
  ok=True
  n=1
  while n<len(liste) and ok:
    if liste[n]!=liste[n-1]*a+b:
      ok=False
    n+=1
  return ok
