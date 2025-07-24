x = input()
n = input()
if n.count("A") > n.count("D"):
    print("Anton")
elif n.count("A") == n.count("D"):
    print("Friendship")
else:
    print("Danik")