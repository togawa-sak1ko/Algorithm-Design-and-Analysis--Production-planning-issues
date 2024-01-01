import numpy as np
import sys

def func(n, d, m, c):
    D = [0] * n
    cost = np.zeros((n, sum(d)+1),dtype = int)
    p = np.zeros((n, sum(d)+1),dtype = int)
    D[0] = d[0]
    for i in range(1, n):
        D[i] = D[i - 1] + d[i]
    for i in range(n):
        for j in range(D[i], D[n-1]+1):
            if(i == 0):
                cost[i][j] = 5*(j-D[0])
                if(j > m):
                    cost[i][j] = cost[i][j]+c*(j-m)
                p[i][j] = j
            else:
                cost[i][j] = 9999
                for k in range(0, j-D[i-1]+1):
                    t = cost[i-1][j-k] + 5*(j-D[i])
                    if(k > m):
                        t = t+c*(k-m)
                    if(t < cost[i][j]):
                        cost[i][j] = t
                        p[i][j] = k
    return p

def func1(p, i, j, sss):
    if(i >= 0):
        a = int(j-p[i][j])
        print(i, j, p[i][j])
        func1(p, i-1, a, sss)
        sss.append(p[i][j])

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split(" ")))

p = func(n, d, m, c)
sss = []
func1(p, n-1, sum(d), sss)
for i in range(len(sss)):
    if(i != len(sss) - 1):
        sys.stdout.write(str(sss[i]))
        sys.stdout.write(" ")
    else:
        sys.stdout.write(str(sss[i]))

