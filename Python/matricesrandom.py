#script en python que calcula y muestra la suma de dos matrices
#cuadradas generadas aleatoriamente. Utilizar compresion de listas

import random
N= 3
matriz_A = [[random.randint(1,50) for j in range(N)] for i in range(N)]
matriz_B = [[random.randint(1,50) for j in range(N)] for i in range(N)]
resultado =[[0]*N for i in range(N)] #un vector de N vecs repetido 0

resultado = [[matriz_A[i][j]+ matriz_B[i][j] for j in range(N) ] for i in range(N)] #otra forma
#impresion larga
for i in range(N): #for para recorrer las matrices
    if i == N//2:
        print(f'{matriz_A[i]} +{matriz_B[i]} = {resultado[i]}')
    else:
        print(f'{matriz_A[i]}  {matriz_B[i]} = {resultado[i]}')

#version corta para immpresion
for i in range(N):
     print(f'{matriz_A[i]} +{matriz_B[i]} = {resultado[i]}') if i == N//2 else print(f'{matriz_A[i]}  {matriz_B[i]} = {resultado[i]}')




