entrees_visibles = [
	("engage le jeu que je le gagne"),
	(""),
	("python est genial"),
]
entrees_invisibles = [
	("an n a"),
	("a bc defghh gfe dc ba"),
	("abcd ef ghh gfedcb b"),
]

@solution
def phrasePalindrome(phrase):
  ok=True
  i=0
  j=len(phrase)-1
  while i<j and ok:
    if phrase[i]==' ':
      i+=1
    elif phrase[j]==' ':
      j-=1
    elif phrase[i]!=phrase[j]:
      ok=False
    else:
      i+=1
      j-=1
  return ok
