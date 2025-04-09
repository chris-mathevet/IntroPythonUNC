entrees_visibles = [
        ([6,6,3,4,2,2,2,4]),
		([6,6,3,4,2,1,2,4]),
		([]),
]

entrees_invisibles = [
		([6,6,6,3,3,3,3,4,2,1,1,1,2,4]),
		([6,5,6,3,2,3,1,4,2,1,8,1,-3,4]),
		([6,-3,-3,2]),
]


@solution
def plusLongueSuite(liste):
   max=0
   temp=1
   prec=None
   for x in liste:
      if x==prec:
         temp+=1
      else:
         if temp>max:
            max=temp
            temp=1
      prec=x
   if temp>max and len(liste)>0:
      max=temp
   return max
