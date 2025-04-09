entrees_visibles = [
        (['AS Magenta','AS Mont-Dore','Hienghène Sports']),
        (['AS Magenta','AS Mont-Dore']),
        (['AS Magenta']),
		([]),
]

entrees_invisibles = [
        (list(range(10))),
]


@solution
def listeMatchs(liste):
  res=[]
  for i in range(len(liste)-1):
    for j in range(i+1,len(liste)):
      res.append((liste[i],liste[j]))
  return res
