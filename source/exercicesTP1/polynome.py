import math

entrees_visibles = [
        (1,-1,0),
        (2,-4,2),
        (3,-2,10)
]
entrees_invisibles = [
        (1,-1,0),
        (2,-4,2),
        (3,-2,10)
]

@solution
def polynome(a,b,c):
   delta=b**2-4*a*c
   if delta<0:
       res='pas de solution'
   elif delta==0:
       res=-b/(2*a)
   else:
       res=((-b+math.sqrt(delta))/(2*a)),((-b-math.sqrt(delta))/(2*a))
   return res
