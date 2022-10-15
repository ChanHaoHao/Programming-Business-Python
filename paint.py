x, y = input().split(" ")
x = int(x)
y = int(y)
paint = [1]*x
tmpColor = []
for z in range(y):
    start, stop, color = input().split(" ")
    start = int(start)
    stop = int(stop)
    color = int(color)
    tmpColor.append(color)

    for c in range(start-1, stop):
        paint[c] = color
print(tmpColor)
ans = [0]*len(tmpColor)
for x in paint:
    if x==1 and 1 not in tmpColor:
        continue
    ans[tmpColor.index(x)] += 1
for x in range(len(ans)-1):
    print(ans[x], tmpColor[x], end=";")
print(ans[-1], tmpColor[-1])