x = 1000 - int(input())
money = [500,100,50,10,5,1]
for y in money:
    if (x//y > 0):
        print(y, end='')
        print(", ", end='')
        print(x//y, end='')
        x -= x//y*y
        if y!=1:
            print("; ", end='')