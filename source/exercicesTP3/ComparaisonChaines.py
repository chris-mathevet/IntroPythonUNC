entrees_visibles = [
        ('nouvelle','caledonie'),
        ('caledonie','nouvelle'),
        ('caledonie','caledonien'),
        ('bonjour','bonjour'),
		('','bonjour'),
]

entrees_invisibles = [
        ('new','york'),
        ('york','new'),
        ('news','new'),
        ('new','new'),
		('',''),
		('new',''),
]

@solution
def compare(chaine1,chaine2):
    res=0
    i=0
    while i<len(chaine1) and i<len(chaine2) and res==0:
        if chaine1[i]<chaine2[i]:
            res=-1
        elif chaine1[i]>chaine2[i]:
            res=1
        i+=1
       #on gère le cas des chaînes de tailles différentes
    if res==0 :
        if i<len(chaine1):
            res=1
        elif i<len(chaine2):
            res=-1
    return res
