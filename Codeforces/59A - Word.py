word = input()
lower = 0
upper = 0
for i in word:
    if(i.islower()):
        lower +=1
    else:
        upper +=1

if lower >= upper:
    print(word.lower())
else:
    print(word.upper())