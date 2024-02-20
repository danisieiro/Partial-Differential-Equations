# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N=20; dimt=1000
deltat=0.001;deltax=0.5;u=3.;C=u*deltat/deltax;alfa=1.;s=alfa*deltat/deltax/deltax

T=np.zeros(N+1);Tn=np.zeros(N+1)
T[9:11]=10#Condiciones iniciales

plt.figure(1);plt.plot(T,"-r");plt.pause(0.1)


for n in range(dimt):
    for i in range(1,N):
        Tn[i] = alfa*deltat/deltax/deltax * (T[i-1] - 2*T[i] + T[i+1]) - u*deltat/2/deltax * (T[i+1] - T[i-1]) + T[i]
    Tn[0]=0;T[N]=0
    T=np.copy(Tn)
    if n%100==0:
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.5)