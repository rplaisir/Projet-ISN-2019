#!/usr/bin/env python
# coding: utf-8

# # Quelques notions autour d'un exercice de maths

# ### I. Objectif : Milieu et parallélogramme.

# #### I.1. Déterminons les coordonées du milieu I d'un segment [AB]

# On récupère les coordonnées de A et B grace aux fonctions (built-in) **_input( )_** et **_float( )_**




xA = float(input('Abscisse de A ? '))
yA = float(input('Ordonnée de A ? '))


# Faire de même avec le point B !




xB = 0
yB = 0


# Utilisons la formule permettant de déterminer les coordonnées de I

# In[ ]:


xI = 0
yI = 0
print('Les coordonnées de I sont (',xI,';',yI,')')


# ### L'objectif de cette séquence sera de créer un programme permettant de tester si un quadrilatère ABCD est un parallélogramme

# #### I.2. Première étape : création d'une fonction permettant de calculer les coordonnées d'un milieu

# Il n'est pas très pratique de réecrire les lignes de code précédente pour les points C, D et J.
# Nous allons donc utiliser les **fonctions**

# Avant cela il pourrait être utile de découvrir une variable d'un nouveau type : les **_tuples_**




A = (5,-2)
""" tapez A dans la console ci-contre """


# Il est évident que les tuples sont très pratiques dans notre situation car, on peut définir un point en donnant directement ses coordonnées !

# **_Remarque :_** Un tuple peut contenir autre chose que des nombres et peut être constitué de plus de 2 éléments !

# In[ ]:


couple = ('2F',33)
triplet = (1,2,-7.5)


# Maintenant que nous savons définir un tuple, il nous faut apprendre à accéder à une valeur du tuple.
# En fait, un tuple est une "sorte" de liste donc chaque élément est indexé ("numéroté") en commençant à 0.

# In[ ]:


""" tapez A[0] dans la console ci-contre """


# In[ ]:


""" tapez A[1] dans la console ci-contre """


# Nous avons tous les éléments pour créer une fonction : 
# on utilise l'instruction **def** nom_fonction (*argument1,argument2,...*)<span style="color: #fb4141"><b>:</b></span>
# puis l'instruction <span style="color: #fb4141"><b>return</b></span> pour renvoyer un résultat
# par exemple, créons une fonction milieu.

# In[ ]:


def milieu(A,B):
    # milieu a 2 arguments les points A et B
    xI = (A[0]+B[0])/2
    # à compléter avec yI correct
    yI = 0
    
    return (xI,yI)     # la fonction retourne un tuple correspondant aux coordonnées du milieu de [AB] (explication à suivre)


# Décortiquons un peu ce code :
# * **def** permet de créer une fonction que l'on nomme _milieu_
# * cette fonction nécessite deux **arguments** _A_ et _B_ pour être éxécutée
# * A et B étant des tuples pour permettre d'avoir des coordonnées
# * l'instruction **return** permet de récupérer les coordonnées du milieu

# Evaluons cette fonction, A étant déjà définie. Il suffit de créer un deuxième point.

# In[ ]:


B = (7,3)
K = milieu(A,B)
""" tapez K dans la console ci-contre """


# Evidemment il est possible d'utiliser la fonction milieu avec des points autre que A et B.
# Par exemple: milieu(C,D)

# In[ ]:


""" ci-dessous définissez 2 points C et D, et utiliser la fonction milieu pour trouver les coordonnées
 de J milieu de [CD]  """


# <br>Maintenant vous pouvez utiliser la fonction _milieu_ pour générer les coordonnées d'autant de milieu que vous le souhaitez!
# 

#  I.3. Deuxième étape : création d'une fonction parallelogramme

# L'Objectif est de créer une fonction ayant comme arguments 4 points et retournant un message précisant si le quadrilatère est un parallélogramme ou non !

# In[ ]:


def parallelogramme(A,B,C,D):
    # ABCD parallélogramme ?
    
    
    return
    
    

# Testez votre programme avec le code suivant avec 4 points, par exemple M,N,P et Q !

# In[ ]:

""" Dans la console ci-contre définir 4 points :
M=(3,7)
N=(...,...)
P=(...,...)
Q=(...,...)
puis saisir : parallelogramme(M,N,P,Q) pour faire un test utilisez plusieurs valeurs pour M,N,P et Q. """


#  Bravo, vous avez fini le premier objectif ! Il ne reste plus qu'à regrouper toutes les fonctions dans Spyder, pour avoir un programme complet !

# In[ ]:





# II. Objectif : utilisation de la distance.

#  II.1 Distance

# Après avoir créer une fonction milieu, ne nous aretons pas en si bon chemin !
# Nous allons créer une fonction <b><i>distance</i></b> ayant 2 points comme arguments et retournant un réel (la distance)

# In[ ]:


from math import *    # permet d'utiliser la fonction racine carrée noté sqrt
def distance(A,B):
    
    
    return d


# II.2 Triangle rectangle

# Nous allons maintenant créer une fonction <b><i>pythagore</i></b> ayant 3 points comme arguments et qui retourne un message indiquant si le triangle est rectangle ou non.

# In[ ]:


def pythagore (A,B,C):
    
    
    
    
    return
 

#  II.3 Losange et rectangle

# Utilisez les fonctions parallelogramme distance et pythagore pour créer deux fonctions <b>retangle</b> et <b>losange</b> permettant de dire si un quadrilatère est particulier.

# <b>Remarque :</b> les fonctions <b>parallelogramme</b> et <b>pythagore</b> retourneront <span style="color: #fb4141">True</span> ou <span style="color: #fb4141">False </span> pour simplifier le codage.

# <b>Bon Courage ! </b>

# In[ ]:


def losange(A,B,C,D):
    
    
    
    
    return

# In[ ]:


def rectangle(A,B,C,D):
    

    
    
    return