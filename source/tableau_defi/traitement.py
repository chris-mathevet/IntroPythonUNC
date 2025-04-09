def chargerResultats(nomFic,listeExercices):
	"""Parcour du fichier des resultats synthetiques de l'exerciseur"""
	fic=open(nomFic,'r')
	resultats=dict()
	for ligne in fic:
		decomp=ligne.split(';')
		for i in range(len(decomp)):
			decomp[i]=decomp[i][1:-1]
		if decomp[6] in listeExercices:
			if decomp[0] not in resultats.keys():
				resultats[decomp[0]]=dict()
			resultats[decomp[0]][decomp[6]]=decomp[3]
	fic.close()
	return resultats

res=chargerResultats('/Users/cleuziou/donnees/enseignement/UNC/IntroPython/easySphinx/tableau_defi/tentatives_csv.csv',["doubleLettre","polynome"])
print(res)
