line1=[int(x) for x in input().split()]
line2=[int(x) for x in input().split()]
line3=[int(x) for x in input().split()]
line4=[int(x) for x in input().split()]
line5=[int(x) for x in input().split()]

if 1 in line1:
    vertperm = 2
    horizperm = line1.index(1)
elif 1 in line2:
    vertperm = 1
    horizperm = line2.index(1)
elif 1 in line3:
    vertperm = 0
    horizperm = line3.index(1)
elif 1 in line4:
    vertperm = 1
    horizperm = line4.index(1)
elif 1 in line5:
    vertperm = 2
    horizperm = line5.index(1)

print(vertperm + abs(horizperm - 2))