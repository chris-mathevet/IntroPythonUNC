entrees_visibles = [
        1,
		3,
		5,
		-2
]

entrees_invisibles = [
		0,
		10,
		124,
		-5
]

@solution
def sommeNPremiersEntiersPairs(n):
   res=0
   for x in range(1,n+1):
	   if x%2==0:
		   res+=x
   return res
