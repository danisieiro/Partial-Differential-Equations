# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N=20;dimt=1000
T=np.zeros((N+1,N+1));Tn=np.copy(T)

alfa=1.;deltat=0.001;deltax=0.5;C=alfa*deltat/deltax/deltax

T[10,10]=3.

plt.figure(1);plt.pcolor(T);plt.colorbar();plt.clim(0,13)
plt.pause(0.2)

for n in range(dimt):
    for i in range(1,N):
        for j in range(1,N):
            Tn[i,j] = T[i,j] + C * (T[i-1,j] - 2*T[i,j] + T[i+1,j] + T[i,j-1] - 2*T[i,j] + T[i,j+1])
    Tn[0,:]=10.;Tn[N,:]=13.;Tn[:,0]=5.;Tn[:,N]=7.
    T=np.copy(Tn)
    if n%100==0:
        plt.figure(1)
        plt.pcolor(T)
        plt.clim(0,13)
        plt.pause(0.2)