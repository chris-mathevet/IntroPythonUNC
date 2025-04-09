entrees_visibles = [
	("program","J'aime la programmation"),
	("programme","J'aime la programmation"),
	("","bonjour"),
]
entrees_invisibles = [
	("Jaime","la vie est belle"),
	("elle","la vie est belle"),
	("elle","la viell est belle"),
	("la vie","la vie est belle"),
	("belles","la vie est belle"),
	("telle","la vie est belle"),
	("la c","la vie est belle"),
	("ala vie","la vie est belle"),
]

@solution
def sousChaine(s1,s2):
  i=0
  j=0
  while i<len(s2) and j<len(s1):
    if s1[j]==s2[i]:
      j+=1
    elif j>0:
      i-=1
      j=0
    i+=1
  return j==len(s1)
