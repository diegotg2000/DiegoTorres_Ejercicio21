import os
import numpy as np
import matplotlib.pyplot as plt

os.system('g++ generador.cpp -o  ejercicio.x')
os.system("./ejercicio.x > datos.dat")

data = np.loadtxt("datos.dat")

plt.figure()
plt.plot(data[:,0], data[:,1])
plt.savefig("datos.png")
