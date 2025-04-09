entrees_visibles = [
        ('M',11.0,5,False),
		('M',11.0,2,False),
		('M',11.0,2,True),
		('F',14.0,5,False)
]
entrees_invisibles = [
		('M',11.0,2,True),('M',11.0,3,True),('M',11.0,4,True),
		('M',12.0,2,True),('M',12.0,3,True),('M',12.0,4,True),
		('M',13.0,2,True),('M',13.0,3,True),('M',13.0,4,True),
		('M',15.0,2,True),('M',15.0,3,True),('M',15.0,4,True),
		('M',16.0,2,True),('M',16.0,3,True),('M',16.0,4,True),
		('F',11.0,2,True),('F',11.0,3,True),('F',11.0,4,True),
		('F',12.0,2,True),('F',12.0,3,True),('F',12.0,4,True),
		('F',13.0,2,True),('F',13.0,3,True),('F',13.0,4,True),
		('F',15.0,2,True),('F',15.0,3,True),('F',15.0,4,True),
		('F',16.0,2,True),('F',16.0,3,True),('F',16.0,4,True),
		('M',11.0,2,False),('M',11.0,3,False),('M',11.0,4,False),
		('M',12.0,2,False),('M',12.0,3,False),('M',12.0,4,False),
		('M',13.0,2,False),('M',13.0,3,False),('M',13.0,4,False),
		('M',15.0,2,False),('M',15.0,3,False),('M',15.0,4,False),
		('M',16.0,2,False),('M',16.0,3,False),('M',16.0,4,False),
		('F',11.0,2,False),('F',11.0,3,False),('F',11.0,4,False),
		('F',12.0,2,False),('F',12.0,3,False),('F',12.0,4,False),
		('F',13.0,2,False),('F',13.0,3,False),('F',13.0,4,False),
		('F',15.0,2,False),('F',15.0,3,False),('F',15.0,4,False),
		('F',16.0,2,False),('F',16.0,3,False),('F',16.0,4,False)
]

@solution
def qualifJO(sexe,record,nbvictoires,champion):
    res=False
    if sexe=='M' and (record<12 and nbvictoires>=3 or champion):
            res=True
    elif sexe=='F' and (record<15 and nbvictoires>=3 or champion):
            res=True
    return res
