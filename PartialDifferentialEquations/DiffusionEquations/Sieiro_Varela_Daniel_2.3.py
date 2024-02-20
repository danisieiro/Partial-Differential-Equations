# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N=20; dimt=1000
deltat=0.01;deltax=0.5;alfa=1

T=np.zeros(N+1);Tn=np.zeros(N+1)
T[9:11]=10#Condiciones iniciales

plt.figure(1);plt.plot(T,"-r");plt.pause(0.1)


#EN ESTE ESQUEMA DEBEMOS DISMINUIR EL VALOR DE
#ALFA DELTAT/DELTAX/DELTAX, PUES EL QUE TENÍAMOS PARA
#EJERCICIOS ANTERIORES NO NOS SIRVE PARA ESTE ESQUEMA, PUES
#SERÍA INESTABLE. REDUCIMOS EL VALOR DE DELTAT A 0.01
#EN VEZ DE 0.1



#===========CONDICIONES DE DIRICHLET=============

for n in range(dimt):
    for i in range(2,N-1):
        Tn[i] = T[i] + alfa*deltat/deltax/deltax * (-1/12 * T[i-2] + 4/3 * T[i-1] - 2.5*T[i] + 4/3*T[i+1] - 1/12 * T[i+2])
    Tn[0]=7;Tn[1]=2;Tn[N]=7;T[N-1]=6 #LAS CONDICIONES DE FRONTERA TIENEN UN GROSOR DE 2 INDICES
    T=np.copy(Tn)
    if n%100==0:
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.5)





#==========CONDICIONES DE NEUMANN==============

T=np.zeros(N+1);Tn=np.zeros(N+1)
T[9:11]=10#Condiciones iniciales

plt.figure(2);plt.plot(T,"-r");plt.pause(0.1)

for n in range(dimt):
    for i in range(2,N-1):
        Tn[i] = T[i] + alfa*deltat/deltax/deltax * (-1/12 * T[i-2] + 4/3 * T[i-1] - 2.5*T[i] + 4/3*T[i+1] - 1/12 * T[i+2])
    Tn[0]=0;Tn[1]=0;Tn[N]=7;T[N-1]=6
    T=np.copy(Tn)
    if n%100==0:
        plt.figure(2)
        plt.plot(T)
        plt.pause(0.5)