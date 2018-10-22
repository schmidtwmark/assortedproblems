import numpy as np

Distances = [1, 1.5, 3, 5]
Profits = [5, 9, 8, 2]

D = 1
n = len(Distances)

def Next(i):
    for j in range(i+1, n):
        if(Distances[i] + D < Distances[j]):
            return j
    return n

def MP(k):
    Cache = np.zeros((n+1,k+1))
    for i in range(n-1, -1, -1):
        temp = Next(i)
        for l in range(1, k+1):
            
            skip = Cache[i+1][l]
            build = Profits[i] + Cache[temp][l-1]
            Cache[i][l] = max(skip, build)
    print(Cache)

MP(3)




