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
def stockerChiffres(nombre):
    res=[]
    decomp=nombre
    while decomp!=0:
        res+=[decomp%10]
        decomp=decomp//10
    if res==[]: #cas de 0
        res=[0]
    return res
