entrees_visibles = [
        (1,10,7,20),
        (1,7,10,20),
		(20,25,10,20)
]
entrees_invisibles = [
		(13,18,20,25),
		(13,18,15,25),
		(13,18,18,25),
		(13,18,14,16),
		(13,18,2,10),
		(13,18,10,15),
		(13,18,9,13)
]

@solution
def rendezVous(debut1,fin1,debut2,fin2):
   if fin1<debut2 or fin2<debut1:
	   res=False
   else:
	   res=True
   return res
