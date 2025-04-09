entrees_visibles = [
        (2009),
        (2020),
]

entrees_invisibles = [
		(2),
		(22),
		(12),
		(122),
		(123),
		(123456789987654321),
]


@solution
def doubleChiffre(nombre):
    trouve=False
    prec=nombre%10
    reste=nombre//10
    while reste>0 and not trouve:
        if prec==reste%10:
            trouve=True
        else:
            prec=reste%10
            reste=reste//10
    return trouve
