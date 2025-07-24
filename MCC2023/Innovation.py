n, m = map(int, input().split())
ab = []
cd = []
abcd = []
ans = 0
for i in range(n):
    a, b, c, d = map(int, input().split())
    cd.append(c+d)
    abcd.append(a+b+c+d)
    ab.append(a+b)

#finding full value of top most
indexoftopmost = cd.index(max(cd))
fullvalueoftopmost = abcd[indexoftopmost]

#removing the top most
ab.pop(indexoftopmost)
cd.pop(indexoftopmost)
abcd.pop(indexoftopmost)

#getting the continuing ones
print(sum(sorted(ab, reverse = True)[:m-1])+fullvalueoftopmost)

# matrix = []
# with open(r"C:\Users\CY O\Documents\DOCS 2023\coding stuff\MCC\innovation.txt") as f:
#     for i in f:
#         matrix.append(list(map(int, i.split(" "))))

# row_sums = [(row[0] + row[1], sum(row), row) for row in matrix]
# row_sums = sorted(row_sums, key=lambda x: (x[0], -sum(x[2])), reverse = True)

# n = 30
# m = 3
# x = sum(row[0] + row[1] for _, _, row in row_sums[:m-1])
# selected_rows = row_sums[-(n-m+1):]

# max_sum = max([sum(row) for _, _, row in selected_rows])

# result = x + max_sum

# print("x = ", x)
# print("y = ", max_sum)
# print("result", result)