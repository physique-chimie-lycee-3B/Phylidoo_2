
"""
Created on Thu Aug 3 10:55:00 2023

@author: Manon Leconte
"""

###Chargement des bibliothèques

import numpy as np
import matplotlib.pyplot as plt


###Couleurs

bleuvert=(0,.5,.5)
violet=(.5,0,.5)
jaunefonce=(.5,.5,0)


###Tirages aléatoires

N=100000 #Nombre de tirages simulés

Cm = np.random.normal(0.1,0.0001,N) #loi normale de moyenne X, d'écart-type u --- A MODIFIER
Vm = np.random.triangular(9.98,10,10.02,N) #loi triangulaire de moyenne X, de valeur min Xm et de valeur max XM --- A MODIFIER
Vf = np.random.triangular(199.75,200,200.25,N) #--- A MODIFIER
Cf=Cm * Vm / Vf #Calcul de la concentration fille


###Détermination de l'incertitude-type composée et d'incertitude élargie

Cf_moy = np.average(Cf) #Calcul de la valeur moyenne
uCf = np.std(Cf,ddof=1)/np.sqrt(N) #Calcul de l'écart-type = incertitude-type composée
UCf = 2*uCf #Calcul de l'incertitude élargie

print('Concentration fille : Cf = ',round(Cf_moy,6),' +/- ',round(UCf,6),' mol/L (95 %)')


###Tracé de l'histogramme avec la règle de Rice

plt.hist(Cf, bins='rice',facecolor=bleuvert)
plt.ylabel('Effectifs') #légende de l’axe des ordonnées
plt.xlabel('Valeurs simulées pour Cf') #légende de l’axe des abscisses

plt.show()