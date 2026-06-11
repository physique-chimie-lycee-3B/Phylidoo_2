# -*- coding: utf-8 -*-

"""
Created on Tue Aug 16 16:25:57 2022

@author: Manon Leconte
"""


###Chargement des bibliothèques

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import scipy.optimize
from scipy import stats
from math import *


###Couleurs

bleuvert=(0,.5,.5)
violet=(.5,0,.5)
jaunefonce=(.5,.5,0)


###Inputs

data = np.loadtxt('donnees_chute_libre.txt') # import depuis le fichier des données
n=50 # nombre de classes pour l'histogramme --- A MODIFIER


###Stats

moyenne=np.average(data) # calcule la moyenne des valeurs stockées dans le tableau X --- A MODIFIER
ecart_type=np.std(data, ddof = 1) # calcule l'écart-type des valeurs stockées dans le tableau X --- A MODIFIER
IT=ecart_type/np.sqrt(105) # incertitude-type (A)
IE=IT*1.66 # incertitude élargie
print(IE)


###Tracé de l'histogramme de distribution des valeurs

plt.hist(data,'rice',facecolor=bleuvert)
plt.xlabel("Temps de chute mesurés") # légende de l’axe des abscisses
plt.ylabel('Effectifs') #légende de l’axe des ordonnées
                      
plt.show()
