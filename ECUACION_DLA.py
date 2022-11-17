import numpy as np
import matplotlib.pyplot as plt
import random

#resolución de la imagen
altura_columnas=30
ancho_filas=30

R=random.uniform(0.0,1)
P=np.zeros([ancho_filas,altura_columnas])
P[15,15]=1.0

for i in range(29):
    for j in range(29):
        P[i,j]=0.25*(P[i+1,j]+P[i-1,j]+P[i,j+1]+P[i,j-1])
        
plt.figure(figsize=(5,5))
plt.imshow(P.T,cmap='Greys')
plt.ylim(0,29)
plt.xlim(0,29)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
