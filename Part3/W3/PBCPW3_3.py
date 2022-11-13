# a is the request when the good is free
# b is the addition request when opponent raises 1 dollar
# c1, c2 is the price bought by the two stores
# n is the rounds that the store changes price
# p2 = (a+b*p1+c2)/2

data = input("input a, b, c1, c2, n: ").split(",")
a = int(data[0])
b = float(data[1])
c1 = int(data[2])
c2 = int(data[3])
n = int(data[4])
p1 = (a+c1)/2
p2 = (a+b*p1+c2)/2
for x in range(n):
    p1 = (a + b*p2 + c1)/2
    p2 = (a + b*p1 + c2)/2

print("%0.2f %0.2f" % (p1, p2))