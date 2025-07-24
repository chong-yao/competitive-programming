chars = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
allchars = chars.split()
n = int(input())
str = list(input().lower())
res = all(ele in str for ele in allchars)
if res:
    print("YES")
else:
    print("NO")