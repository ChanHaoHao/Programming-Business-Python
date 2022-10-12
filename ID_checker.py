s = str(input("Input your ID: "))
s = s.upper()
s = str(ord(s[0])-55)+s[1::]

weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
tmp = 0
for x in range(len(s)):
    tmp += int(s[x])*weight[x]
if (tmp % 10):
    print("False ID")
else:
    print("True ID")