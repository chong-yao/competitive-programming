ans = [int(input())]

while ans[-1] != 1:
    if ans[-1] % 2 == 0:
        ans.append(ans[-1] / 2)

    else:
        ans.append(ans[-1]*3 + 1)

print(*[int(x) for x in ans])