entrees_visibles = [
	('coucou'),
	('creee'),
]
entrees_invisibles = [
	(''),
	('aa'),
	('abab'),
	('abaabab'),
]

@solution
def doubleLettre(mot):
   res=False
   prec=None
   for c in mot:
      if c==prec:
         res=True
      prec=c
   return res
