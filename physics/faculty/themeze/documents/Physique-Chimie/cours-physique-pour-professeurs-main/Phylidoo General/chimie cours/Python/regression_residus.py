
# -*- coding: utf-8 -*-

"""
Created on Thu Aug 3 14:55:00 2023

@author: Manon Leconte
"""


###Chargement des bibliothèques

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.optimize
from scipy import stats
from math import *


###Couleurs

bleuvert=(0,.5,.5)
violet=(.5,0,.5)
jaunefonce=(.5,.5,0)
   

###Import et traitement des données du fichier regression.csv

c,u_c,A,u_A = pd.read_csv('regression.csv', delimiter=';', decimal=',', dtype='float', encoding='utf-8').transpose().to_numpy() # import du fichier de données --- A MODIFIER
n=len(c)


###Modélisation

a, b, rvalue, pvalue, stderr = stats.linregress(c,A)
fitline=a*c+b
Residus = [A[i] - fitline[i] for i in range(0,n)]
print("R2 = {}".format(rvalue**2))


###Tracé de la droite de modélisation

plt.figure(1)
plt.errorbar(c,A,xerr=u_c ,yerr=u_A,ls='',fmt='',ecolor=bleuvert,zorder=2,label='Points expérimentaux')
plt.plot(c,fitline,color=violet, label='Régression linéaire')
plt.title("Droite d'étalonnage pour le curaçao")
plt.xlabel("Concentration (mol/L)")
plt.ylabel("Absorbance")
plt.legend()
plt.show()

###Tracé des résidus

plt.figure(2)
y_max=max(np.abs(Residus))+max(u_A)
plt.ylim(-y_max,y_max)
plt.errorbar(c,Residus,xerr=u_c ,yerr=u_A,ls='',fmt='',ecolor=bleuvert,zorder=2)
plt.title("Résidus")
plt.xlabel("Concentration (mol/L)")
plt.axhline(linewidth=1,color=violet)
plt.axhline(y=-2*max(u_A),ls=':',linewidth=.5,color=violet)
plt.annotate("2 $u(A)$",(1e-6,2*max(u_A)),color=violet)
plt.axhline(y=2*max(u_A),ls=':',linewidth=.5,color=violet)
plt.annotate("$-2 u(A)$",(9e-6,-2*max(u_A)),color=violet)
plt.show()