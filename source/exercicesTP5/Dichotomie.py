entrees_visibles = [
        ([1,2,3,4,5,6,7,8,9],7),
        ([1,2,3,4,4,6,7,8,9],4),
        ([1,2,3,4,5,6,7,8],10),
]

entrees_invisibles = [
        (list(range(100)),70),
        (list(range(0,100,2)),18),
        (list(range(0,100,2)),19),
		([],8)
]


@solution
def  rechercheDicho(liste,val):
  trouve=False
  i=0
  cpt=0
  j=len(liste)-1
  while i<j and not trouve:
    milieu=(i+j)//2
    x=liste[milieu]
    cpt+=1
    if x==val:
      trouve=True
    elif x<val:
      i=milieu+1
    else:
      j=milieu-1
  if trouve:
    return (milieu,cpt)
  return (None,cpt)
