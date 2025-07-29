letters1 = list(input())
ans = 0
allletters = list("abcdefghijklmnopqrstuvwxyz")
for i in range(len(allletters)):
    if (allletters[i] in letters1) > 0:
        ans+=1
        
print(ans)