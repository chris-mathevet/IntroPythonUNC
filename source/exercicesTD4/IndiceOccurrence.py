entrees_visibles = [
        (3, 12, [12,3,4,12,8,12,5,12]),
        (2, 8, [12,3,4,12,8,12,5,12]),
        (1, 12, []),
]

entrees_invisibles = [
        (4, 12, [12,3,4,12,8,12,5,12]),
        (1, 12, [12,3,4,12,8,12,5,12]),
        (4, 7, [12,3,4,12,8,12,5,12]),
        (-3, 12, [12,3,4,12,8,12,5,12]),
]


@solution
def indiceOccurrence(n, x, l):
    """nième occurrence de x dans la liste l"""
    cpt = 0
    i = 0
    while i < len(l) and cpt < n:
        if l[i] == x:
            cpt += 1
        i += 1
    if cpt == n:
        res = i-1
    else:
        res = None
    return res
