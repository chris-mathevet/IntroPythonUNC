entrees_visibles = [
        ("tableau"),
		("phrase"),
        ("schwimmen"),
		(""),
]

entrees_invisibles = [
		(""),
		("bcdanuio"),#prononçable malgré un plateau de 3 consonnes et un autre de trois voyelles
		("abcvfejklaeo"), #imprononcable car un plateau de 4 consonnes même si les autres plateaux qui suivent sont de taille <4
		("daeioruyafgh"), #imprononcable car un plateau de 4 voyelles même si les autres plateaux qui suivent sont de taille <4
		("aei"),
		("fgh"),
		("a"),
		("f")
]

@solution
def prononcable(mot):
   res=True
   cons=True #True si la lettre précédente était une consonne
   cpt=0
   for lettre in mot:
      if lettre in 'aeiouy':
         if cons:
            cons=False
            cpt=1
         else:
            cpt=cpt+1
      else:#il s'agit d'une consonne
         if (not cons):
            cons=True
            cpt=1
         else:
            cpt=cpt+1
      if cpt>3:
         res=False
   return res
