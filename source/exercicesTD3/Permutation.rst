Exercice 4.2 : Permutation
--------------------------

Une permutation permet de "mélanger" une liste d'éléments en suivant une certaine loi. Pour un ensemble à *n* éléments, toute liste de taille *n* qui contient tous les entiers de 0 à *n*-1 est une permutation. On voudrait, à partir d'une *liste* et d'une *permutation* de mêmes tailles, construire une liste mélangée suivant la permutation. 

Par exemple, le mélange de la liste ``[12,18,23,8]`` avec la permutation ``[3,2,0,1]`` doit donner ``[23,8,18,12]`` (12 va à la position 3, 18 à la position 2, 23 à la position 0 et 8 à la position 1).

Ecrire une fonction ``permutationListe`` qui construit ce résultat à partir d'une *liste* et d'une *permutation* passées en paramètres.


.. easypython:: /exercicesTD3/Permutation.py
   :language: python
   :uuid: 1231313