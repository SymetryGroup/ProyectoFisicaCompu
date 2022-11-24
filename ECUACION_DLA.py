from random import choice
import numpy as np
import matplotlib.pyplot as plt

npart=10000 #Numero de particulas del agregado
tama=150 #tamaño de la imagen
dir = [(1,0),(-1,0),(0,1),(0,-1)] #direcciones para la difusion



grid=[[0 for x in range(tama)] for y in range(tama)]
grid[int(tama/2)][int(tama/2)]=1
for ipart in range(npart):
    # 
    x,y = 0,0
    # Inicio de la caminata aleatoria
    while 1:
        grid[x][y]=0 #Eliminar partículas del lugar actual
        # Movimiento de particulas aleatorias
        sx,sy = choice(dir)
        x += sx
        y += sy
        # Caminos donde se añaden las particulas
        if x < 0: 
            x=tama-1
        if y < 0: 
            y=tama-1
        if x==tama: 
            x=0
        if y==tama: 
            y=0
        grid[x][y]=1 #Pone la partícula en una nueva ubicación
        # se detiene si está al lado de una partícula
        if (grid[(x+1)%tama][y]+grid[x][(y+1)%tama]+grid[(x+tama-1)%tama][y]+grid[x][(y+tama-1)%tama])>0:
            break

plt.imshow(grid,interpolation="bilinear",cmap="gray")
