x = int(input())
y = int(input())
z = int(input())

if (z>x):
    y += x
    x = 0
else:
    x -= z
    y += z

print(x,y)