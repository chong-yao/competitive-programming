a = int(input())
b = int(input())
c = int(input())

res1 = a + b + c
res2 = a * b * c
res3 = a + b * c
res4 = a * b + c
res5 = (a + b) * c
res6 = a * (b + c)

print(max(res1, res2, res3, res4, res5, res6))