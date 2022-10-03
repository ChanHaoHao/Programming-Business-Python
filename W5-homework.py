import math
import matplotlib.pyplot as plt
import numpy as np

n = -1
p = -1
d = -1
a=[]
b=[]
cityCor = []
cityBool = []
while True:
    x = input()
    if (x != ''):
        x = x.split()
        if (n != -1):
            a.append(int(x[0]))
            b.append(int(x[1]))
            cityCor.append([int(x[0]), int(x[1]), int(x[2])])
            cityBool.append(0)
        else:
            n = int(x[0])
            p = int(x[1])
            d = int(x[2])
    else:
        break

cityInd = [-1]*(p+1)
for y in range(p):
    tmp, tmpPeople = 0, 0

    for x in range(len(cityCor)):
        cur = 0
        if cityBool[x]==0:
            cur=cityCor[x][2]
        if x not in cityInd:
            for z in range(len(cityCor)):
                if (z!=x):
                    if (cityBool[z]==0 and math.sqrt((cityCor[x][0]-cityCor[z][0])*(cityCor[x][0]-cityCor[z][0]) 
                        + (cityCor[x][1]-cityCor[z][1])*(cityCor[x][1]-cityCor[z][1])) <= d):
                        cur += cityCor[z][2]
            if (cur > tmpPeople and cur!=0):
                tmp, tmpPeople = x, cur
    cityBool[tmp] = 1
    for x in range(len(cityCor)):
        if (math.sqrt((cityCor[x][0]-cityCor[tmp][0])*(cityCor[x][0]-cityCor[tmp][0]) 
            + (cityCor[x][1]-cityCor[tmp][1])*(cityCor[x][1]-cityCor[tmp][1])) <= d):
            cityBool[x] = 1
    cityInd[y] = tmp
    cityInd[-1] += tmpPeople
for x in cityInd:
    print(x+1, end=' ')

fig, axe = plt.subplots()
axe.set_aspect(1)
points = plt.scatter(a, b, s=1)
axe.add_artist(points)
for x in range(p):
    circle1 = plt.Circle((cityCor[cityInd[x]][0], cityCor[cityInd[x]][1]), d, fill=False)
    axe.add_artist(circle1)
plt.show()