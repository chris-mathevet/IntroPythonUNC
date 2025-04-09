entrees_visibles = [
        28,
		5,
		21,
		16,
		17
]
entrees_invisibles = list(range(-1,26))

@solution
def jourNuit(heure):
    """ Cette fonction renvoie une chaîne décrivant le moment de la journée en fonction de l'heure passée en paramètre"""
    if heure>=0 and heure<=24:
        res=""
        #on identifie la période de la journée : matin, après-midi, soirée, nuit
        if heure<5 or heure>=21:
            res="on est la nuit"
        elif heure<12:
            res="on est le matin"
        elif heure<17:
            res="on est l'après-midi"
        else:
            res="on est le soir"
        #on identifie s'il fait jour ou nuit
        if heure<6 or heure>=18:
            res=res+" et il fait nuit"
        else:
            res=res+" et il fait jour"
    else:
        res="l'heure saisie est invalide"
    return res
