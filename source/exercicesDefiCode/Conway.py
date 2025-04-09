entrees_visibles = [
	('1'),
	('11'),
	('21'),
	('1211'),
	('1113213211'),
]
entrees_invisibles = [
	('111221'),
	('312211'),
	('13112221'),
	('31131211131221'),
	('13211311123113112211'),
]

@solution
def nextConway(s):
  res=''
  prec=None
  cpt=0
  for c in s:
    if c==prec:
      cpt+=1
    else:
      if prec:
        res+=str(cpt)+str(prec)
      cpt=1
    prec=c
  if prec:
    res+=str(cpt)+str(prec)
  return res
