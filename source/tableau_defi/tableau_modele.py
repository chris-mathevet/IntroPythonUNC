# imagier_modele_1_facile.py
# Version 1 du modèle

nomFic='/Users/cleuziou/donnees/enseignement/UNC/IntroPython/easySphinx/source/tableau_defi/tentatives_csv.csv'
exercices=["produitScalaire","motPalindrome","compteChiffre","phrasePalindrome","sousChaine","elemAri","elemGeo","verifSuiteAriGeo","suiteAri","suiteGeo","suiteAriGeo","nextConway"]
idExercices=["0787173acdaeb235af8b8904fce81952","4c4b7a924be986e72228374530812bf0","e2e71241db6a4971b7f407789330fdfd","908defc05cefcce7d5707781c7f9e500","3588d5b2366ad1ff5f1d78b184175afa","a7cdd094daa2f0bfccc7a4ec419f7243","f239498950e974e29e01472749d9a09d","d7c83a7fb9b49e28804e55955ad06968","415838ff0b81e52cfa661e514d52f26e","24fcf43c6eaccdd09abf09cc65703741","1bf7c612843eda9ce08f308b85561049","4c9665daf155b115fe13218141fa1aff","a580c32690609356dae4401b3c89a3b8"]
enseignants=['guillaume.cleuziou']

def chargerResultats(nomFic,listeExercices,idExercices):
	"""Parcour du fichier des resultats synthetiques de l'exerciseur"""
	fic=open(nomFic,'r')
	resultats=dict()
	for ligne in fic:
		decomp=ligne.split(';')
		for i in range(len(decomp)):
			decomp[i]=decomp[i][1:-1]
		if decomp[6] in listeExercices and decomp[1] in idExercices and decomp[0] not in enseignants:
			name=decomp[0].split('.')
			decomp[0]=''
			for elem in name:
				decomp[0]+=elem[0].upper()+elem[1:]+' '
			if decomp[0] not in resultats.keys():
				resultats[decomp[0]]=dict()
			if decomp[6] in resultats[decomp[0]].keys() and decomp[3]=='non':
				pass
			else :
				resultats[decomp[0]][decomp[6]]=decomp[3]
	fic.close()
	return resultats

resultats=chargerResultats(nomFic,exercices,idExercices)


# ===========
# Traitements sur les données
# ===========

def toutReussi(resultat,exercices):
	"""renvoie True si resultat contient tous les exercices avec des 'oui' partout"""
	if len(resultat)<len(exercices):
		return False
	for exo in resultat.keys():
		if resultat[exo]!='oui':
			return False
	return True

def best(resultats,exercices):
	"""renvoie le sous-dictionnaire des étudiants ayant tout réussi et les enlève de resultats"""
	best=dict()
	others=dict()
	for etud in resultats.keys():
		if toutReussi(resultats[etud],exercices):
			best[etud]=resultats[etud]
		else:
			others[etud]=resultats[etud]
	return best,others

resultats_best,resultats_others=best(resultats,exercices)
