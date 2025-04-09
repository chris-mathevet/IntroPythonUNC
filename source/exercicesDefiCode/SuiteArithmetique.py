entrees_visibles = [
	([]),
	([0,1]),
	([0,2,3]),
	([1,3,5,7,9]),
]
entrees_invisibles = [
	([0,100,200,300,400,500,600,700]),
	([0,100,200,300,400,500,600,701]),
	([10,0,-10,-20,-30,-40,-50,-60]),
	([1,3,9,27]),
]

@solution
def suiteAri(liste):
  res=True
  if len(liste)>1:
    r=liste[1]-liste[0]
    res=verifSuiteAriGeo(liste,1,r)
  return res

def verifSuiteAriGeo(liste,a,b):
  ok=True
  n=1
  while n<len(liste) and ok:
    if liste[n]!=liste[n-1]*a+b:
      ok=False
    n+=1
  return ok
