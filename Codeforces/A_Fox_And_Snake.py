n, m = map(int, input().split())

snake = ["#"*m]

rightsnake = True

for i in range(2, n+1):
    if i%2 == 0:
        if rightsnake == True:
            snake.append("."*(m-1) + "#")
        else:
            snake.append("#" + ("."*(m-1)))
        rightsnake = not rightsnake

    elif i%3 == 0:
        snake.append("#"*m)

    else:
        snake.append("#"*m)

print(*snake, sep = "\n")