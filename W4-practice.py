# buy price
c = int(input())
# sell price
r = int(input())
# sold num
n = int(input())
# buy num
q= int(input())

probability = []
for x in range(0,n+1):
    probability.append(float(input()))
print(" ")

tmp = 0
for x in range(0,q+1):
    if (x != q):
        tmp += ((-c)*q+x*r)*probability[x]
    else:
        tmp += ((-c)*q+x*r)*sum(probability[x::])
print(q, tmp)