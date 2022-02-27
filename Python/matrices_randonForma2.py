#cuadradas generadas aleatoriamente. Utilizar compresion de listas

import random
N= 3
matriz_A = [[random.randint(1,50) for j in range(N)] for i in range(N)]
matriz_B = [[random.randint(1,50) for j in range(N)] for i in range(N)]
resultado =[[0]*N for i in range(N)] #un vector de N vecs repetido 0
#suma primera forma
for renglon in range(N):
    for columna in range(N):
        resultado[renglon][columna]= matriz_A[renglon][columna] + matriz_B[renglon][columna]
for i in range(N):
    if i == N//2:
        print(f'{matriz_A[i]} +{matriz_B[i]} = {resultado[i]}')
    else:
        print(f'{matriz_A[i]}  {matriz_B[i]} = {resultado[i]}')