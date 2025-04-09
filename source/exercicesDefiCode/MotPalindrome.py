entrees_visibles = [
	("radar"),
	(""),
	("python"),
]
entrees_invisibles = [
	("anna"),
	("abcdefghhgfedcba"),
	("abcdefghhgfedcbb"),
	("abcdefghigfedcba"),
]

@solution
def motPalindrome(mot):
  ok=True
  i=0
  while i<len(mot)//2 and ok:
    if mot[i]!=mot[-1-i]:
      ok=False
    i+=1
  return ok
