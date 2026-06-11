# TP 1 Chimie




import numpy as np
import matplotlib.pyplot as plt

# Pour augmenter la police des textes sur les figures pyplot.
plt.rcParams.update({
  "font.size" : 15
})

N = int(1e6) # Nombre de points pour chaque distribution

volume = 200 # en mL


graduation_fiole = 0.25 # (mL)
volume_solution = np.random.uniform(low=volume-graduation_fiole,
                                    high=volume+graduation_fiole,
                                    size=N) # Volume final de la solution


volume_dans_la_pipette = np.random.normal(loc=10, scale=0.02, size=N) # (mL) Volume de la pipette 


plt.figure()
plt.hist(volume_dans_la_pipette, bins=1000, histtype='step', density=True, label='volume_dans_la_pipette')
plt.legend()
plt.show()



volume_dans_la_pipette = np.random.uniform(low=10-0.02,
                                           high=10+0.02, size=N) # (mL) Volume de la pipette 
plt.figure()
plt.hist(volume_dans_la_pipette, bins=1000, histtype='step', density=True, label='volume_dans_la_pipette')
plt.legend()
plt.show()


volume_dans_la_pipette = np.random.triangular(left=10-0.02,
                                              mode = 10,
                                              right=10+0.02,size=N)


plt.figure()
plt.hist(volume_dans_la_pipette, bins=1000, histtype='step', density=True, label='volume_dans_la_pipette')
plt.legend()
plt.show()



# concentration en mol/ml = 0.0001
concentration_solution_mere = np.random.normal(loc=0.0001, scale=0.001*0.0001, size=N) #Volume de la pipette 



#plt.hist(volume_solution)
#plt.hist(volume_dans_la_pipette)
#plt.hist(concentration_solution_mere)
plt.figure()
plt.hist(volume_dans_la_pipette, bins=1000, histtype='step', density=True, label='volume_dans_la_pipette')
plt.legend()
plt.show()


# en mol.ml
concentration_solution_diluee = concentration_solution_mere * volume_dans_la_pipette/volume_solution

c_dil_mol_l = concentration_solution_diluee*1e3

#plt.hist(c_dil_mol_l)


plt.figure()
plt.hist(c_dil_mol_l, bins=1000, histtype='step', density=True, label='concentration_solution_diluee')
plt.legend()
plt.show()



moyenne = np.mean(c_dil_mol_l)
ecart_type = np.std(c_dil_mol_l, ddof=1)

print(f"A partir de la distribution : c = ({moyenne*1e3:.5f} +- {ecart_type*1e3:.5f}) 1e-3 mol/l")

c = np.mean(concentration_solution_mere) * np.mean(volume_dans_la_pipette)/np.mean(volume_solution)
c = c *1e3






