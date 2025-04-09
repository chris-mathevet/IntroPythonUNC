entrees_visibles = [
	(3,13038),
	(2,13038),
	(0,0),
]
entrees_invisibles = [
	(9,13429567181929093870),
	(7,134295618192909380),
]

@solution
def compteChiffre(chiffre,nombre):
  cpt=0
  if nombre==0 and cpt==0:
    cpt=1
  while nombre>0:
    if nombre%10==chiffre:
      cpt+=1
    nombre=nombre//10
  return cpt
