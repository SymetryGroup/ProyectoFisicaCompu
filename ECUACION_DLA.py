import numpy as np
import matplotlib.pyplot as plt
import random

#resolución de la imagen
altura_columnas=50
ancho_filas=50


P=np.zeros([ancho_filas,altura_columnas])
P[25,25]=1.0
for t in range(500):
    plt.imshow(P.T,cmap='Greys')
    R=random.uniform(0,0.01)

    for i in range(49):
        for j in range(49):
            P[i,j]=0.25*(P[i+1,j]+P[i-1,j]+P[i,j+1]+P[i,j-1]+R)

plt.ylim(0,49)
plt.xlim(0,49)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
