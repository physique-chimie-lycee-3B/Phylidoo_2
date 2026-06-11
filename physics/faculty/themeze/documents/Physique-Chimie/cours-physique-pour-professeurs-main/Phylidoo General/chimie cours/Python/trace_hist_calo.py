# -*- coding: utf-8 -*-

"""
Created on Tue Aug 16 16:25:57 2022

@author: Manon Leconte
"""


###Chargement des bibliothèques

import matplotlib.pyplot as plt
import numpy as np


###Couleurs

bleuvert=(0,.5,.5)
violet=(.5,0,.5)
jaunefonce=(.5,.5,0)


###Inputs

data=[5.10,4.23,3.75,4.56,3.98]
titre='Distribution des valeurs obtenues lors du TP'

ecart_type=np.std(data, ddof = 1) # calcule l'écart-type des valeurs
IT=ecart_type/np.sqrt(5) # incertitude-type (A)
IE=IT*2.132 # incertitude élargie
print(IE)


###Tracé de l'histogramme avec la règle de Rice

plt.hist(data, bins='rice',label=titre,facecolor=bleuvert)
plt.xlabel("Valeurs mesurées pour la capacité calorifique de l'eau") # légende de l’axe des abscisses
plt.ylabel('Effectifs') #légende de l’axe des ordonnées
plt.legend() # affichage du titre du graphique
plt.show()