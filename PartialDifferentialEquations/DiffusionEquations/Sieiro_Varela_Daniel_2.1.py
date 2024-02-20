# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N=20; dimt=1000
deltat=0.1;deltax=0.5;alfa=1




#==================APARTADO A======================#

T=np.zeros(N+1);Tn=np.zeros(N+1)
T[9:11]=10#Condiciones iniciales

plt.figure(1);plt.plot(T,"-r");plt.pause(0.1)
plt.title('(a) Ecuación de difusión con focos térmicos a 0 y 10°C')
plt.xlabel('Índice j');plt.ylabel('Índice n')

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = T[i] + alfa*deltat/deltax/deltax * (T[i-1] - 2*T[i] + T[i+1])#FUNCIONA MAS RAPIDO LA OPERACION DIVISION QUE LA OPERACION ELEVAR A
    Tn[0]=0;Tn[N]=10
    for i in range(0,N+1):
        T[i]=Tn[i]
    if n%100==0:
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.5)






#==================APARTADO B======================#

T=np.zeros(N+1);Tn=np.zeros(N+1)
#CAMBIAMOS LAS CONDICIONES INICIALES
T[3:6]=5;T[5]=8;T[6:8]=10; T[8] = 6;T[9:N-3]=3
plt.figure(2);plt.plot(T)
plt.title('(b) Ecuación de difusión con diferentes condiciones iniciales')
plt.xlabel('Índice j');plt.ylabel('Índice n')

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = T[i] + alfa*deltat/deltax/deltax * (T[i-1] - 2*T[i] + T[i+1])#FUNCIONA MAS RAPIDO LA OPERACION DIVISION QUE LA OPERACION ELEVAR A
    Tn[0]=7;Tn[N]=9
    for i in range(0,N+1):
        T[i]=Tn[i]
    if n%100==0:
        plt.figure(2)
        plt.plot(T)
        plt.pause(0.5)




#==================APARTADO C======================#

T=np.zeros(N+1);Tn=np.zeros(N+1)
T[3:6]=10
plt.figure(3);plt.plot(T)
plt.title('(c) Ecuación de difusión con foco término sinusoidal en j=0')
plt.xlabel('Índice j');plt.ylabel('Índice n')

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = T[i] + alfa*deltat/deltax/deltax * (T[i-1] - 2*T[i] + T[i+1])#FUNCIONA MAS RAPIDO LA OPERACION DIVISION QUE LA OPERACION ELEVAR A
    Tn[0]=np.sin(0.5*(n*deltat));Tn[N]=6
    for i in range(0,N+1):
        T[i]=Tn[i]
    if n%100==0:
        plt.figure(3)
        plt.plot(T)
        plt.pause(0.5)





#==================APARTADO D======================#

T=np.zeros(N+1);Tn=np.zeros(N+1)
T[3:6]=10;T[9:14]=9;T[17:19]=2
plt.figure(4);plt.plot(T)
plt.title('(d) Ecuación de difusión con condiciones de frontera de flujo nulo en j=0')
plt.xlabel('Índice j');plt.ylabel('Índice n')

for n in range(dimt):
    for i in range(1,N):
        Tn[i] = T[i] + alfa*deltat/deltax/deltax * (T[i-1] - 2*T[i] + T[i+1])#FUNCIONA MAS RAPIDO LA OPERACION DIVISION QUE LA OPERACION ELEVAR A
    Tn[0]=0;Tn[1]=0;Tn[N]=6
    for i in range(0,N+1):
        T[i]=Tn[i]
    if n%100==0:
        plt.figure(4)
        plt.plot(T)
        plt.pause(0.5)
