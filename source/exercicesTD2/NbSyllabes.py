entrees_visibles = [
	'tableau',
	'ecouteur',
	''
]

entrees_invisibles = [
	'chronologie',
	'analphabette',
	'dfgdhaeuiauyvbgftrs'
]

@solution
def nbSyllabes(mot):
   cons=False #True si la lettre précédente était une consonne
   if len(mot)==0:
      res=0
   else:
      if mot[0] in 'aeiouy':
         res=1
      else:
         res=0
      for lettre in mot:
         if lettre in 'aeiouy':
            if cons: #changement consonne puis voyelle
               res=res+1
               cons=False
         else:
            cons=True
   return res
