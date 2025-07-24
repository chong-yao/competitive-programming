#Codeforces A. Way Too Long Words
totallines = int(input())
for i in range(totallines):
    word = input()
    lenword = len(word)
    first = word[0]
    last = word[-1]
    mid = lenword - 2
    if lenword > 10:
        print(first+str(mid)+last)

    else:
        print(word)