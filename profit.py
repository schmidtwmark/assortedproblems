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

def MP_2(k):
    Cache = np.zeros((n+1, 2))
    for l in range(1, k+1):
        for i in range(n-1, -1, -1):
            temp = Next(i) 
            if l % 2 == 1:
                skip = Cache[i+1][1]
                build = Profits[i] + Cache[temp][0]
                Cache[i][1] = max(skip, build)
            else:
                skip = Cache[i+1][0]
                build = Profits[i] + Cache[temp][1]
                Cache[i][0] = max(skip, build)
    print(Cache)

    if k % 2 is 1:
        return Cache[0,1]
    else:
        return Cache[0,0]

MP(2)
print(MP_2(2))



