import matplotlib.pyplot as plt
import numpy as np




r = 4e-3 / 2        # rayon de la bille (m)
g = 9.81            # accélération de pesanteur (m/s)
mu_b = 7.8e3        # masse volumique de la bille (kg/L)
mu_h = 0.97e3        # masse volumique de l'huile silicone (kg/L)
eta = 0.5           # viscosité dynamique de l'huile (PA.s)









data = np.array([0.1085166 , 0.08952917, 0.10146745, 0.09883515, 0.09006254,
       0.1163983 , 0.10427756, 0.11103207, 0.06917342, 0.08241197,
       0.12319323, 0.09602415, 0.1355468 , 0.10352657, 0.09150465,
       0.10953144, 0.07461392, 0.10139349, 0.09441104, 0.09698972,
       0.09516845, 0.11974437, 0.08645809, 0.09646799, 0.08671181,
       0.112465  , 0.11699316, 0.10717084, 0.08286318, 0.11186971,
       0.11863431, 0.09816004, 0.11529022, 0.09613429, 0.08654955,
       0.09761018, 0.12014731, 0.08512864, 0.10959338, 0.11157745,
       0.12188089, 0.09695674, 0.0991507 , 0.08989498, 0.09756408,
       0.08043863, 0.12714415, 0.09052691, 0.09584994, 0.07831345])

#data = np.random.normal(loc=0.102, scale=0.02, size=50)






###Tracé de l'histogramme de distribution des valeurs
n = 10
plt.hist(data,n)
plt.xlabel("Vitesses limites mesurés")
plt.ylabel('Effectifs')
plt.show()



v_th = 2/9*((mu_b - mu_h)/eta)*r**2*g
print("La valeur théorique de v est: " +f"{v_th:.3g}" + "m/s")   # moyenne
print("La valeur expérimentale de v est: " +f"{data.mean():.3g}" + "m/s" + ' \u00B1' +\
      f"{data.std():.2g}")   # moyenne

Zscore = np.abs(v_th-data.mean())/data.std()
print("On a un Z-score de: " + f"{Zscore:.3g}")







Re = (mu_b*r*v_th)/eta
print('Re = ',Re)





def oseen(r, g, mu_b, mu_h, eta):
    A = (9/4)*np.pi*mu_h*r**2
    B = 6*np.pi*eta*r
    C = (4/3)*np.pi*r**3*g*(mu_h-mu_b)

    delta = B**2 - 4*A*C
    x1 = (-1*B - np.sqrt(delta))/(2*A)
    x2 = (-1*B + np.sqrt(delta))/(2*A)

    return [x1,x2]

v_thO = oseen(r, g, mu_b, mu_h, eta)[1]
print("L'approximation d'Oseen nous donne: v = " +f"{v_thO:.3g}" + "m/s")   # moyenne

Zscore2 = np.abs(v_thO-data.mean())/data.std()
print("On a un Z-score de: " + f"{Zscore2:.3g}")





#*(1-2.1*r/0.1)































#7.9e-3 / 2













