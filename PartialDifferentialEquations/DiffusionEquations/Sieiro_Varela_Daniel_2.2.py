# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N=20; dimt=1000
deltat=0.1;deltax=0.5;alfa=1

T=np.zeros(N+1);Tn=np.zeros(N+1);To=np.zeros(N+1)
T[9:11]=10#Condiciones iniciales


plt.figure(1);plt.plot(T,"-r");plt.pause(0.1)



#CONDICIONES DE DIRICHLET

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = (2*T[i] - 0.5*To[i] + alfa*deltat/deltax/deltax * (T[i-1] - 2*T[i] + T[i+1]))/1.5#FUNCIONA MAS RAPIDO LA OPERACION DIVISION QUE LA OPERACION ELEVAR A
    Tn[0]=7;Tn[N]=7
    To=np.copy(T);T=np.copy(Tn)
    if n%100==0:
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.5)




#CONDICIONES DE NEUMANN SISTEMA AISLADO EN J=0

T=np.zeros(N+1);Tn=np.zeros(N+1);To=np.zeros(N+1)
T[9:11]=10#Condiciones iniciales

plt.figure(2);plt.plot(T,"-r");plt.pause(0.1)

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = (2*T[i] - 0.5*To[i] + alfa*deltat/deltax/deltax * (T[i-1] - 2*T[i] + T[i+1]))/1.5#FUNCIONA MAS RAPIDO LA OPERACION DIVISION QUE LA OPERACION ELEVAR A
    Tn[0]=0;Tn[1]=0;Tn[N]=7
    To=np.copy(T);T=np.copy(Tn)
    if n%100==0:
        plt.figure(2)
        plt.plot(T)
        plt.pause(0.5)