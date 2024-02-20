# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N=20; dimt=1000
deltat=0.1;deltax=0.5;alfa=1
s=alfa*deltat/deltax/deltax

T=np.zeros(N+1);Tn=np.zeros(N+1);To=np.zeros(N+1)
T[0]=3;T[N]=3;T[9:11]=10;T[2:9]=16;T[11:13]=3;T[13:19]=16#Condiciones iniciales


plt.figure(1)
#plt.plot(T,"-r");plt.pause(0.1)



#CONDICIONES DE DIRICHLET

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = 2*s/(1+2*s) * (T[i-1] + T[i+1]) + (1-2*s)/(1+2*s) * To[i]
    Tn[0]=3;Tn[N]=3
    for j in range(0,N+1):
        Tn[j]=0.5*(Tn[j]+T[j])
    To=np.copy(T);T=np.copy(Tn)
    if n%100==0:
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.5)




#CONDICIONES DE NEUMANN SISTEMA AISLADO EN J=0

T=np.zeros(N+1);Tn=np.zeros(N+1);To=np.zeros(N+1)
T[0]=0;T[N]=7;T[9:11]=10;T[2:9]=16;T[11:13]=3;T[13:19]=16#Condiciones iniciales

plt.figure(2)
#plt.plot(T,"-r");plt.pause(0.1)

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = 2*s/(1+2*s) * (T[i-1] + T[i+1]) + (1-2*s)/(1+2*s) * To[i]
    Tn[0]=0;Tn[1]=0;Tn[N]=7
    for j in range(0,N+1):
        Tn[j]=0.5*(Tn[j]+T[j])
    To=np.copy(T);T=np.copy(Tn)
    if n%100==0:
        plt.figure(2)
        plt.plot(T)
        plt.pause(0.5)