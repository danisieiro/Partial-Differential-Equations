# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N=20; dimt=1000
deltat=0.01;deltax=0.5;u=1.;C=u*deltat/deltax

T=np.zeros(N+1);Tn=np.zeros(N+1);To=np.zeros(N+1)
T[9:11]=10#Condiciones iniciales

plt.figure(1);plt.plot(T,"-r");plt.pause(0.1)

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = To[i] - C* (T[i+1] - T[i-1])
    Tn[0]=0;T[N]=0
    for i in range(N+1):
        Tn[i]=0.5*(Tn[i] + T[i])
    Tn[0]=Tn[1];Tn[N]=Tn[N-1]
    To=np.copy(T);T=np.copy(Tn)
    if n%100==0:
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.5)