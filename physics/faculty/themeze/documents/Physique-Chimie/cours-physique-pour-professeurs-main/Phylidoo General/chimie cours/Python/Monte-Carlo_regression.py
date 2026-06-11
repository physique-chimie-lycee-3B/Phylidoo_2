
"""
Created on Thu Aug 3 13:17:00 2023

@author: Manon Leconte
"""

###Chargement des bibliothèques

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


###Couleurs

bleuvert=(0,.5,.5)
violet=(.5,0,.5)
jaunefonce=(.5,.5,0)


###Import et traitement des données du fichier regression.csv

c,u_c,A,u_A = pd.read_csv('regression.csv', delimiter=';', decimal=',',
                       dtype='float', encoding='utf-8').transpose().to_numpy()
n=len(c)

###Tirages aléatoires

N=10 #Nombre de tirages simulés

a,b=[],[] #initialisation des listes de coefficients directeurs et ordonnées à l'origine

for i in range(N):#réalisation de N régressions linéaires sur des séries de points aléatoires
    c_random=np.zeros(n)
    A_random=np.zeros(n)
    for j in range(n):#génération d'une série de points expérimentaux aléatoire
        c_random[j]=np.random.normal(c[j],u_c[j])
        A_random[j]=np.random.uniform(A[j]-u_A[j],A[j]+u_A[j])
    p=np.polyfit(c_random,A_random,1) #régression linéaire
    a.append(p[0])
    b.append(p[1])


###Détermination de l'incertitude-type composée et d'incertitude élargie

a_moy = np.average(a) #Calcul de la valeur moyenne
b_moy = np.average(b)
u_a = np.std(a,ddof=1)/np.sqrt(N) #Calcul de l'écart-type = incertitude-type composée
u_b = np.std(b,ddof=1)/np.sqrt(N)
U_a = 2*u_a #Calcul de l'incertitude élargie
U_b = 2*u_b

print('Droite de régression :',round(a_moy,0),'x ',round(b_moy,3),'\n U(a) = ',round(U_a,0),' ; U(b) = ',round(U_b,3),' (95 %).')


###Tracé de la droite de régression linéaire

xfit=c

plt.plot(xfit, b_moy + a_moy*xfit,color=violet, label='Régression linéaire')
plt.errorbar(c,A,xerr=u_c ,yerr=u_A,ls='',fmt='',ecolor=bleuvert,zorder=2,label='Points expérimentaux')
plt.title("Droite d'étalonnage pour le curaçao")
plt.xlabel("Concentration (mol/L)")
plt.ylabel("Absorbance")
plt.legend()
plt.show()


plt.show()
