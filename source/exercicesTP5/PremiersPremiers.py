entrees_visibles = [
        (1),
        (2),
        (5),
]

entrees_invisibles = [
        (0),
		(100),
]


@solution
def nombresPremiers(n):
  res=[]
  x=2
  while len(res)<n:
    ok=True
    i=0
    while i<len(res) and ok:
      if x%res[i]==0:
        ok=False
      i+=1
    if ok:
      res.append(x)
    x+=1
  return res
