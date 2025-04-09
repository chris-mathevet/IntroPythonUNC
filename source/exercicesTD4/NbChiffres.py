entrees_visibles = [
        (1234),
        (0),
]

entrees_invisibles = [
        (12340000),
        (8),
        (12),
        (123),
        (1234987654321),
]


@solution
def nbChiffres(nombre):
    cpt=0
    decomp=nombre
    while decomp!=0:
        decomp=decomp//10
        cpt+=1
    if cpt==0: #cas de 0
        cpt=1
    return cpt
