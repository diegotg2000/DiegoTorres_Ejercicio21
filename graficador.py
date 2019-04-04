import os
import numpy as np
import matplotlib.pyplot as plt

os.system('g++ DiegoTorres_Ejercicio22.cpp -o  ejercicio.x')
os.system("./ejercicio.x > datos.dat")

datos = np.loadtxt("datos.dat", usecols=0)

x=np.linspace(-3,3)
_=plt.hist(datos, bins=100, density=True)
plt.plot(x, np.exp(-x*x/2)/np.sqrt(2*np.pi))
